from collections import Counter
import json
import os
import smtplib
from email.message import EmailMessage
import random

EMAIL_REMETENTE = 'patascontato@gmail.com' # Variável global que armazena o email do remetente
SENHA_APP = 'pxys ogwp crlw foar' # Variável global que armazena a senha do email do remetente

class Usuario:
    """Classe que representa um usuário"""
    def __init__(self, maior_id, nome, email, senha, icone):
        self.id = maior_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.icone = icone
        self.adm = False
        self.pedido = False

    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
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
        # Verifica se todos os campos foram preenchidos.
        if not nome or not email or not senha or not confirma_senha:
            return "Todos os campos devem ser preenchidos."

        # Verifica o comprimento do nome de usuário.
        if len(nome) > 40:
            return "Nome de usuário acima do limite."

        # Verifica se as senhas coincidem.
        if senha != confirma_senha:
            return "As senhas não coincidem."

        # Verifica o comprimento mínimo e máximo da senha.
        if len(senha) < 8:
            return "A senha deve ter no mínimo 8 caracteres."

        if len(senha) > 16:
            return "A senha não pode ter mais de 16 caracteres."

        # Verifica se um ícone de perfil foi escolhido.
        if icone is None:
            return "Por favor, escolha um ícone de perfil."

        # Valida o formato do e-mail.
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

        # Verifica se o e-mail já está em uso.
        usuarios = carregar_dados("usuarios.json")
        for usuario_existente in usuarios:
            if usuario_existente['email'] == email.strip().lower():
                return "Este email já está a ser utilizado."

        return True


    # Cria um novo usuário.
    def criar_usuario(nome, email, senha, icone):
        usuarios = carregar_dados("usuarios.json")

        # Gera um novo ID para o usuário.
        maior_id = -1
        for u in usuarios:
            if u['id'] > maior_id:
                maior_id = u['id']
        novo_id = maior_id + 1

        # Cria uma nova instância de Usuario e a adiciona à lista de usuários.
        novo_usuario = Usuario(novo_id, nome.title().strip(), email.strip().lower(), senha.strip(), icone)
        usuarios.append(novo_usuario.converter_para_dicionario())

        # Salva os dados atualizados no arquivo JSON.
        salvar_dados("usuarios.json", usuarios)


    # Realiza o login do usuário.
    def fazer_login(email, senha):
        """Comando para fazer login do usuário."""
        # Verifica se os campos de e-mail e senha foram preenchidos.
        if not email or not senha:
            return "Preencha todos os campos."

        usuarios = carregar_dados("usuarios.json")

        # Verifica as credenciais do usuário.
        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                print(f"--- Login bem-sucedido para {usuario['nome']} ---")
                return usuario
                
        return "Email ou senha incorretos."


    # Salva as alterações no perfil do usuário.
    def salvar_alteracoes_perfil(usuario_atualizado):
        todos_usuarios = carregar_dados('usuarios.json')

        # Cria uma nova lista de usuários, substituindo os dados do usuário atualizado.
        novo_arquivo_usuarios = []
        for usuario in todos_usuarios:
            if usuario['id'] != usuario_atualizado['id']:
                novo_arquivo_usuarios.append(usuario)
        
        novo_arquivo_usuarios.append(usuario_atualizado)
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios)


    # Deleta a conta do usuário.
    def deletar_conta(usuario_logado):
        """Exclui a conta do usuário do arquivo JSON."""
        arquivo_usuario = carregar_dados('usuarios.json')
        
        # Cria uma nova lista de usuários, excluindo o usuário logado.
        novo_arquivo_usuarios = []
        for usuarios in arquivo_usuario:
            if usuarios['id'] != usuario_logado['id']:
                novo_arquivo_usuarios.append(usuarios) 
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios) 
        return True


    # Altera o status de administrador de um usuário.
    def alterar_status_adm(email, novo_status):
        """Encontra um usuário por email e altera seu status de administrador."""
        if not email:
            return "O campo de email não pode estar vazio."

        usuarios = carregar_dados("usuarios.json")
        
        # Encontra o usuário pelo e-mail e atualiza seu status de administrador.
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario['email'] == email.strip().lower():
                usuario['adm'] = novo_status
                usuario_encontrado = True
                break

        if not usuario_encontrado:
            return f"Nenhum usuário encontrado com o email: {email}"

        salvar_dados("usuarios.json", usuarios)
        
        if novo_status is True:
            return f"O usuário {email} foi promovido a administrador com sucesso."
        else:
            return f"O usuário {email} foi removido de administrador com sucesso."
    

    # Verifica se um e-mail já está cadastrado.
    def email_existe(email):
        """Verifica se um email já está cadastrado no sistema."""
        usuarios = carregar_dados("usuarios.json")
        for usuario in usuarios:
            if usuario.get('email') == email.strip().lower():
                return usuario

        return False


    def enviar_email(destinatario, codigo, info, assunto):
        """
        Envia um email com um código de verificação para o destinatário especificado.

        Parâmetros:
        destinatario (str): Endereço de email do destinatário.
        codigo (str): Código aleatório de verificação que será enviado.
        info (str): Mensagem explicativa sobre para que é o código.
        assunto (str): Assunto do email.

        Funciona usando o servidor SMTP do Gmail com conexão SSL.
        Requer as constantes EMAIL_REMETENTE e SENHA_APP que são variaváveis globais.

        retorno:
        Em caso de sucesso, exibe uma mensagem de confirmação no terminal.
        Em caso de erro, exibe uma mensagem de erro com o motivo.
        """
        
        msg = EmailMessage() # define o objeto msg com a clase EmailMessage
        msg["Subject"] = assunto
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = destinatario
        msg.set_content(f"{info} {codigo}")

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: #Essa é uma classe da biblioteca smtplib que permite enviar e-mails usando o protocolo SMTP com SSL direto na conexão.
                smtp.login(EMAIL_REMETENTE, SENHA_APP)
                smtp.send_message(msg)
            print(" Código de verificação enviado para o seu email!")
        except Exception as e:
            print(" Erro ao enviar email:", e)

    def gerar_codigo(email):
        """
        Gera um código de 6 dígitos garantindo que nenhum número se repita mais de 3 vezes.
        """
        while True:
            codigo_provisorio = str(random.randint(100000, 999999))# Gera um número candidato entre 100000 e 999999 e o converte para string
            verificao_codigo = Counter(codigo_provisorio)# Conta a ocorrência de cada dígito no número gerado
            
            # Verifica se algum dígito apareceu mais de 3 vezes.
            # A função any() retorna True se qualquer valor na sequência for True.
            # Se nenhum dígito se repetiu mais de 3 vezes, a condição é falsa e o 'if not' é executado.
            if not any(count > 3 for count in verificao_codigo.values()):
                codigo_final = codigo_provisorio
                break

        mensagem = "Código para Confirmação de identidade:"
        assunto = "Código de Verificação P.A.T.A.S"
        Usuario.enviar_email(email, str(codigo_final), mensagem, assunto)
        return codigo_final

    def recuperar_senha(usuario, nova_senha):
        """
        Permite ao utilizador redefinir a sua senha através de verificação por e-mail.
        """
        arquivo_usuarios = carregar_dados('usuarios.json') 
        email = usuario.get("email")
        for usuarios in arquivo_usuarios:
            if usuarios['email'] == email:
                usuarios['senha'] = nova_senha
                break
        
        salvar_dados('usuarios.json', arquivo_usuarios)
        return True

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


