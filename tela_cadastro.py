from tkinter import Button, PhotoImage, Entry
import tela_inicial
import tools

user_icon = None

def _transicao_para_inicial(window, canvas):
    tools.fade_out(
        window,
        canvas,
        lambda: tela_inicial.criar_tela_inicial(window, canvas)
    )

def _selecionar_icone(canvas, x, y, nome_imagem_selecao, nome_icone):
    global user_icon
    user_icon = nome_icone
    print(f"Ícone selecionado: {user_icon}")

    if hasattr(canvas, "selecao_atual_id"):
        canvas.delete(canvas.selecao_atual_id)

    canvas.imagem_selecionada = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", nome_imagem_selecao)
    )
    canvas.selecao_atual_id = canvas.create_image(
        x,
        y,
        image=canvas.imagem_selecionada
    )
    canvas.tag_raise(canvas.selecao_atual_id)


def criar_tela_cadastro(window, canvas):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#EADFC8")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "image_1.png")
    )
    canvas.create_image(
        646.0373306274414,
        365.037353515625,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=649.0,
        y=588.0,
        width=371.0,
        height=78.0
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: _transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place(
        x=1158.0,
        y=60.0,
        width=67.0,
        height=73.0
    )

    canvas.icon_images = []

    icon_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_3.png")
    )
    canvas.icon_images.append(icon_image_3)
    canvas.create_image(
        155.0, 
        199.0, 
        image=icon_image_3, 
        tags=("icon_3",)
    )
    canvas.tag_bind(
        "icon_3",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 155.0, 199.0, "image_8.png", "button_3.png")
    )

    icon_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_4.png")
    )
    canvas.icon_images.append(icon_image_4)
    canvas.create_image(
        262.0, 
        199.0, 
        image=icon_image_4, 
        tags=("icon_4",)
    )
    canvas.tag_bind(
        "icon_4",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 262.0, 199.0, "image_5.png", "button_4.png")
    )

    icon_image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_5.png")
    )
    canvas.icon_images.append(icon_image_5)
    canvas.create_image(
        369.0, 
        198.0, 
        image=icon_image_5, 
        tags=("icon_5",)
    )
    canvas.tag_bind(
        "icon_5",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 369.0, 198.0, "image_7.png", "button_5.png")
    )

    icon_image_6 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_6.png")
    )
    canvas.icon_images.append(icon_image_6)
    canvas.create_image(
        155.0, 
        322.0, 
        image=icon_image_6, 
        tags=("icon_6",)
    )
    canvas.tag_bind(
        "icon_6",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 155.0, 322.0, "image_10.png", "button_6.png")
    )

    icon_image_7 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_7.png")
    )
    canvas.icon_images.append(icon_image_7)
    canvas.create_image(
        262.0, 
        322.0, 
        image=icon_image_7, 
        tags=("icon_7",)
    )
    canvas.tag_bind(
        "icon_7",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 262.0, 322.0, "image_9.png", "button_7.png")
    )

    icon_image_8 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_8.png")
    )
    canvas.icon_images.append(icon_image_8)
    canvas.create_image(
        370.0, 
        322.0, 
        image=icon_image_8, 
        tags=("icon_8",)
    )
    canvas.tag_bind(
        "icon_8",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 370.0, 322.0, "image_6.png", "button_8.png")
    )

    icon_image_9 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_9.png")
    )
    canvas.icon_images.append(icon_image_9)
    canvas.create_image(
        155.0, 
        452.0, 
        image=icon_image_9, 
        tags=("icon_9",)
    )
    canvas.tag_bind(
        "icon_9",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 155.0, 452.0, "image_3.png", "button_9.png")
    )

    icon_image_10 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_10.png")
    )
    canvas.icon_images.append(icon_image_10)
    canvas.create_image(
        261.0, 
        452.0, 
        image=icon_image_10, 
        tags=("icon_10",)
    )
    canvas.tag_bind(
        "icon_10",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 261.0, 452.0, "image_2.png", "button_10.png")
    )

    icon_image_11 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_11.png")
    )
    canvas.icon_images.append(icon_image_11)
    canvas.create_image(
        370.0, 
        451.0, 
        image=icon_image_11, 
        tags=("icon_11",)
    )
    canvas.tag_bind(
        "icon_11",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 370.0, 451.0, "image_4.png", "button_11.png")
    )

    icon_image_12 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_12.png")
    )
    canvas.icon_images.append(icon_image_12)
    canvas.create_image(
        155.0, 
        580.0, 
        image=icon_image_12, 
        tags=("icon_12",)
    )
    canvas.tag_bind(
        "icon_12",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 155.0, 580.0, "image_12.png", "button_12.png")
    )

    icon_image_13 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_13.png")
    )
    canvas.icon_images.append(icon_image_13)
    canvas.create_image(
        261.0, 
        580.0, 
        image=icon_image_13, 
        tags=("icon_13",)
    )
    canvas.tag_bind(
        "icon_13",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 261.0, 580.0, "image_11.png", "button_13.png")
    )

    icon_image_14 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_14.png")
    )
    canvas.icon_images.append(icon_image_14)
    canvas.create_image(
        370.0, 
        580.0, 
        image=icon_image_14, 
        tags=("icon_14",)
    )
    canvas.tag_bind(
        "icon_14",
        "<Button-1>",
        lambda e: _selecionar_icone(canvas, 370.0, 580.0, "image_13.png", "button_14.png")
    )

    canvas.create_text(
        489.0,
        132.0,
        anchor="nw",
        text="Nome:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        489.0,
        248.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        489.0,
        364.0,
        anchor="nw",
        text="Senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        489.0,
        475.0,
        anchor="nw",
        text="Confirme sua senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        153.0,
        76.0,
        anchor="nw",
        text="Escolha um ícone \n               de perfil ",
        fill="#EED3B2",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(
        588.0,
        70.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "entry_1.png")
    )
    canvas.create_image(
        836.0,
        200.0,
        image=canvas.entry_image_1
    )
    entry_1 = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=489.0,
        y=171.0,
        width=694.0,
        height=56.0
    )

    canvas.entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "entry_2.png")
    )
    canvas.create_image(
        836.0,
        316.0,
        image=canvas.entry_image_2
    )
    entry_2 = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=489.0,
        y=287.0,
        width=694.0,
        height=56.0
    )

    canvas.entry_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "entry_3.png")
    )
    canvas.create_image(
        836.0,
        432.0,
        image=canvas.entry_image_3
    )
    entry_3 = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=489.0,
        y=403.0,
        width=694.0,
        height=56.0
    )

    canvas.entry_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "entry_4.png")
    )
    canvas.create_image(
        836.0,
        548.0,
        image=canvas.entry_image_4
    )
    entry_4 = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=489.0,
        y=519.0,
        width=694.0,
        height=56.0
    )