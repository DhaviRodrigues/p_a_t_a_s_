from tkinter import Button, Canvas, Entry, PhotoImage, Text
from telas import tools

def transicao_para_menu(window, canvas, usuario_logado):
    """Inicia a transição de volta para a tela do menu principal."""
    from telas import tela_menu_principal
    tools.fade_out(window, canvas, lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar.


def tentar_enviar_feedback(entry_assunto, entry_mensagem, usuario_logado, window):
    """
    Valida e envia a mensagem de feedback do usuário.
    Verifica se os campos de assunto e mensagem não estão vazios antes de enviar.
    """
    from .modulos import feedback

    assunto = entry_assunto.get() # Obtém o texto do campo de assunto.
    mensagem = entry_mensagem.get("1.0", "end-1c") # Obtém o texto do campo de mensagem.

    if not assunto: # Verifica se o campo de assunto está vazio.
         tools.custom_messagebox(window, "Erro de envio", "Você precisa preencher o assunto.") # Exibe mensagem de erro.
    elif not mensagem: # Verifica se o campo de mensagem está vazio.
         tools.custom_messagebox(window, "Erro de envio", "Você precisa escrever alguma mensagem.") # Exibe mensagem de erro.
    else: # Se ambos os campos estiverem preenchidos.
        feedback.Feedback.enviar_feedback(entry_assunto,entry_mensagem,usuario_logado) # Chama a função para enviar o feedback.
        tools.custom_messagebox(window, "Envio bem-sucedido", "O email foi enviado, responderemos assim que possível.") # Exibe mensagem de sucesso.

        entry_assunto.delete(0, "end") # Limpa o campo de assunto.
        entry_mensagem.delete("1.0", "end") # Limpa o campo de mensagem.


def criar_tela_feedback(window, canvas, usuario_logado):
    """Cria a interface gráfica da tela de feedback, permitindo ao usuário enviar uma mensagem."""
    from .modulos import feedback

    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo do canvas.

    canvas.image_bg = PhotoImage( # Carrega a imagem de fundo.
        file=tools.relative_to_assets("TelaFeedback", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        360.0,
        image=canvas.image_bg
    )

    canvas.button_voltar = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaFeedback", "button_1.png")
    )
    button_1 = Button( # Botão para voltar ao menu principal.
        canvas,
        image=canvas.button_voltar,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar".
        x=1123.0,
        y=19.0,
        width=135.0,
        height=129.0
    )

    canvas.button_enviar = PhotoImage( # Carrega a imagem do botão "Enviar".
        file=tools.relative_to_assets("TelaFeedback", "button_2.png")
    )
    button_2 = Button( # Botão para enviar o feedback.
        canvas,
        image=canvas.button_enviar,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_enviar_feedback(entry_assunto, entry_mensagem, usuario_logado, window),
        relief="flat"
    )
    button_2.place( # Posiciona o botão "Enviar".
        x=1101.49,
        y=586.35,
        width=164.55,
        height=98.41
    )
    
    canvas.create_text( # Texto "Assunto:".
        100.0,
        190.0,
        anchor="nw",
        text="Assunto:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    canvas.create_text( # Texto "Mensagem:".
        460.0,
        266.0,
        anchor="nw",
        text="Mensagem:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    canvas.create_text( # Título da tela.
        334.0,
        81.0,
        anchor="nw",
        text="ENVIE SUA MENSAGEM",
        fill="#44302C",
        font=("Poppins Black", 40 * -1)
    )

    canvas.entry_image_1 = PhotoImage( # Carrega a imagem de fundo do campo de mensagem.
        file=tools.relative_to_assets("TelaFeedback", "entry_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo do campo de mensagem.
        570.0,
        487.0,
        image=canvas.entry_image_1
    )
    entry_mensagem = Text( # Campo de texto para a mensagem.
        canvas,
        bd=0,
        bg="#EED3B2",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 16),
        wrap="word" # Permite a quebra de linha automática por palavra.
    )
    entry_mensagem.place( # Posiciona o campo de mensagem.
        x=117.0,
        y=333.0,
        width=906.0,
        height=306.0
    )

    canvas.entry_image_2 = PhotoImage( # Carrega a imagem de fundo do campo de assunto.
        file=tools.relative_to_assets("TelaFeedback", "entry_2.png")
    )
    canvas.create_image( # Exibe a imagem de fundo do campo de assunto.
        652.5,
        216.5,
        image=canvas.entry_image_2
    )
    entry_assunto = Entry( # Campo de entrada para o assunto.
        canvas,
        bd=0,
        bg="#EED3B2",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_assunto.place( # Posiciona o campo de assunto.
        x=278.0,
        y=193.0,
        width=749.0,
        height=45.0
    )