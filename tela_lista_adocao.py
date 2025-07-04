from tkinter import Button, PhotoImage, messagebox
from pathlib import Path
from PIL import Image, ImageTk
import tools
import tela_menu_principal
from modulos import animalcrud

def transicao_para_menu(window,canvas,usuario_logado):
    tools.fade_out(window,canvas,lambda: tela_menu_principal.criar_tela_menu_principal(window,canvas,usuario_logado))

def criar_tela_lista_adocao(window,canvas,usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaListaAdocao", "image_1.png")
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )
    canvas.create_text(
        319.0,
        33.0,
        anchor="nw",
        text="Animais Disponíveis Para Adoção",
        fill="#EED3B2",
        font=("Poppins Black", 35 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaListaAdocao", "button_2.png")
    )
    button_voltar = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu(
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

    animais_para_adocao = animalcrud.carregar_dados("animais_adocao.json")
    
    canvas.lista_imagens_botoes = []
    canvas.lista_imagens_animais = []

    posicao_y_inicial = 120.0
    espacamento_vertical = 237.0

    if not animais_para_adocao:
        canvas.create_text(
            640,
            360,
            text="Não há animais para adoção no momento.",
            fill="#44312D",
            font=("Poppins", 24),
            anchor="center"
        )
        return

    for i, animal in enumerate(animais_para_adocao):
        y_atual = posicao_y_inicial + (i * espacamento_vertical)

        img_botao = PhotoImage(
            file=tools.relative_to_assets("TelaListaAdocao", "button_1.png")
        )
        canvas.lista_imagens_botoes.append(img_botao)
        
        animal_card = Button(
            canvas,
            image=img_botao,
            borderwidth=0,
            highlightthickness=0,
            command=lambda id=animal.get('id'): print(f"Card do animal ID {id} clicado"),
            relief="flat"
        )
        animal_card.place(
            x=32.0,
            y=y_atual,
            width=1227.0,
            height=217.0
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