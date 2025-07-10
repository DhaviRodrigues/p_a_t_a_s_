from tkinter import Button, PhotoImage, Entry
from telas import tools
from telas import tela_login
import random

def transicao_para_login(window, canvas,):
    tools.fade_out(window, canvas, lambda: tela_login.criar_tela_login(window, canvas,))

def tentar_enviar_codigo(entry_email, window):
    from .modulos import usercrud
   
    email = entry_email.get()
    resultado = usercrud.Usuario.email_existe(email)

    if resultado is True:
        codigo = random.randint(000000, 999999)
        mensagem = "Seu código para redefinição de senha é:"
        assunto = "Código de Verificação P.A.T.A.S"
        resultado_email = usercrud.enviar_email(email, str(codigo), mensagem, assunto)
        
        if resultado_email is True:
            tools.custom_messagebox(
                window,
                "Código Enviado",
                f"Um código de verificação foi enviado para {email}."
            )
        else:
            tools.custom_messagebox( window,"Erro de Envio",resultado_email)
    else:
        tools.custom_messagebox(window,"Erro",resultado)

def criar_tela_redefinir_senha_pt1(window, canvas):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenhaPt1", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenhaPt1", "button_1.png")
    )
    button_enviar = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_enviar_codigo(entry_1, window),
        relief="flat"
    )
    button_enviar.place(
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text(
        293.0,
        336.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenhaPt1", "button_2.png")
    )
    button_voltar = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_login(window, canvas),
        relief="flat"
    )
    button_voltar.place(
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text(
        440.0,
        140.0,
        anchor="nw",
        text="Redefinição de senha",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenhaPt1", "entry_1.png")
    )
    canvas.create_image(
        640.0,
        404.0,
        image=canvas.entry_image_1
    )
    entry_1 = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_1.place(
        x=293.0,
        y=375.0,
        width=694.0,
        height=56.0
    )