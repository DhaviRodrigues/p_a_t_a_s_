from usercrud import enviar_email, EMAIL_REMETENTE, SENHA_APP

EMAIL_ADMIN = EMAIL_REMETENTE

class Feedback:
    """
    Módulo de Feedback do P.A.T.A.S.
    
    Este módulo permite que os utilizadores enviem feedback sobre o sistema.
    Ele recolhe informações como nome, email e mensagem de feedback,
    e envia um email para o administrador do sistema.
    """


def solicitar_feedback():
    """
    Esta função interage com o utilizador no terminal para recolher uma mensagem de feedback.
    A função garante que o utilizador não envie uma mensagem vazia.
    """

    nome_utilizador = input("Digite o seu nome (opcional): ").strip()
    while True:
        email_utilizador = input("Digite o seu email para contacto: ").strip()
        if email_utilizador:
            if "@" in email_utilizador and "." in email_utilizador:
                break
            else:
                print("Por favor, digite um email válido.")

    # Loop para garantir que a mensagem de feedback não seja vazia
    while True:
        mensagem = input("Digite a sua mensagem de feedback: ").strip()
        if mensagem:
            return nome_utilizador, email_utilizador, mensagem
        else:
            print("Por favor, digite uma mensagem antes de enviar.")


def enviar_feedback():
    """
    Função principal do módulo. Orquestra a recolha e o envio do feedback.
    
    Ela chama a função para pedir o feedback ao utilizador e, em seguida,
    formata e envia o email para o administrador do sistema.
    """
    # 1. Recolher a informação do utilizador
    nome, email_contato, mensagem_feedback = solicitar_feedback()

    # 2. Formatar o conteúdo do email que será enviado
    assunto = f"Novo Feedback Recebido de: {nome or 'Utilizador Anónimo'}"
    
    # O corpo do email (a variável 'info')
    corpo_email = f"""
    Olá, Administrador!

    Você recebeu uma nova mensagem de feedback através do sistema P.A.T.A.S.

    --------------------------------------------------
    Nome do Utilizador: {nome or 'Não informado'}
    Email para Contato: {email_contato or 'Não informado'}
    --------------------------------------------------

    Mensagem:
    "{mensagem_feedback}"
    """

    # 3. Envia o email usando a função já existente
    try:
        enviar_email(
            destinatario=EMAIL_ADMIN,
            codigo="",  # Não aplicável neste caso
            info=corpo_email,
            assunto=assunto
        )
        print("\nObrigado! O seu feedback foi enviado com sucesso.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar enviar o seu feedback: {e}")
