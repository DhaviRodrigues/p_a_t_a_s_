from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools


def transicao_para_lista_adocao(window, canvas, usuario_logado):
    from telas import tela_lista_adocao
    tools.fade_out(window, canvas, lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado))

def tentar_adotar(window, canvas, animal_clicado, usuario_logado):
    from .modulos import pedidos

    if usuario_logado.get('pedido', True):
        tools.custom_messagebox(
            window,
            "Adoção Pendente",
            "Você já possui um pedido de adoção pendente.\n Para mais informações, veja seu perfil."
        )
    elif animal_clicado.get('processo_adoacao', True):
        tools.custom_messagebox(
            window,
            "Adoção Pendente",
            "Este animal já está em processo de adoção.\n Caso queira, adote outro animal."
        )
    else:
        resposta = tools.custom_yn(
            window,
            "Confirmar Pedido de Adoção", 
            "Tem a certeza de que deseja adotar este animal?"
        )
        if resposta:

            pedidos.Pedidos.criar_pedido_adocao(animal_clicado, usuario_logado)
            if pedidos.Pedidos.criar_pedido_adocao:
                tools.custom_messagebox(
                    window,
                    "Pedido Enviado",
                    "O seu pedido de adoção foi enviado com sucesso!\nVeja mais informações no seu perfil."
                )
            else:
                tools.custom_messagebox(
                    window,
                    "Erro",
                    "Ocorreu um erro ao enviar o pedido de adoção. Por favor, tente novamente mais tarde\n\n Peço que nos envie uma mensagem relatando o erro."
                )


def criar_tela_info_pet_adocao(window, canvas, usuario_logado, animal_clicado):
    tools.limpar_tela(canvas)
    canvas.configure(
        bg="#FFFFFF"
    )

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "image_1.png"
        )
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )

    canvas.create_text(
        322.0,
        103.0,
        anchor="nw",
        text=f"Nome: {animal_clicado.get('nome', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        160.0,
        anchor="nw",
        text=f"Espécie: {animal_clicado.get('especie', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        217.0,
        anchor="nw",
        text=f"Sexo: {animal_clicado.get('sexo', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        271.0,
        anchor="nw",
        text=f"Idade: {animal_clicado.get('idade', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    info_label = Label(
        canvas,
        text=animal_clicado.get('informacoes', 'Nenhuma informação adicional.'),
        font=("Poppins", 15),
        fg="#44312D",
        bg="#EED3B2", 
        wraplength=920,
        justify="left",
        anchor="nw"
    )
    info_label.place(
        x=120.0,
        y=400.0,
        width=920.0,
        height=250.0 
    )

    canvas.create_text(
        129.0,
        343.0,
        anchor="nw",
        text="Outras informações:",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_1.png"
        )
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place(
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_2.png"
        )
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_adotar(window, canvas, animal_clicado, usuario_logado),
        relief="flat"
    )
    button_2.place(
        x=1079.0,
        y=557.0,
        width=181.0,
        height=116.0
    )

    placeholder_path = tools.relative_to_assets(
        "TelaInfoPet",
        "image_2.png"
    )
    placeholder_pil = Image.open(placeholder_path)
    largura_ref, altura_ref = placeholder_pil.size
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil)

    canvas.create_image(
        184.0,
        209.0,
        image=canvas.placeholder_tk
    )

    caminho_foto = Path(__file__).parent / "fotos_animais" / animal_clicado.get("foto", "")
    if caminho_foto.exists():
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPet", "image_2.png"))
        largura_ref, altura_ref = placeholder_pil.size

        img = Image.open(caminho_foto)
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS)
        canvas.foto_animal_tk = ImageTk.PhotoImage(img_redimensionada)
        
        canvas.create_image(
            184.0,
            209.0,
            image=canvas.foto_animal_tk
        )