import json
from . import usercrud
from . import animalcrud


class Pedidos:
    """Classe que representa um pedido de adoção"""
    def __init__(self, id_mensagem, nome_animal, id_animal, id_usuario, nome_usuario, email_usuario, processo):
        self.id_mensagem = id_mensagem
        self.nome_animal = nome_animal
        self.id_animal = id_animal
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.processo = processo

    def converter_para_dicionario(self):
        return {
            "id_mensagem": self.id_mensagem,
            "nome_animal": self.nome_animal,
            "id_animal": self.id_animal,
            "id_usuario": self.id_usuario,
            "nome_usuario": self.nome_usuario,
            "email_usuario": self.email_usuario,
            "processo": self.processo
        }


    # Cria um novo pedido de adoção.
    def criar_pedido_adocao(animal_clicado, usuario_logado):
        # Carrega os pedidos pendentes do arquivo JSON.
        pedidos = carregar_dados('pedidos_pedente.json')

        # Encontra o maior ID de mensagem existente para gerar um novo ID.
        maior_id_atual = -1 
        for pedido_existente in pedidos:
            if pedido_existente['id_mensagem'] > maior_id_atual:
                maior_id_atual = pedido_existente['id_mensagem']
        id_mensagem = maior_id_atual + 1
        # Define o status inicial do processo de adoção.
        processo = "Em análise, verifique sempre seu email."
        # Cria uma nova instância de Pedidos.
        novo_pedido = Pedidos(id_mensagem, animal_clicado['nome'], animal_clicado['id'], usuario_logado['id'], usuario_logado['nome'], usuario_logado['email'], processo)
        
        # Atualiza o status do pedido do usuário para True.
        todos_usuarios = usercrud.carregar_dados("usuarios.json")
        for usuario in todos_usuarios:
            if usuario.get("id") == usuario_logado['id']:
                usuario["pedido"] = True
                break
        usercrud.salvar_dados("usuarios.json", todos_usuarios)
        usuario_logado['pedido'] = True


        # Atualiza o status de 'processo_adoacao' do animal para True.
        todos_animais = animalcrud.carregar_dados("animais_adocao.json")
        for animal in todos_animais:
            if animal.get("id") == animal_clicado['id']:
                animal["processo_adoacao"] = True
                break
        animalcrud.salvar_dados("animais_adocao.json", todos_animais)

        # Adiciona o novo pedido à lista de pedidos pendentes e salva no arquivo.
        pedidos.append(novo_pedido.converter_para_dicionario())
        salvar_dados('pedidos_pendente.json', pedidos)


    def aceitar_pedido(pedido_usuario):
        from . import animalcrud
        
        # Remove o pedido da lista de pendentes
        pedidos_pendentes = carregar_dados('pedidos_pendente.json')
        pedidos_pendentes_atualizados = []
        for pedido in pedidos_pendentes:
            if pedido.get('id_mensagem') != pedido_usuario.get('id_mensagem'):
                pedidos_pendentes_atualizados.append(pedido)
        salvar_dados('pedidos_pendente.json', pedidos_pendentes_atualizados)

        # Adiciona o pedido à lista de aprovados
        pedidos_aprovados = carregar_dados('pedidos_aprovado.json')
        pedidos_aprovados.append(pedido_usuario)
        salvar_dados('pedidos_aprovado.json', pedidos_aprovados)

        # Altera a chave 'pedido' do usuário para False
        todos_usuarios = usercrud.carregar_dados("usuarios.json")
        for usuario in todos_usuarios:
            if usuario.get("id") == pedido.get("id_usuario"):
                usuario["pedido"] = False
                break
        usercrud.salvar_dados("usuarios.json", todos_usuarios)

        # Chama a função para mover os dados do animal
        animalcrud.Animal.mover_animal_para_adotados(pedido_usuario.get('id_animal'))

        destinatario = pedido.get('email_usuario')
        assunto = "Adoção Aprovada! Seu novo amigo está a sua espera!"
        corpo = f"""Olá, {pedido_usuario.get('nome_usuario')}!

Temos uma notícia maravilhosa! Seu adoção para o(a) {pedido_usuario.get('nome_animal')} aconteceu com sucesso!

Estamos muito felizes por você e por ele(a). Temos certeza que ele receberá todo o amor e carinho que merece.

E também prepare-se para muito amor e carinho vindo dele!  :)

Atenciosamente,
Equipe P.A.T.A.S.
"""
        codigo = ""
        usercrud.Usuario.enviar_email(destinatario, codigo, corpo, assunto)
    

    def recusar_pedido(pedido_usuario):
        from . import animalcrud

        # Remove o pedido da lista de pendentes
        pedidos_pendentes = carregar_dados('pedidos_pendente.json')
        pedidos_pendentes_atualizados = []
        for pedido in pedidos_pendentes:
            if pedido.get('id_mensagem') != pedido_usuario.get('id_mensagem'):
                pedidos_pendentes_atualizados.append(pedido)
        salvar_dados('pedidos_pendente.json', pedidos_pendentes_atualizados)

        # Adiciona o pedido à lista de recusados
        pedidos_recusados = carregar_dados('pedidos_recusado.json')
        pedidos_recusados.append(pedido_usuario)
        salvar_dados('pedidos_recusado.json', pedidos_recusados)

        # Altera a chave 'pedido' do usuário para False
        todos_usuarios = usercrud.carregar_dados("usuarios.json")
        for usuario in todos_usuarios:
            if usuario.get("id") == pedido_usuario.get("id_usuario"):
                usuario["pedido"] = False
                break
        usercrud.salvar_dados("usuarios.json", todos_usuarios)

        # Altera a chave 'processo_adocao' do animal para False
        todos_animais = animalcrud.carregar_dados("animais_adocao.json")
        for animal in todos_animais:
            if animal.get("id") == pedido_usuario.get("id_animal"):
                animal["processo_adocao"] = False
                break
        animalcrud.salvar_dados("animais_adocao.json", todos_animais)

        # Envia e-mail de recusa
        destinatario = pedido_usuario.get('email_usuario')
        assunto = "Pedido de Adoção Recusado"
        corpo = f"""Olá, {pedido_usuario.get('nome_usuario')}.

Agradecemos o seu interesse em adotar o(a) {pedido_usuario.get('nome_animal')}, mas infelizmente o seu pedido foi recusado.

Determinamos que essa adoção não seria a melhor opção para o animal.

Atenciosamente,  
Equipe P.A.T.A.S."""
        codigo = ""
        usercrud.Usuario.enviar_email(destinatario, codigo, corpo, assunto)

def carregar_dados(arquivo):
    """Carrega o arquivo json dos animais"""
    try:
        with open(arquivo, 'r') as arquivo:
            #Tenta abrir o arquivo em modo 'r'(leitura)
            dados = json.load(arquivo)
            #Insere as informações do arquivo json em "dados"
            return dados
    except FileNotFoundError:
        #Se o arquivo não for encontrado, ele retornará o arquivo com uma lista em branco no nome informado na variável "arquivo"
        return []

def salvar_dados(arquivo, dados):
    """Salva as informações no arquivo json dos animais"""
    with open(arquivo, 'w') as arquivo:
        #Abre o arquivo json em modo 'w'(write)
        json.dump(dados, arquivo, indent=6)
        #json é a biblioteca importada, .dump() é a função que vai jogar da primeira variável, dentro do "arquivo" de animais.json, indent=6 é apenas para deixar mais organizado na hora da escrita do arquivo
