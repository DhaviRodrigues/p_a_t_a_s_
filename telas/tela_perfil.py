from tkinter import Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_menu(window, canvas, usuario_logado):
    from telas import tela_menu_principal

    tools.fade_out(
        window,
        canvas,
        lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado)
    )

def transicao_para_logout(window, canvas):
    from telas import tela_inicial

    tools.fade_out(
        window, 
        canvas, 
        lambda: tela_inicial.criar_tela_inicial(window, canvas))


def verificar_pedido_adocao(window,canvas, usuario_logado):
    from .modulos import pedidos
    from telas import tela_pedido_usuario

    if usuario_logado.get("pedido") == False:
        tools.custom_messagebox(window, "Erro na visualização do pedido", "Você ainda não possui um pedido de adoção ativo.")

    else:
        tools.fade_out(window, canvas, lambda: tela_pedido_usuario.criar_tela_pedido_usuario(window, canvas, usuario_logado,))


def criar_tela_perfil(window, canvas, usuario_logado,):
    from telas import tela_editar_perfil
    from .modulos import usercrud
    from telas import tela_pedido_usuario

    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "image_1.png")
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )

    canvas.create_text(
        521.8,
        156.2,
        anchor="nw",
        text="Nome:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )
    
    nome_usuario = usuario_logado.get("nome", "")
    if len(nome_usuario) > 28:
        nome_perfil = nome_usuario[:28] + "..."
    else:
        nome_perfil = nome_usuario

    canvas.create_text(
        630.0,
        156.2,
        anchor="nw",
        text=nome_perfil,
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.create_text(
        521.8,
        231.2,
        anchor="nw",
        text="Email:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )
    
    email_usuario = usuario_logado.get("email", "")
    if len(email_usuario) > 28:
        email_perfil = email_usuario[:28] + "..."
    else:
        email_perfil = email_usuario

    canvas.create_text(
        630.0,
        231.2,
        anchor="nw",
        text=email_perfil,
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.create_text(
        522.0,
        301.5,
        anchor="nw",
        text="ID:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )

    canvas.create_text(
        580.0,
        301.5,
        anchor="nw",
        text=str(usuario_logado.get("id", "")),
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "button_1.png")
    )
    button_1 = Button(
        canvas, 
        image=canvas.button_image_1, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: tools.fade_out(window, canvas, lambda: tela_editar_perfil.criar_tela_editar_perfil(window, canvas, usuario_logado)),
        relief="flat"
    )
    button_1.place(
        x=701.0, 
        y=532.0, 
        width=181.0, 
        height=115.0
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "button_2.png")
    )
    button_2 = Button(
        canvas, 
        image=canvas.button_image_2, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: confirmar_e_deletar_conta(window, canvas, usuario_logado), 
        relief="flat"
    )
    button_2.place(
        x=941.0, 
        y=533.0, 
        width=181.0, 
        height=115.0
    )

    canvas.button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "button_3.png")
    )
    button_3 = Button(
        canvas, 
        image=canvas.button_image_3, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: transicao_para_logout(window, canvas), 
        relief="flat"
    )
    button_3.place(
        x=461.0, 
        y=532.0, 
        width=181.0, 
        height=115.0
    )


    canvas.button_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "button_4.png")
    )
    button_4 = Button(
        canvas, 
        image=canvas.button_image_4, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: verificar_pedido_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_4.place(
        x=170.0, 
        y=535.0, 
        width=232.0, 
        height=113.0
    )

    canvas.button_image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaPerfil", "button_5.png")
    )
    button_5 = Button(
        canvas, 
        image=canvas.button_image_5, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: transicao_para_menu(window, canvas, usuario_logado), 
        relief="flat"
    )
    button_5.place(
        x=1122.5, 
        y=63.0, 
        width=109.4, 
        height=111.0
    )

    canvas.create_text(
        364.0,
        462.0,
        anchor="nw",
        text="CONFIGURAÇÕES DE USUÁRIO:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    user_icon_filename = usuario_logado.get("icone", "button_3.png")
    clean_icon_filename = user_icon_filename.replace("button_", "icon_")
    
    icon_path = Path(__file__).parent / "perfil_icons" / clean_icon_filename
    
    img = Image.open(icon_path)
    max_size = (257, 257)
    img.thumbnail(max_size)
    canvas.user_icon_image = ImageTk.PhotoImage(img)
    
    canvas.create_image(
        302.0,
        252.0,
        image=canvas.user_icon_image
    )

def confirmar_e_deletar_conta(window, canvas, usuario_logado):
    from .modulos import usercrud
    resposta = tools.custom_yn(
        window,
        "Confirmar Exclusão", 
        "Tem a certeza de que deseja excluir a sua conta permanentemente? Esta ação não pode ser desfeita."
    )

    if resposta: 
        sucesso = usercrud.Usuario.deletar_conta(usuario_logado)
        if sucesso:
            tools.custom_messagebox(
                window, 
                "Conta Excluída", 
                "A sua conta foi excluída com sucesso. Será redirecionado para a tela inicial."
            )
            transicao_para_logout(window, canvas)