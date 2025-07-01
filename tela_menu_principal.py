from tkinter import Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
import tools
import tela_perfil

def criar_tela_menu_principal(window, canvas, usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_bg = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_1.png")
    )
    canvas.create_image(
        640.0,
        400.0,
        image=canvas.image_bg
    )

    canvas.button_adotar = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_adotar,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Botão Adotar clicado"),
        relief="flat"
    )
    button_1.place(
        x=950.0,
        y=545.0,
        width=165.0,
        height=168.0
    )

    canvas.button_tratamento = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_tratamento,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Botão Tratamento clicado"),
        relief="flat"
    )
    button_2.place(
        x=160.0,
        y=545.0,
        width=165.0,
        height=168.0
    )

    canvas.button_editar_perfil = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_3.png")
    )
    button_3 = Button(
        canvas,
        image=canvas.button_editar_perfil,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Botão Editar Perfil clicado"),
        relief="flat"
    )
    button_3.place(
        x=562.0,
        y=545.0,
        width=164.0,
        height=168.0
    )

    canvas.image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_2.png")
    )
    canvas.create_image(
        1034.0,
        409.0,
        image=canvas.image_2
    )

    canvas.image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_3.png")
    )
    canvas.create_image(
        242.2,
        410.0,
        image=canvas.image_3
    )

    canvas.image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_4.png")
    )
    canvas.create_image(
        645.0,
        410.0,
        image=canvas.image_4
    )

    canvas.create_text(
        521.0,
        14.0,
        anchor="nw",
        text="Menu",
        fill="#EED3B2",
        font=("Poppins Black", 79 * -1)
    )

    canvas.create_text(
        109.0,
        20.0,
        anchor="nw",
        text="Ver\nPerfil",
        fill="#44312D",
        font=("Poppins Black", 32 * -1),
        justify="left",
        tags=("ver_perfil_link",)
    )
    canvas.tag_bind(
        "ver_perfil_link",
        "<Button-1>",
        lambda e: tools.fade_out(window, canvas, lambda: tela_perfil.criar_tela_perfil(window, canvas, usuario_logado))
    )

    user_icon_filename = usuario_logado.get("icone", "button_3.png")
    clean_icon_filename = user_icon_filename.replace("button_", "icon_")
    
    icon_path = Path(__file__).parent / "perfil_icons" / clean_icon_filename
    
    img = Image.open(icon_path)
    max_size = (80, 80)
    img.thumbnail(max_size)
    canvas.user_icon_image = ImageTk.PhotoImage(img)
    
    canvas.create_image(
        53.0,
        45.0,
        image=canvas.user_icon_image
    )