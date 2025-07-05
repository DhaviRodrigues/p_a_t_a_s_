from tkinter import Button, Canvas, Entry, PhotoImage, Text
from telas import tools

def transicao_para_menu(window, canvas, usuario_logado):
    """
    Inicia a transição de volta para a tela do menu principal.
    """
    from telas import tela_menu_principal
    callback_function = lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado)
    
    tools.fade_out(
        window,
        canvas,
        callback_function
    )

def criar_tela_feedback(window, canvas, usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_bg = PhotoImage(
        file=tools.relative_to_assets("TelaFeedback", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_bg
    )

    canvas.button_voltar = PhotoImage(
        file=tools.relative_to_assets("TelaFeedback", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_voltar,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place(
        x=1123.0,
        y=19.0,
        width=135.0,
        height=129.0
    )

    canvas.button_enviar = PhotoImage(
        file=tools.relative_to_assets("TelaFeedback", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_enviar,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Botão 'Enviar' clicado."),
        relief="flat"
    )
    button_2.place(
        x=1101.49,
        y=586.35,
        width=164.55,
        height=98.41
    )
    
    canvas.create_text(
        100.0,
        190.0,
        anchor="nw",
        text="Assunto:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    canvas.create_text(
        460.0,
        266.0,
        anchor="nw",
        text="Mensagem:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    canvas.create_text(
        334.0,
        81.0,
        anchor="nw",
        text="ENVIE SUA MENSAGEM",
        fill="#44302C",
        font=("Poppins Black", 40 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaFeedback", "entry_1.png")
    )
    canvas.create_image(
        570.0,
        487.0,
        image=canvas.entry_image_1
    )
    entry_mensagem = Text(
        canvas,
        bd=0,
        bg="#EED3B2",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 16),
        wrap="word"
    )
    entry_mensagem.place(
        x=117.0,
        y=333.0,
        width=906.0,
        height=306.0
    )

    canvas.entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaFeedback", "entry_2.png")
    )
    canvas.create_image(
        652.5,
        216.5,
        image=canvas.entry_image_2
    )
    entry_assunto = Entry(
        canvas,
        bd=0,
        bg="#EED3B2",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_assunto.place(
        x=278.0,
        y=193.0,
        width=749.0,
        height=45.0
    )