import json
import os
import smtplib
from email.message import EmailMessage
import random

EMAIL_REMETENTE = 'patascontato@gmail.com' # Variável global que armazena o email do remetente
SENHA_APP = 'pxys ogwp crlw foar' # Variável global que armazena a senha do email do remetente

class Usuario:
    """Classe que representa um usuário, e quais ações ele pode realizar.
    Atributos:
    - id: Identificador único do usuário.
    - nome: Nome do usuário.
    - email: Email do usuário.
    - senha: Senha do usuário.
    - icone: Ícone do usuário.
    - adm: Indica se o usuário é administrador.
    - pedido: Indica se o usuário tem um pedido de adoção pendente."""

    def __init__(self, maior_id, nome, email, senha, icone):
        """
        Inicializa um novo usuário com os dados fornecidos.
        """
        self.id = maior_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.icone = icone
        self.adm = False
        self.pedido = False

    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        """Converte a instância do usuário em um dicionário."""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "icone": self.icone,
             "adm": self.adm,
             "pedido": self.pedido
        }


    def validar_usuario(nome, email, senha, confirma_senha, icone):
        """Valida os dados fornecidos para cadastro ou edição de um usuário."""
        if not nome or not email or not senha or not confirma_senha: # Verifica se todos os campos foram preenchidos.
            return "Todos os campos devem ser preenchidos."

        if len(nome) > 40: # Verifica o limite de caracteres do nome.
            return "Nome de usuário acima do limite."

        if senha != confirma_senha: # Verifica se as senhas coincidem.
            return "As senhas não coincidem."

        if len(senha) < 8: # Verifica o comprimento mínimo da senha.
            return "A senha deve ter no mínimo 8 caracteres."

        if len(senha) > 16: # Verifica o comprimento máximo da senha.
            return "A senha não pode ter mais de 16 caracteres."

        if icone is None: # Verifica se um ícone foi selecionado.
            return "Por favor, escolha um ícone de perfil."

        email_valido = ( # Verifica se o e-mail possui um dos domínios permitidos.
            '@gmail.com' in email or
            '@hotmail.com' in email or
            '@yahoo.com' in email or
            '@outlook.com' in email or
            '@ufrpe.br' in email or
            '@ufpe.br' in email
        )
        if not email_valido: # Retorna erro se o domínio não for permitido.
            return "Formato de email inválido ou domínio não permitido."

        usuarios = carregar_dados("usuarios.json") # Carrega a lista de usuários existentes.
        for usuario_existente in usuarios: # Itera sobre os usuários.
            if usuario_existente['email'] == email.strip().lower(): # Verifica se o e-mail já está em uso.
                return "Este email já está a ser utilizado."

        return True # Retorna True se todas as validações passarem.


    def criar_usuario(nome, email, senha, icone):
        """Cria um novo usuário, gera um ID e o salva no arquivo JSON."""
        usuarios = carregar_dados("usuarios.json") # Carrega os usuários existentes.

        maior_id = -1 # Inicializa a variável para encontrar o maior ID existente.
        for u in usuarios: # Itera sobre os usuários para encontrar o maior ID.
            if u['id'] > maior_id:
                maior_id = u['id']
        novo_id = maior_id + 1 # Cria um novo ID incremental.

        novo_usuario = Usuario(novo_id, nome.title().strip(), email.strip().lower(), senha.strip(), icone) # Cria uma nova instância da classe Usuario.
        usuarios.append(novo_usuario.converter_para_dicionario()) # Adiciona o novo usuário (convertido em dicionário) à lista.

        salvar_dados("usuarios.json", usuarios) # Salva a lista atualizada no arquivo JSON.


    def fazer_login(email, senha):
        """Verifica as credenciais de e-mail e senha para realizar o login do usuário."""
        if not email or not senha: # Verifica se os campos foram preenchidos.
            return "Preencha todos os campos."

        usuarios = carregar_dados("usuarios.json") # Carrega os usuários cadastrados.

        for usuario in usuarios: # Itera sobre a lista de usuários.
            if usuario['email'] == email and usuario['senha'] == senha: # Se encontrar uma correspondência de e-mail e senha.
                print(f"--- Login bem-sucedido para {usuario['nome']} ---") # Imprime uma mensagem de sucesso no console.
                return usuario # Retorna os dados do usuário logado.
                
        return "Email ou senha incorretos." # Retorna mensagem de erro se nenhuma correspondência for encontrada.


    def salvar_alteracoes_perfil(usuario_atualizado):
        """Salva as alterações feitas no perfil de um usuário no arquivo JSON."""
        todos_usuarios = carregar_dados('usuarios.json') # Carrega todos os usuários.

        novo_arquivo_usuarios = [] # Cria uma nova lista para armazenar os usuários.
        for usuario in todos_usuarios: # Itera sobre os usuários existentes.
            if usuario['id'] != usuario_atualizado['id']: # Adiciona todos os usuários, exceto o que está sendo atualizado.
                novo_arquivo_usuarios.append(usuario)
        
        novo_arquivo_usuarios.append(usuario_atualizado) # Adiciona a versão atualizada do usuário à nova lista.
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios) # Salva a lista completamente reescrita no arquivo JSON.


    def deletar_conta(usuario_logado):
        """Exclui a conta do usuário logado do arquivo JSON."""
        arquivo_usuario = carregar_dados('usuarios.json') # Carrega todos os usuários.
        
        novo_arquivo_usuarios = [] # Cria uma nova lista para armazenar os usuários.
        for usuarios in arquivo_usuario: # Itera sobre os usuários existentes.
            if usuarios['id'] != usuario_logado['id']: # Adiciona todos os usuários, exceto o que deve ser deletado.
                novo_arquivo_usuarios.append(usuarios)
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios) # Salva a lista sem o usuário deletado.
        return True


    def alterar_status_adm(email, novo_status):
        """Encontra um usuário por email e altera seu status de administrador (adm)."""
        if not email: # Verifica se o campo de e-mail está preenchido.
            return "O campo de email não pode estar vazio."

        usuarios = carregar_dados("usuarios.json") # Carrega todos os usuários.
        
        usuario_encontrado = False # Flag para verificar se o usuário foi encontrado.
        for usuario in usuarios: # Itera sobre os usuários.
            if usuario['email'] == email.strip().lower(): # Se encontrar o e-mail correspondente.
                usuario['adm'] = novo_status # Altera o status de administrador.
                usuario_encontrado = True
                break # Interrompe o loop, pois o usuário já foi encontrado.

        if not usuario_encontrado: # Se o loop terminar e o usuário não for encontrado.
            return f"Nenhum usuário encontrado com o email: {email}"

        salvar_dados("usuarios.json", usuarios) # Salva a lista de usuários com a alteração.
        
        if novo_status is True: # Retorna uma mensagem de sucesso apropriada.
            return f"O usuário {email} foi promovido a administrador com sucesso."
        else:
            return f"O usuário {email} foi removido de administrador com sucesso."
    

    def email_existe(email):
        """Verifica se um email já está cadastrado no sistema e retorna os dados do usuário se existir."""
        usuarios = carregar_dados("usuarios.json") # Carrega todos os usuários.
        for usuario in usuarios: # Itera sobre os usuários.
            if usuario.get('email') == email.strip().lower(): # Se encontrar o e-mail.
                return usuario # Retorna o dicionário completo do usuário.

        return False # Retorna False se o e-mail não for encontrado.


    def enviar_email(destinatario, codigo, info, assunto):
        """Envia um email com um código de verificação para o destinatário especificado."""
        msg = EmailMessage() # Cria um objeto de mensagem de e-mail.
        msg["Subject"] = assunto # Define o assunto do e-mail.
        msg["From"] = EMAIL_REMETENTE # Define o remetente.
        msg["To"] = destinatario # Define o destinatário.
        msg.set_content(f"{info} {codigo}") # Define o corpo do e-mail.

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: # Inicia uma conexão segura com o servidor SMTP do Gmail.
                smtp.login(EMAIL_REMETENTE, SENHA_APP) # Faz login na conta de e-mail do remetente.
                smtp.send_message(msg) # Envia a mensagem.
            print(" Código de verificação enviado para o seu email!") # Confirmação no console.
        except Exception as e:
            print(" Erro ao enviar email:", e) # Mensagem de erro no console em caso de falha.


    def gerar_codigo(email):
        """Gera um código numérico aleatório de 6 dígitos e o envia por e-mail."""
        codigo = random.randint(000000, 999999) # Gera um número aleatório entre 0 e 999999.
        mensagem = "Código para redefinição de senha:" # Define a mensagem do corpo do e-mail.
        assunto = "Código de Verificação P.A.T.A.S - Redefinição de Senha" # Define o assunto do e-mail.
        Usuario.enviar_email(email, str(codigo), mensagem, assunto) # Chama a função para enviar o e-mail.
        return str(codigo) # Retorna o código gerado como uma string.


    def recuperar_senha(usuario, nova_senha):
        """Atualiza a senha de um usuário específico no arquivo JSON."""
        arquivo_usuarios = carregar_dados('usuarios.json') # Carrega todos os usuários.
        email = usuario.get("email") # Obtém o e-mail do usuário a ser atualizado.
        for usuarios in arquivo_usuarios: # Itera sobre os usuários.
            if usuarios['email'] == email: # Encontra o usuário correspondente.
                usuarios['senha'] = nova_senha # Define a nova senha.
                break # Interrompe o loop.
        
        salvar_dados('usuarios.json', arquivo_usuarios) # Salva a lista de usuários atualizada.
        return True


def carregar_dados(arquivo):
    """Carrega dados de um arquivo JSON especificado."""
    try:
        with open(arquivo, 'r') as f: # Tenta abrir o arquivo em modo de leitura ('r').
            dados = json.load(f) # Carrega o conteúdo JSON do arquivo.
            return dados # Retorna os dados carregados.
    except FileNotFoundError: # Se o arquivo não existir.
        return [] # Retorna uma lista vazia para evitar erros.

def salvar_dados(arquivo, dados):
    """Salva uma lista de dicionários em um arquivo JSON com formatação."""
    with open(arquivo, 'w') as f: # Abre o arquivo em modo de escrita ('w'), sobrescrevendo o conteúdo.
        json.dump(dados, f, indent=4) # Escreve os dados no arquivo JSON com uma indentação de 4 espaços para legibilidade.