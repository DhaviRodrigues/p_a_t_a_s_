from time import sleep
import usercrud
import animalcrud
import artes
import editarperfil
import pedidos

def menu_user_crud():
    """Insere um menu de escolha para o usuário, contendo:
    [1] Cadastrar-se no P.A.T.A.S.
    [2] Fazer Login
    [3] Saber mais sobre o P.A.T.A.S."""
    while True:
        print('''Bem vindo ao P.A.T.A.S.''')
        print('-='*12)
        sleep(1)
        print("O que você gostaria de fazer?")
        print("[1] Cadastrar-se no P.A.T.A.S.")
        print("[2] Fazer login")
        print("[3] Saber mais sobre o P.A.T.A.S.")
        escolha = input("Digite o número correspondente a sua escolha: ").strip()
        if escolha == '1':
            usercrud.cadastrar_usuario() # Chama a funçao de cadastrar usuário
        elif escolha == '2':
            usuario_logado =  usercrud.fazer_login() # Irá atribuir um valor ao "usuario_logado", que seria o dicionário do usuario que fez login (usuario). | uc.fazer_login(), possui um retorno, o retorno de "usuario", um dicionário recebido caso o login seja bem sucedido.
            if usuario_logado is not None: # Caso o login seja bem sucedido:
                print('\n')
                sleep(1)
                print("\n")
                return usuario_logado #Entrega um dicionário com as informações do usuário logado como uma "variável" no main.py, onde será utilizado por outras funções
        elif escolha == '3':
            print(""" 

O P.A.T.A.S. é um acrônimo para Plataforma de Apoio ao Tratamento e Adoção Solidária.
                  
O P.A.T.A.S. tem como intuito auxiliar projetos voluntários que 
atuam no resgate, tratamento e adoção de animais. A proposta visa 
oferecer uma solução tecnológica acessível, funcional e organizada,
capaz de centralizar informações importantes sobre animais acolhidos, 
seu estado de saúde, sua disponibilidade para adoção e o andamento 
dos cuidados prestados.
       
                  """)
            sleep(3)
        else:
            print('\n')
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")
            print('\n')
            print('\n')
            sleep(2)

def menu_pos_login(usuario_logado): # Chama a função menupuc com o dicionário do usuário como parâmetro
    """
    Menu principal para o usuário após o login.
    Contém opções para animais em tratamento, adoção, edição de perfil, sair da conta e opções administrativas (secreta).
    """
    nome_usuario = usuario_logado.get('nome') # Pega o nome do usuário logado
    while True:
        print(f"\n--- Bem-vindo(a) ao Menu Principal, {nome_usuario}!---")
        print("O que você gostaria de fazer?")
        print("[1] Visualizar os animais em processo de tratamento")
        print("[2] Adotar um pet")
        print("[3] Editar Informações de usuário")
        print("[0] Sair da Conta")

        escolha = input("Digite o número correspondente a sua escolha: ").strip()
        print('\n')

        if escolha == '1':
            print("Você escolheu: Animais em processo de tratamento.") #Imprime a lista dos animais em tramento
            sleep(1)
            print('\n')
            animalcrud.lista_animais_tratamento()
            print("---Fim da lista de animais em tratamento---")
            input("Pressione Enter para continuar...") # Espera o usuário pressionar Enter
            continue # Continua o loop do menu
        elif escolha == '2':
            animalcrud.lista_animais_adocao() #Imprime a lista dos animais em adoção
            pedidos.enviar_pedido_adocao(usuario_logado)
            sleep(2)
        elif escolha == '3':
            print("Você escolheu: Editar Informações de usuário.")#Joga pro menus_ep()
            sleep(2)
            menu_editar_perfil(usuario_logado) # Chama a função menu_ep com o dicionário do usuário logado como parâmetro
        elif escolha == '1703': # Opção secreta para o menu administrativo
            sleep(1)
            menu_opcoes_administrativas() #imprime o menu administrativo
        elif escolha == '0':
            print("Saindo da conta. Voltando ao menu inicial.")
            break
        else:
            print("Opção inválida. Por favor, digite 0, 1, 2 ou 3.")#Tratamento de erro
            sleep(2)

def menu_info_pet():
    """O menuinfo pet significa menu informações do pet, que se refere ao [2]
    do menu de opções administrativas"""
    while True:
        print("[1]Editar informações dos animais em tratamento")
        print("[2]Editar informações dos animais disponíveis para adoção")
        print("[0] Voltar ao Menu de Opções Administrativas")  
        escolha = input("Digite o número correspondente a sua escolha: ").strip()
        if escolha == '1':
            print("Você escolheu editar informações dos animais em tratamento.")#joga pras opções de cadastrar animal ac.py
            sleep(1)
            animalcrud.lista_animais_tratamento() # Imprime a lista dos animais em tratamento
            animalcrud.editar_animal_tratamento()
        elif escolha == '2':
            print("Você escolheu editar informações dos animais disponíveis para adoção.") #Edita as informações dos animais
            sleep(2)
            animalcrud.lista_animais_adocao() # Imprime a lista dos animais disponíveis para adoção
            animalcrud.editar_animal_adocao()
        elif escolha == '0':
            print("Voltando ao menu de opções administrativas...") #Retorna ao menu opções administrativas
            break
        else:
            print("Opção inválida. Por favor, digite 0, 1, 2 ou 3.") #Tratamento de erro
            sleep(2)

def menu_opcoes_administrativas():
    """As opções administrativas não devem ser utilizadas por usuários, apenas pela
    orgazinação que está utilizando o P.A.T.A.S. como plaforma de apoio ao seu trabalho solidário.
    No menu administrativo conterá as opções de:
    [1] Cadastrar Novo Animal
    [2] Editar informações dos pets
    [3] Ver pedidos de doação
    [0] Voltar ao Menu Principal:"""
    while True:
        print("\n--- Menu de Opções Administrativas ---")
        print("[1] Cadastrar Novo Animal")
        print("[2] Editar informações dos pets")
        print("[3] Ver pedidos de doação")
        print("[0] Voltar ao Menu Principal")

        escolha = input("Digite o número correspondente a sua escolha: ").strip()
        print('\n')

        if escolha == '1':
            print("Você escolheu: Cadastrar Novo Animal.") #joga pras opções de cadastrar animal ac.py
            sleep(1)
            animalcrud.cadastrar_animal()
        elif escolha == '2':
            print("Você escolheu: Editar informações dos pets.") #Edita as informações dos animais
            sleep(2)
            menu_info_pet()
        elif escolha == '3':
            print("Você escolheu: Ver pedidos de adoação.") 
            sleep(2)
            pedidos.pedidos_adocao
        elif escolha == '0':
            print("Voltando ao menu principal...") #Retorna ao menu PUC
            sleep(1)
            break
        else:
            print("Opção inválida. Por favor, digite 0, 1, 2 ou 3.") #Tratamento de erro
            sleep(2)

def menu_editar_perfil(usuario_logado):
    while True:
        print("\n=== MENU ===")
        print("1. Ver perfil")
        print("2. Atualizar perfil")
        print("3. Excluir conta")
        print("0. Voltar ao menu principal")
        
        opcao = input("\nOpção: ")
        
        if opcao == '1':
            editarperfil.ver_perfil(usuario_logado)
        elif opcao == '2':
            editarperfil.atualizar_perfil(usuario_logado)
        elif opcao == '3':
            if editarperfil.deletar_conta(usuario_logado): #Se o usuario for deletado o menu inicial será aberto novamente.
                artes.conjunto
                menu_user_crud()
                break 
        elif opcao == '0':
            break