from tkinter import Button, PhotoImage, Frame, Canvas, Scrollbar, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_menu_principal(window, canvas, usuario_logado):
    from telas import tela_menu_principal
    tools.fade_out(window, canvas, lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado))

def criar_tela_lista_tratamento(window, canvas, usuario_logado):
    from .modulos import animalcrud
    tools.limpar_tela(canvas)
    canvas.configure(bg="#44312D")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaListaAdocao", "image_1.png")
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )
    canvas.create_text(
        449.0,
        33.0,
        anchor="nw",
        text="Animais em Tratamento",
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
        command=lambda: transicao_para_menu_principal(window, canvas, usuario_logado),
        relief="flat"
    )
    button_voltar.place(
        x=1155.0,
        y=19.0,
        width=90.0,
        height=89.0
    )

    main_frame = Frame(canvas, bg="#44312D", bd=0, highlightthickness=0)
    main_frame.place(x=32, y=120, width=1227, height=580)

    canvas_lista = Canvas(
        main_frame,
        bg="#44312D",
        bd=0,
        highlightthickness=0
    )
    
    frame_cards = Frame(
        canvas_lista,
        bg="#44312D"
    )

    scrollbar = Scrollbar(
        main_frame,
        orient="vertical",
        command=canvas_lista.yview
    )
    canvas_lista.configure(
        yscrollcommand=scrollbar.set
    )

    scrollbar.pack(side="right", fill="y")
    canvas_lista.pack(side="left", fill="both", expand=True)
    canvas_lista.create_window((0, 0), window=frame_cards, anchor="nw")

    def onFrameConfigure(event):
        canvas_lista.configure(
            scrollregion=canvas_lista.bbox("all")
        )

    frame_cards.bind("<Configure>", onFrameConfigure)

    animais_em_tratamento = animalcrud.carregar_dados("animais_tratamento.json")
    
    canvas.lista_imagens_botoes = []
    canvas.lista_imagens_animais = []

    if not animais_em_tratamento:
        label_vazio = Label(
            frame_cards,
            text="Não há animais em tratamento no momento.",
            bg="#44312D",
            fg="#44312D",
            font=("Poppins", 24)
        )
        label_vazio.pack(pady=200)
        return

    placeholder_path = tools.relative_to_assets("TelaListaAdocao", "image_2.png")
    placeholder_pil = Image.open(placeholder_path)
    largura_ref, altura_ref = placeholder_pil.size
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil)

    for animal in animais_em_tratamento:
        img_botao = PhotoImage(
            file=tools.relative_to_assets("TelaListaAdocao", "button_1.png")
        )
        canvas.lista_imagens_botoes.append(img_botao)
        
        card_frame = Frame(
            frame_cards,
            width=1227,
            height=217,
            bg="#44312D"
        )
        card_frame.pack(pady=10)

        card_canvas = Canvas(
            card_frame,
            width=1227,
            height=217,
            bg="#44312D",
            highlightthickness=0
        )
        card_canvas.pack()

        tag_card = f"card_{animal.get('id')}"
        card_canvas.create_image(
            1227 / 2,
            217 / 2,
            image=img_botao,
            tags=(tag_card,)
        )
        
        card_canvas.tag_bind(
            tag_card,
            "<Button-1>",
            lambda e, id=animal.get('id'): print(f"Card do animal ID {id} clicado")
        )

        card_canvas.create_image(
            124.0,
            109,
            image=canvas.placeholder_tk
        )

        caminho_foto = Path(__file__).parent / "fotos_animais" / animal.get("foto", "")
        if caminho_foto.exists():
            img = Image.open(caminho_foto)
            img_redimensionada = img.resize(
                (largura_ref, altura_ref),
                Image.Resampling.LANCZOS
            )
            img_tk = ImageTk.PhotoImage(img_redimensionada)
            canvas.lista_imagens_animais.append(img_tk)
            
            card_canvas.create_image(
                124.0,
                109,
                image=img_tk
            )

        card_canvas.create_text(
            272.0,
            30,
            anchor="nw",
            text=f"Nome: {animal.get('nome', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        card_canvas.create_text(
            272.0,
            69,
            anchor="nw",
            text=f"Espécie: {animal.get('especie', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        card_canvas.create_text(
            272.0,
            107,
            anchor="nw",
            text=f"Sexo: {animal.get('sexo', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )
        card_canvas.create_text(
            272.0,
            145,
            anchor="nw",
            text=f"Idade: {animal.get('idade', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1)
        )