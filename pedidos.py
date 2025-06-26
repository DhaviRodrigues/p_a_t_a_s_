import json
import os
from time import sleep
import animalcrud
import pedidos

class Pedidos:
    """Classe que representa um pedido de adoção"""
    def __init__(self, id_mensagem, nome_animal, id_animal, id_usuario, nome_usuario, email_usuario, mensagem):
        self.id = id_mensagem
        self.nome_animal = nome_animal
        self.id_animal = id_animal
        self.id_usuario = id_usuario
        self.nome_usuario = id_usuario
        self.email_usuario = id_usuario
        self.mensagem = mensagem

    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        return {
            "id": self.id,
            "id_animal": self.id_animal,
            "id_usuario": self.id_usuario,
            "mensagem": self.mensagem
        }


def enviar_pedido_adocao(usuario_logado):
    """Permite que o usuário faça uma solitação de adoção de um pet, o pedido será enviado a equipe administrativa, que entrará em contato com quem fez o pedido"""
    animais_adocao = animalcrud.carregar_dados('animais_adocao.json')
    while True:
        if not animais_adocao:
            print("Não há animais disponíveis para adoção no momento.")
            sleep(2)
            return

        id_animal = input ("Informe o id que gostaria de adotar (Digite VOLTAR para ir ao menu principal): ")
        if id_animal.upper() == "VOLTAR":
            return

        if id_animal.isdigit() == False:
            print("Insira apenas números")
            continue
        else:
            id_animal = int(id_animal)

        animal_selecionado = None
        for animal_lista in animais_adocao:
            if animal_lista.get('id') == id_animal:
                animal_selecionado = animal_lista
                break

        if animal_selecionado is None:
            print(" O ID digitado não corresponde a nenhum animal disponível para adoção.")
            sleep(2)
            continue

        nome_animal = animal_selecionado.get('nome') 

        print("\n--- Enviar Pedido de Adoção ---") 
        while True:
            confirmacao = input(str(f"Tem certeza que deseja fazer um pedido de adoção para o animal ID {id_animal}? (S/N): ")).strip().lower()
            if confirmacao == 's':
                break
            elif confirmacao == 'n':
                print("Pedido de adoção cancelado.")
                sleep(2)
                return
            else:
                print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
                sleep(1)
        sleep(1)
        print("\n--- Escreva seu Pedido de Adoção ---")
        print("--------------------------------------------------")
        print("Modelo Sugerido:")
        print("--------------------------------------------------")
        print("""Bom dia, gostaria de adotar um animal, seu id é XX,
para entrar em contato comigo use meu email, ou meu
telefone: (81) 9.1234-5678""")
        sleep(2)

        mensagem = input(str("Digite sua mensagem, siga o modelo se preferir: (apenas aperte ENTER quando digitar toda mensagem) ")).strip()
        while not mensagem:
            print("A mensagem não pode estar vazia. Por favor, digite seu pedido.")
            mensagem = input(str("Sua mensagem: ")).strip()

        pedidos = carregar_dados('pedidos.json')

        id_mensagem = 0
        if pedidos:
            maior_id_atual = -1 
            for pedido_existente in pedidos:
                if pedido_existente['id_mensagem'] > maior_id_atual:
                    maior_id_atual = pedido_existente['id_mensagem']
            id_mensagem = maior_id_atual + 1

        novo_pedido = Pedidos(id_mensagem, nome_animal, id_animal, usuario_logado['nome'], usuario_logado['email'], mensagem)

        # novo_pedido = {
        #     'id_mensagem': id_mensagem,
        #     'nome_animal': nome_animal,
        #     'id_animal_adotado': id_animal,
        #     'nome_usuario': usuario_logado['nome'],
        #     'email_usuario': usuario_logado['email'],
        #     'mensagem_pedido': mensagem
        # }

        pedidos.append(novo_pedido.converter_para_dicionario())
        salvar_dados('pedidos.json', pedidos)
        
        print("\nPedido de adoção enviado com sucesso!")
        print("Entraremos em contato em breve através do e-mail fornecido.")
        sleep(2)
        return

def pedidos_adocao():
    print("\n--- Lista de Pedidos de Adoção ---")
    pedidos = carregar_dados('pedidos.json')

    if not pedidos:
        print("Não há pedidos de adoção registrados no momento.")
        sleep(2)
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
    sleep(3)

def deletar_pedido():
    print("\n--- Deletar Pedido de Adoção ---")
    while True:
        id_deletar = input("Insira o ID da mensagem do pedido que deseja deletar (Digite VOLTAR para o menu): ").strip().lower()
        
        if id_deletar == "voltar":
            print("Operação de exclusão de pedido cancelada.")
            sleep(1)
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
            sleep(1)
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
                sleep(2)
                return
            
            elif confirmacao_exclusao == 'n':
                print("Exclusão de pedido cancelada.")
                sleep(1)
                return
            else:
                print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
                sleep(1)

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
