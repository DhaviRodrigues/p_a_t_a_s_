from .usercrud import enviar_email, EMAIL_REMETENTE, SENHA_APP

EMAIL_ADMIN = EMAIL_REMETENTE

class Feedback:
    """
    Módulo de Feedback do P.A.T.A.S.
    
    Este módulo permite que os utilizadores enviem feedback sobre o sistema.
    Ele recolhe informações como nome, email e mensagem de feedback,
    e envia um email para o administrador do sistema.
    """



def enviar_feedback(entry_assunto,entry_mensagem,usuario_logado):
    """
    Função principal do módulo. Orquestra a recolha e o envio do feedback.
    
    Ela chama a função para pedir o feedback ao utilizador e, em seguida,
    formata e envia o email para o administrador do sistema.
    """
    # 1. Recolher a informação do utilizador

    assunto=entry_assunto
    mensagem_feedback=entry_mensagem
    nome = usuario_logado.get("nome")
    email_contato=usuario_logado.get("email")

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
