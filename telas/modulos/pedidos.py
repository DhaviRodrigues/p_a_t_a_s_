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

    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        return {
            "id_mensagem": self.id_mensagem,
            "nome_animal": self.nome_animal,
            "id_animal": self.id_animal,
            "id_usuario": self.id_usuario,
            "nome_usuario": self.nome_usuario,
            "email_usuario": self.email_usuario,
            "processo": self.processo
        }


    def criar_pedido_adocao(animal_clicado, usuario_logado):
        pedidos = carregar_dados('pedidos_pedente.json')

        maior_id_atual = -1 
        for pedido_existente in pedidos:
            if pedido_existente['id_mensagem'] > maior_id_atual:
                maior_id_atual = pedido_existente['id_mensagem']
        id_mensagem = maior_id_atual + 1
        processo = "Em análise, verifique sempre seu email."
        novo_pedido = Pedidos(id_mensagem, animal_clicado['nome'], animal_clicado['id'], usuario_logado['id'], usuario_logado['nome'], usuario_logado['email'], processo)
        
        todos_usuarios = usercrud.carregar_dados("usuarios.json")
        for usuario in todos_usuarios:
            if usuario.get("id") == usuario_logado['id']:
                usuario["pedido"] = True
                break
        usercrud.salvar_dados("usuarios.json", todos_usuarios)
        usuario_logado['pedido'] = True


        todos_animais = animalcrud.carregar_dados("animais_adocao.json")
        for animal in todos_animais:
            if animal.get("id") == animal_clicado['id']:
                animal["processo_adoacao"] = True
                break
        animalcrud.salvar_dados("animais_adocao.json", todos_animais)


            # novo_pedido = {
            #     'id_mensagem': id_mensagem,
            #     'nome_animal': nome_animal,
            #     'id_usuario': usuario_logado['id'],
            #     'id_animal_adotado': id_animal,
            #     'nome_usuario': usuario_logado['nome'],
            #     'email_usuario': usuario_logado['email'],
            # }

        pedidos.append(novo_pedido.converter_para_dicionario())
        salvar_dados('pedidos_pendente.json', pedidos)

    def pedidos_adocao():
        print("\n--- Lista de Pedidos de Adoção ---")
        pedidos = carregar_dados('pedidos.json')

        if not pedidos:
            print("Não há pedidos de adoção registrados no momento.")
            
            return

        for pedido in pedidos:
            print("-" * 30)
            print(f"ID Mensagem: {pedido.get('id_mensagem', )}")
            print(f"Animal: {pedido.get('nome_animal')}") 
            print(f"ID: {pedido.get('id_animal_adotado')}")
            print(f"Usuario: {pedido.get('nome_usuario')}")
            print(f"E-mail: {pedido.get('email_usuario')}")
            print(f"Mensagem: {pedido.get('mensagem_pedido')}")
            print("-" * 30)
        

    def deletar_pedido():
        print("\n--- Deletar Pedido de Adoção ---")
        while True:
            id_deletar = input("Insira o ID da mensagem do pedido que deseja deletar (Digite VOLTAR para o menu): ").strip().lower()
            
            if id_deletar == "voltar":
                print("Operação de exclusão de pedido cancelada.")
                
                return
            else:
                id_deletar = int(id_deletar)

            pedidos = carregar_dados('pedidos.json')
            
            nova_lista_pedidos = []
            for pedido in pedidos:
                if pedido.get('id_mensagem') == id_deletar:
                    pedido_encontrado = pedido
            
            if pedido_encontrado is None:
                print(f"Não foi encontrado nenhum pedido com o ID {id_deletar}.")
                
                continue
            
            while True:
                confirmacao_exclusao = input(str(f"Tem certeza que deseja deletar o pedido do animal '{pedido_encontrado.get('nome_animal')}' (ID Mensagem: {id_deletar})? (S/N): ")).strip().lower()
                if confirmacao_exclusao == 's':
                    nova_lista_pedidos = []
                    for pedido in pedidos:
                        if pedido.get('id_mensagem') != id_deletar:
                            nova_lista_pedidos.append(pedido)
                    salvar_dados('pedidos.json', nova_lista_pedidos)
                    print(f"Pedido com ID {id_deletar} deletado com sucesso.")
                    
                    return
                
                elif confirmacao_exclusao == 'n':
                    print("Exclusão de pedido cancelada.")
                    
                    return
                else:
                    print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
                    

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
