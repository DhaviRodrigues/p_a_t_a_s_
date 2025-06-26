import json
import os
from time import sleep

class Usuario:
    """Classe que representa um usuário"""
    def __init__(self, maior_id, nome, email, senha):
        self.id = maior_id
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }

def cadastrar_usuario():
    """Cadastra um novo usuário a partir dos dados:
    Nome:
    Email:
    Senha:"""
    
    print("--- Cadastro de Usuário ---")
    usuarios = carregar_dados('usuarios.json')
    #Esse é o primeiro momento em que o arquivo .json é criado, no caso ele irá carregar um dicionários dentro de uma lista "usuarios.json", e caso não exista ele criará.

#Cadastra o nome do usuário
    while True:
        nome = input(str("Digite seu nome e sobrenome: ")).strip() #Remove espaços no início e final do texto
        if nome == '': ##Verifica se o nome está vazio
            print('Nome não pode estar vazio. Tente novamente.') 
        elif nome.replace(' ', '').isalpha() == False:  #Verifica se o nome possui apenas letras
            print('Nome deve conter apenas letras. Tente novamente.')
        else:
            break
#Cadastra o Email do usuário
    while True:
        email = input("Digite seu e-mail: ").strip().lower() #Remove espaços no início e final do texto e deixa o email inteiro em minúsculo
        
        email_existe = False
        for usuario_existente in usuarios: #Verifica se o email já está cadastrado
            if usuario_existente['email'] == email: #Procura o email no "usuario.json"
                email_existe = True #Caso encontre retorna o valor True nessa variável
                break
        if email_existe: #Caso seja verdade, impedirá a sequência do cadastro
            print('\n')
            print("-- O email já está cadastrado, peço que tente executar o login.--")
            print('\n')
            return #Encerra a função de cadastrar usuário
        
        if not ('@gmail.com' in email or \
                '@hotmail.com' in email or \
                '@yahoo.com' in email or \
                '@outlook.com' in email or \
                '@ufrpe.br' in email or \
                'ufpe' in email): # os parenteses servem para agrupar as condições ou seja, ela será avaliada como um bloco e será "True" caso não haja gmail, por exemplo, no email inserido pelo usuário
                                # caso não fossem agrupadas, nenhum email seria permitido, já que, caso o usuário digitasse @gmail.com seria negado por não ter o @hotmail.com obrigado o usuário a adicionar todos os emails para ser considerado válido
            print("Formato de e-mail inválido ou domínio não permitido.")
            continue 
        else:
            break 
#Cadastra a senha
    while True:
        senha = input("Digite sua senha (mínimo 8 caracteres): ").strip()
        if len(senha) < 8:
            print("A senha deve ter no mínimo 8 caracteres.")
            continue 
        confirmar_senha = input("Confirme sua senha: ").strip()
        if senha != confirmar_senha:
            print("As senhas não coincidem. Por favor, tente novamente.")
            continue 
        else:
            break 

#Cadastra o id do usuário
    maior_id = -1 # Começa com -1 para garantir que o primeiro ID seja 0 se a lista estiver vazia
    for id in usuarios: # Percorre a lista para encontrar o maior ID
        if id['id'] > maior_id:
            maior_id = id['id'] # Quando um maior id da lista de usuários é encontrado atribuido a "id"
    id=maior_id + 1 # Soma id +1 para evitar conflitos entre id iguais
#Cria uma lista com as informações do usuário

    novo_usuario = Usuario(maior_id, nome, email, senha)

#----------------------------------------#    
    # novo_usuario = {
    #     'id': id,
    #     'nome': nome,
    #     'email': email,
    #     'senha': senha
    # }
#-----------------------------------------#
    
#Adiciona o usuário que foi cadastrado no "usuários json."
    usuarios.append(novo_usuario.converter_para_dicionario())
    salvar_dados('usuarios.json', usuarios) # Salva a lista atualizada
    print("\n")
    print("--- Usuário cadastrado com sucesso! ---")
    print('\n')
    print("Agora que você já possui uma conta, tente fazer o login")
    sleep(1)
    print('\n')

def fazer_login():
    """Comando para fazer login do usuário.
    Informações requisitadas:
    email:
    senha:
    
    As informações devem estar presentes no id de algum usuário do "Usuários.json" """

    print("--- Login de Usuário ---")
    #Carrega os dados dos usuários presentes no "usuários.json" para validar as informações.
    usuarios = carregar_dados('usuarios.json')

    email_digitado = input("Digite seu e-mail: ")
    senha_digitada = input("Digite sua senha: ")

#Verifica se o email digitado e a senha correspondem a algum usuário existente
    for usuario in usuarios:
        if usuario['email'] == email_digitado and usuario['senha'] == senha_digitada:
            print(f"---Login bem-sucedido---")
            return usuario # Retorna o dicionário do usuário que as informações correspondem
        print('\n')
    print("E-mail ou senha incorretos.")
    print('\n')
    sleep(1)
    return None # Retorna nada se o login falhar

def carregar_dados(arquivo):
    """Carrega o arquivo json dos usuários"""
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
    """Salva as informações no arquivo json dos usuários"""
    with open(arquivo, 'w') as arquivo:
        #Abre o arquivo json em modo 'w'(write)
        json.dump(dados, arquivo, indent=4)
        #json é a biblioteca importada,   .dump() é a função que vai jogar da primeira variável, dentro do "arquivo" de usuarios.json, indent=4 é apenas para deixar mais organizado na hora da escrita do arquivo
