from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_lista_perfil(window, canvas, usuario_logado):
    from telas import tela_perfil
    tools.fade_out(window, canvas, lambda: tela_perfil.criar_tela_perfil(window, canvas, usuario_logado))

def criar_tela_pedido_usuario(window, canvas, usuario_logado):
    tools.limpar_tela(canvas)
    from .modulos import pedidos
    from .modulos import animalcrud

    user_id = usuario_logado.get('id')
    todos_pedidos = pedidos.carregar_dados('pedidos.json')
    todos_animais = animalcrud.carregar_dados("animais_adocao.json")

    id_animal_pedido = None
    
    animal_pedido = None

    for pedidos_adocao in todos_pedidos:
        if pedidos_adocao.get('id_usuario') == user_id:
            id_animal_pedido = pedidos_adocao.get("id_animal")
            print(f"ID do animal pedido: {id_animal_pedido}")
            status = pedidos_adocao.get("processo")

    if id_animal_pedido != None:
        print("bomdia")
        for animal in todos_animais:
            if animal.get('id') == id_animal_pedido:
                print(f'id animal encontrado: {animal.get("id")}')
                animal_pedido = animal


    canvas.configure(
        bg="#FFFFFF"
    )

    canvas.image_4 = PhotoImage(
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "image_4.png"
        )
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_4
    )

    canvas.create_text(
        322.0,
        103.0,
        anchor="nw",
        text=f"Nome: {animal_pedido.get('nome', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        160.0,
        anchor="nw",
        text=f"Espécie: {animal_pedido.get('especie', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        217.0,
        anchor="nw",
        text=f"Sexo: {animal_pedido.get('sexo', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        322.0,
        271.0,
        anchor="nw",
        text=f"Idade: {animal_pedido.get('idade', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text(
        110.0,
        343.0,
        anchor="nw",
        text= f"Andamento da adoção:",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    info_label = Label(
        canvas,
        text=f"{status}",
        font=("Poppins Black", 30 * -1),
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

    canvas.button_image_4 = PhotoImage(
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_1.png"
        )
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_perfil(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place(
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
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

    caminho_foto = Path(__file__).parent / "fotos_animais" / animal_pedido.get("foto", "")
    if caminho_foto.exists():
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPet", "image_2.png"))
        largura_ref, altura_ref = placeholder_pil.size

        img = Image.open(caminho_foto)
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS)
        canvas.foto_animal_pedido_tk = ImageTk.PhotoImage(img_redimensionada)
        
        canvas.create_image(
            184.0,
            209.0,
            image=canvas.foto_animal_pedido_tk
        )