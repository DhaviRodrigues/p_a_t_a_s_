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
        if not nome or not email or not senha or not confirma_senha:
            return "Todos os campos devem ser preenchidos."

        if len(nome) > 40:
            return "Nome de usuário acima do limite."

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

        return True

    def criar_usuario(nome, email, senha, icone):
        usuarios = carregar_dados("usuarios.json")

        maior_id = -1
        for u in usuarios:
            if u['id'] > maior_id:
                maior_id = u['id']
        novo_id = maior_id + 1

        novo_usuario = Usuario(novo_id, nome.title().strip(), email.strip().lower(), senha.strip(), icone)
        usuarios.append(novo_usuario.converter_para_dicionario())

        salvar_dados("usuarios.json", usuarios)


    def fazer_login(email, senha):
        """Comando para fazer login do usuário.
        Informações requisitadas:
        email:
        senha:
        
        As informações devem estar presentes no id de algum usuário do "Usuários.json" 
        """
        if not email or not senha:
            return "Preencha todos os campos."

        usuarios = carregar_dados("usuarios.json")

        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                print(f"--- Login bem-sucedido para {usuario['nome']} ---")
                return usuario
                
        return "Email ou senha incorretos."


    def salvar_alteracoes_perfil(usuario_atualizado):
        todos_usuarios = carregar_dados('usuarios.json')

        novo_arquivo_usuarios = []
        for usuario in todos_usuarios:
            if usuario['id'] != usuario_atualizado['id']:
                novo_arquivo_usuarios.append(usuario)
        
        novo_arquivo_usuarios.append(usuario_atualizado)
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios)

    def deletar_conta(usuario_logado):
        """
        Exclui a conta do usuário do arquivo JSON.
        """
        arquivo_usuario = carregar_dados('usuarios.json')
        
        novo_arquivo_usuarios = []
        for usuarios in arquivo_usuario:
            if usuarios['id'] != usuario_logado['id']:#Exclui o usuario da lista
                novo_arquivo_usuarios.append(usuarios) #Cria uma lista sem o usario logado
        
        salvar_dados('usuarios.json', novo_arquivo_usuarios) #Salva os dados
        return True

    def alterar_status_adm(email, novo_status):
        """Encontra um usuário por email e altera seu status de administrador."""
        if not email:
            return "O campo de email não pode estar vazio."

        usuarios = carregar_dados("usuarios.json")
        
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
    
    def email_existe(email):
        """Verifica se um email já está cadastrado no sistema."""

        if not email:
            return "O campo de email não pode estar vazio."
            
        usuarios = carregar_dados("usuarios.json")
        for usuario in usuarios:
            if usuario.get('email') == email.strip().lower():
                return True

        return "O email não está cadastrado."

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


    def recuperar_senha():
        """
        Permite ao utilizador redefinir a sua senha através de verificação por e-mail.
        """
        usuarios = carregar_dados('usuarios.json') 
        print("\n=== Redefinir Senha ===")
        
        email = ""
        while True:
            email = input("Digite seu e-mail: ").strip().lower()
            
            email_existe = False
            for usuario_existente in usuarios:
                if usuario_existente['email'] == email:
                    email_existe = True
                    break
            
            if email_existe:
                break 
            else:
                print('\n-- O email não está cadastrado, se dirija para a área de cadastro ou digite outro email.--\n')
                continuar = input("Deseja tentar com outro email? (s/n): ").lower()
                if continuar != 's' or continuar != 'sim':
                    return

        # Envia código de verificação
        codigo = random.randint(100000, 999999)
        mensagem = "Código para redefinição de senha:"
        assunto = "Código de Verificação P.A.T.A.S - Redefinição de Senha"
        Usuario.enviar_email(email, str(codigo), mensagem, assunto)

        for tentativa in range(3):
            codigo_digitado = input("Digite o código enviado ao seu email: ").strip()
            if codigo_digitado == str(codigo):
                print(" Código correto.")
                print('\n--- Atualizar Senha ---')
                
                nova_senha = ""
                while True:
                    nova_senha = input("Digite a nova senha (mínimo 8 caracteres): ").strip()
                    
                    if len(nova_senha) < 8:
                        print('A senha deve ter no mínimo 8 caracteres.')
                        continue
                    
                    confirmar_nova_senha = input("Confirme a nova senha: ").strip()
                    if nova_senha != confirmar_nova_senha:
                        print('As senhas não coincidem. Por favor, tente novamente.')
                        continue
                    
                    # 2. Encontrar o utilizador e atualizar sua senha
                    for usuario in usuarios:
                        if usuario['email'] == email:
                            usuario['senha'] = nova_senha
                            break # Encontrou e atualizou, pode parar de procurar
                    
                    # 3. Salvar as alterações no ficheiro JSON
                    salvar_dados('usuarios.json', usuarios)
                    
                    print("\nSenha redefinida com sucesso!")
                    return # Encerra a função após redefinir a senha
            else:
                tentativas_restantes = 2 - tentativa
                if tentativas_restantes > 0:
                    print(f" Código incorreto. Você tem mais {tentativas_restantes} tentativa(s).")
                else:
                    print("Código incorreto.")
                
        print("\nNúmero máximo de tentativas excedido. A operação foi cancelada.")

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


