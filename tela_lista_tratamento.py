from tkinter import Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
import tools
import tela_menu_principal
from modulos import animalcrud

def transicao_para_menu_principal(window,canvas,usuario_logado):
    tools.fade_out(window,canvas,lambda: tela_menu_principal.criar_tela_menu_principal(window,canvas,usuario_logado))

def criar_tela_lista_tratamento(window,canvas,usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaListaTratamento", "image_1.png"))
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )
    canvas.create_text(
        460.0,
        33.0,
        anchor="nw",
        text="Animais em Tratamento",
        fill="#EED3B2",
        font=("Poppins Black", 35 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaListaTratamento", "button_2.png"))
    button_voltar = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_principal(
            window,
            canvas,
            usuario_logado
        ),
        relief="flat"
    )
    button_voltar.place(
        x=1155.0,
        y=19.0,
        width=90.0,
        height=89.0
    )

    animais_em_tratamento = animalcrud.carregar_dados("animais_tratamento.json")
    
    canvas.lista_imagens_botoes = []
    canvas.lista_imagens_animais = []

    posicao_y_inicial = 120.0
    espacamento_vertical = 237.0

    if not animais_em_tratamento:
        canvas.create_text(
            640,
            360,
            text="Não há animais em tratamento no momento.",
            fill="#44312D",
            font=("Poppins", 24),
            anchor="center"
        )
        return

    for i, animal in enumerate(animais_em_tratamento):
        y_atual = posicao_y_inicial + (i * espacamento_vertical)

        img_botao = PhotoImage(
            file=tools.relative_to_assets("TelaListaTratamento", "button_1.png")
        )
        canvas.lista_imagens_botoes.append(img_botao)
        
        tag_card = f"card_{animal.get('id')}"
        canvas.create_image(
            (32.0 + 1227.0) / 2,
            y_atual + (217.0 / 2),
            image=img_botao,
            tags=(tag_card,)
        )
        
        canvas.tag_bind(
            tag_card,
            "<Button-1>",
            lambda e, id=animal.get('id'): print(f"Card do animal ID {id} clicado")
        )

        caminho_foto = Path(__file__).parent / "fotos_animais" / animal.get("foto", "")
        if caminho_foto.exists():
            img = Image.open(caminho_foto)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            canvas.lista_imagens_animais.append(img_tk)
            
            canvas.create_image(
                156.0,
                y_atual + 109,
                image=img_tk
            )

        canvas.create_text(
            304.0,
            y_atual + 30,
            anchor="nw",
            text=f"Nome: {animal.get('nome', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        canvas.create_text(
            304.0,
            y_atual + 69,
            anchor="nw",
            text=f"Espécie: {animal.get('especie', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        canvas.create_text(
            304.0,
            y_atual + 107,
            anchor="nw",
            text=f"Sexo: {animal.get('sexo', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        canvas.create_text(
            304.0,
            y_atual + 145,
            anchor="nw",
            text=f"Idade: {animal.get('idade', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )