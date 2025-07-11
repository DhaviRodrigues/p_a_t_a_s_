from tkinter import Button, PhotoImage, Entry
from telas import tools

def transicao_para_tela_inicial(window, canvas):
    from telas import tela_inicial
    tools.fade_out(window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas, None))

def transicao_para_login(window, canvas):
    from telas import tela_login
    
    callback_function = lambda: tela_login.criar_tela_login(window, canvas)
    tools.fade_out(
        window,
        canvas,
        callback_function
    )

def tentar_verificar_codigo(window, codigo, entry_codigo, pre_usuario, canvas):
    from .modulos import usercrud
    from telas import tela_login

    nome = pre_usuario["nome"]
    email = pre_usuario["email"]
    senha = pre_usuario["senha"]
    user_icon = pre_usuario["icone"]

    if codigo == entry_codigo:
        if not pre_usuario == {}:
            usercrud.Usuario.criar_usuario(nome, email, senha, user_icon)
            tools.custom_messagebox(window, "Cadastro Bem-Sucedido", "Cadastro realizado com sucesso! Você será redirecionado para a tela de login.")
            tools.fade_out(window,canvas,lambda: tela_login.criar_tela_login(window, canvas,))

    else:    
        tools.custom_messagebox(window, "Erro no cadastro", "O código está incorreto, verifique novamente")

def criar_tela_inserir_codigo(window, canvas, pre_usuario, codigo):
    print (f'{codigo}')
    print(f'{pre_usuario}')
    tools.limpar_tela(canvas)
    canvas.configure(
        bg="#FFFFFF"
    )

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaInserirCodigo", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaInserirCodigo", "button_1.png")
    )
    entry_codigo = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_codigo.place(
        x=293.0,
        y=375.0,
        width=694.0,
        height=56.0
    )
    
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_verificar_codigo(),
        relief="flat"
    )
    button_1.place(
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaInserirCodigo", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_tela_inicial(window, canvas),
        relief="flat"
    )
    button_2.place(
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaInserirCodigo", "entry_1.png")
    )
    canvas.create_image(
        640.0,
        404.0,
        image=canvas.entry_image_1
    )