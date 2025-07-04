from tkinter import Button, PhotoImage, Entry
from telas import tela_inicial
from telas import tela_menu_principal
from telas import tela_menu_adm
from telas import tools
from modulos import usercrud

def transicao_para_inicial(window, canvas):
    tools.fade_out(
        window,
        canvas,
        lambda: tela_inicial.criar_tela_inicial(window, canvas)
    )

def tentar_login(window, canvas, email_entry, senha_entry):
    email = email_entry.get()
    senha = senha_entry.get()

    resultado = usercrud.Usuario.fazer_login(email, senha)

    if isinstance(resultado, dict):
        if resultado.get("adm") is True:
            tools.fade_out(
                window,
                canvas,
                lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, resultado)
            )
        else:
            tools.fade_out(
                window,
                canvas,
                lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, resultado)
            )
    else:
        tools.custom_messagebox(
            window,
            "Erro de Login",
            resultado
        )

def criar_tela_login(window, canvas):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )
    
    entry_email = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_email.place(
        x=293.0,
        y=308.0,
        width=694.0,
        height=56.0
    )

    entry_senha = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )
    entry_senha.place(
        x=293.0,
        y=420.0,
        width=694.0,
        height=56.0
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_login(
            window,
            canvas,
            entry_email,
            entry_senha
        ),
        relief="flat"
    )
    button_1.place(
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text(
        293.0,
        269.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        293.0,
        381.0,
        anchor="nw",
        text="Senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place(
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text(
        403.0,
        202.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "entry_1.png")
    )
    canvas.create_image(
        640.0,
        337.0,
        image=canvas.entry_image_1
    )

    canvas.entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "entry_2.png")
    )
    canvas.create_image(
        640.0,
        449.0,
        image=canvas.entry_image_2
    )

    canvas.button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaLogin", "button_3.png")
    )
    button_3 = Button(
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Esqueceu a senha? clicado"),
        relief="flat"
    )
    button_3.place(
        x=463.0,
        y=592.0,
        width=343.0,
        height=43.0
    )