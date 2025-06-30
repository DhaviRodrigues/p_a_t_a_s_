import json
import os
from time import sleep

class Usuario:
    """Classe que representa um usuário"""
    def __init__(self, maior_id, nome, email, senha, icone):
        self.id = maior_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.icone = icone
    
    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "icone": self.icone
        }

def cadastrar_usuario(nome, email, senha, confirma_senha, icone):
    if not nome or not email or not senha or not confirma_senha:
        return "Todos os campos devem ser preenchidos."

    if senha != confirma_senha:
        return "As senhas não coincidem."
        
    if len(senha) < 8:
        return "A senha deve ter no mínimo 8 caracteres."

    if len(senha) > 16:
        return "A senha não pode ter mais de 16 caracteres."

    if icone is None:
        return "Por favor, escolha um ícone de perfil."
    
    email_valido = (
        '@gmail.com' in email or
        '@hotmail.com' in email or
        '@yahoo.com' in email or
        '@outlook.com' in email or
        '@ufrpe.br' in email or
        '@ufpe.br' in email
    )
    if not email_valido:
        return "Formato de email inválido ou domínio não permitido."
        
    usuarios = carregar_dados("usuarios.json")
    for usuario_existente in usuarios:
        if usuario_existente['email'] == email.strip().lower():
            return "Este email já está a ser utilizado."

    maior_id = -1
    for u in usuarios:
        if u['id'] > maior_id:
            maior_id = u['id']
    novo_id = maior_id + 1
    
    novo_usuario = Usuario(novo_id, nome.title().strip(), email.strip().lower(), senha.strip(), icone)
    
    usuarios.append(novo_usuario.converter_para_dicionario())
    salvar_dados("usuarios.json", usuarios)
        
    return True

def fazer_login():
    """Comando para fazer login do usuário.
    Informações requisitadas:
    email:
    senha:
    
    As informações devem estar presentes no id de algum usuário do "Usuários.json" """

def fazer_login(email, senha):
    if not email or not senha:
        return "Preencha todos os campos."

    usuarios = carregar_dados("usuarios.json")

    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"--- Login bem-sucedido para {usuario['nome']} ---")
            return usuario
            
    return "Email ou senha incorretos."

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
