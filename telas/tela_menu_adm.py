from tkinter import Button, PhotoImage
import tools

def transicao_para_inicial(window, canvas):
    from telas import tela_inicial
    tools.fade_out(
        window,
        canvas,
        lambda: tela_inicial.criar_tela_inicial(window, canvas)
    )

def criar_tela_menu_adm(window, canvas, usuario_logado):
    from telas import tela_cadastrar_animal
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_1.png")
    )
    canvas.create_image(
        640.0,
        376.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tools.fade_out(window, canvas, lambda: tela_cadastrar_animal.criar_tela_cadastrar_animal(window, canvas, usuario_logado)),
        relief="flat"
    )
    button_1.place(
        x=98.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=417.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_3.png")
    )
    button_3 = Button(
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=731.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.button_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_4.png")
    )
    button_4 = Button(
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=1042.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_2.png")
    )
    canvas.create_image(
        797.0,
        455.0,
        image=canvas.image_2
    )

    canvas.image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_3.png")
    )
    canvas.create_image(
        1111.0,
        455.0,
        image=canvas.image_3
    )

    canvas.image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_4.png")
    )
    canvas.create_image(
        479.0,
        454.9999694824219,
        image=canvas.image_4
    )

    canvas.image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_5.png")
    )
    canvas.create_image(
        163.0,
        455.0,
        image=canvas.image_5
    )

    canvas.create_text(
        366.0,
        68.0,
        anchor="nw",
        text="Menu Administrativo",
        fill="#EED3B2",
        font=("Poppins Black", 48 * -1)
    )

    canvas.button_image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_5.png")
    )
    button_5 = Button(
        canvas,
        image=canvas.button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_5.place(
        x=1133.0,
        y=48.0,
        width=106.74418640136719,
        height=102.0
    )