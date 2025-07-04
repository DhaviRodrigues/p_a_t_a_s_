from tkinter import Button, PhotoImage
from telas import tools
from telas import tela_menu_principal

def transicao_para_menu_principal(window, canvas, usuario_logado):
    tools.fade_out(window, canvas, lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado))

def criar_tela_doacao(window, canvas, usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )

    button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_principal(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place(
        x=1159.9130859375,
        y=0.0,
        width=104.08695983886719,
        height=114.0
    )

    button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=665.0,
        y=428.0,
        width=420.0,
        height=75.0
    )

    button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "button_3.png")
    )
    button_3 = Button(
        canvas,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=665.0,
        y=275.0,
        width=420.0,
        height=75.0
    )

    button_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "button_4.png")
    )
    button_4 = Button(
        canvas,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=665.0,
        y=197.0,
        width=420.0,
        height=75.0
    )

    image_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "image_2.png")
    )
    canvas.create_image(
        874.0,
        594.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaDoacao", "image_3.png")
    )
    canvas.create_image(
        874.0,
        252.0,
        image=image_image_3
    )