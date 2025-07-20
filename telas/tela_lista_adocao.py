from tkinter import Button, PhotoImage, messagebox, Frame, Canvas, Scrollbar, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_menu_principal(window,canvas,usuario_logado):
    """Realiza a transição da lista de adoção para o menu principal do usuário."""
    from telas import tela_menu_principal

    tools.fade_out(window,canvas,lambda: tela_menu_principal.criar_tela_menu_principal(window,canvas,usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_menu_adm(window, canvas, usuario_logado):
    """Realiza a transição da lista de adoção para o menu de administrador."""
    from telas import tela_menu_adm
    tools.fade_out(window, canvas, lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def criar_tela_lista_adocao(window,canvas,usuario_logado):
    """
    Cria a interface gráfica que exibe uma lista rolável de animais para adoção.
    Para cada animal, um card clicável exibe informações básicas, foto e status da adoção.
    A interação com o card varia se o usuário é administrador ou não.
    Caso seja administrador, o card leva à tela de edição do animal.
    Caso contrário, leva à tela de informações do animal para adoção.
    """
    from telas import tela_info_pet_adocao
    from .modulos import animalcrud
    from telas import tela_editar_animal

    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure( # Define a cor de fundo do canvas.
        bg="#44312D"
    )

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaLista", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0,
        365.0,
        image=canvas.image_1
    )
    canvas.create_text( # Título da tela.
        319.0,
        33.0,
        anchor="nw",
        text="Animais Disponíveis Para Adoção",
        fill="#EED3B2",
        font=("Poppins Black", 35 * -1)
    )

    canvas.button_image_2= PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaLista", "button_2.png"))

    button_2 = Button( # Botão para voltar ao menu anterior.
    canvas,
    image=canvas.button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: tools.fade_out(window, canvas,lambda: ( # Ação do botão é condicional.
            transicao_para_menu_adm(window, canvas, usuario_logado) # Volta para o menu adm se o usuário for adm.
            if usuario_logado.get("adm")
            else transicao_para_menu_principal(window,canvas,usuario_logado))), # Senão, volta para o menu principal.
    relief="flat"
    )

    button_2.place( # Posiciona o botão "Voltar".
        x=28.0,
        y=28.0,
        width=90.0,
        height=89.0
    )

    main_frame = Frame( # Frame principal que conterá a lista rolável.
        canvas,
        bg="#44312D",
        bd=0,
        highlightthickness=0
    )
    main_frame.place( # Posiciona o frame principal.
        x=32,
        y=120,
        width=1227,
        height=580
    )

    canvas_lista = Canvas( # Canvas que permitirá a rolagem.
        main_frame,
        bg="#44312D",
        bd=0,
        highlightthickness=0
    )
    frame_cards = Frame( # Frame interno que conterá todos os cards dos animais.
        canvas_lista,
        bg="#44312D"
    )

    scrollbar = Scrollbar( # Barra de rolagem vertical.
        main_frame,
        orient="vertical",
        command=canvas_lista.yview
    )
    canvas_lista.configure( # Configura o canvas para usar a barra de rolagem.
        yscrollcommand=scrollbar.set
    )

    scrollbar.pack(side="right", fill="y") # Empacota a barra de rolagem à direita.
    canvas_lista.pack(side="left", fill="both", expand=True) # Empacota o canvas à esquerda.
    canvas_lista.create_window((0, 0), window=frame_cards, anchor="nw") # Adiciona o frame de cards dentro do canvas.

    def onFrameConfigure(event): # Função para reconfigurar a região de rolagem.
        canvas_lista.configure(
            scrollregion=canvas_lista.bbox("all")
        )

    frame_cards.bind("<Configure>", onFrameConfigure) # Associa a função ao evento de configuração do frame.
    
    animais_para_adocao = animalcrud.carregar_dados("animais_adocao.json") # Carrega os dados dos animais para adoção.
    
    canvas.lista_imagens_botoes = [] # Lista para manter referência das imagens dos botões.
    canvas.lista_imagens_animais = [] # Lista para manter referência das imagens dos animais.

    if not animais_para_adocao: # Se não houver animais para adoção...
        label_vazio = Label( # Cria um label informativo.
            frame_cards,
            text="Não há animais para adoção no momento.",
            bg="#44312D",
            fg="#EED3B2",
            font=("Poppins", 24)
        )
        label_vazio.pack(pady=200) # Exibe o label.
        return # Encerra a função.

    placeholder_path = tools.relative_to_assets("TelaLista", "image_2.png") # Caminho para a imagem placeholder.
    placeholder_pil = Image.open(placeholder_path) # Abre a imagem placeholder.
    largura_ref, altura_ref = placeholder_pil.size # Pega as dimensões da imagem.
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil) # Converte para o formato do Tkinter.

    for todos_animais in animais_para_adocao: # Itera sobre cada animal para criar um card.
        img_botao = PhotoImage( # Carrega a imagem de fundo do card.
            file=tools.relative_to_assets("TelaLista", "button_1.png")
        )
        canvas.lista_imagens_botoes.append(img_botao) # Adiciona à lista para evitar garbage collection.
        
        card_frame = Frame( # Cria um frame para o card.
            frame_cards,
            width=1227,
            height=217,
            bg="#44312D"
        )
        card_frame.pack(pady=10) # Empacota o frame do card.

        card_canvas = Canvas( # Cria um canvas dentro do frame do card.
            card_frame,
            width=1227,
            height=217,
            bg="#44312D",
            highlightthickness=0
        )
        card_canvas.pack() # Empacota o canvas do card.

        tag_card = f"card_{todos_animais.get('id')}" # Cria uma tag única para os elementos do card.
        card_canvas.create_image( # Desenha a imagem de fundo do card.
            1227 / 2,
            217 / 2,
            image=img_botao,
            tags=(tag_card,)
        )
        
        card_canvas.tag_bind(tag_card, # Associa um evento de clique a todos os elementos com a tag.
            "<Button-1>",
            lambda e, animal=todos_animais: tools.fade_out(window,canvas, # Define a ação de clique no card.
            lambda: tela_editar_animal.criar_tela_editar_animal(window, canvas, usuario_logado, animal, "animais_adocao.json") # Se for admin, vai para a tela de edição.
            if usuario_logado.get("adm") == True
            else tela_info_pet_adocao.criar_tela_info_pet_adocao(window, canvas, usuario_logado, animal))) # Se não, vai para a tela de informações de adoção.
        
        card_canvas.create_image( # Desenha a imagem placeholder da foto do animal.
            124.0,
            109,
            image=canvas.placeholder_tk,
            tags=(tag_card,)
        )

        caminho_foto = Path(__file__).parent / "fotos_animais" / todos_animais.get("foto", "") # Constrói o caminho para a foto do animal.
        if caminho_foto.exists(): # Se a foto existir...
            img = Image.open(caminho_foto) # Abre a imagem.
            img_redimensionada = img.resize( # Redimensiona a imagem.
                (largura_ref, altura_ref),
                Image.Resampling.LANCZOS
            )
            img_tk = ImageTk.PhotoImage(img_redimensionada) # Converte para o formato do Tkinter.
            canvas.lista_imagens_animais.append(img_tk) # Adiciona à lista para evitar garbage collection.
            
            card_canvas.create_image( # Desenha a foto do animal sobre o placeholder.
                124.0,
                109,
                image=img_tk,
                tags=(tag_card,)
            )

        card_canvas.create_text( # Exibe o nome do animal.
            272.0,
            30,
            anchor="nw",
            text=f"Nome: {todos_animais.get('nome', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1),
            tags=(tag_card,)
        )

        if not todos_animais.get("processo_adoacao", False): # Verifica se o animal não está em processo de adoção.
            card_canvas.create_text( # Exibe a mensagem de que está disponível.
                730,
                145,
                anchor="nw",
                text=f"Pet disponível para adoção",
                fill="#44312D",
                font=("Poppins Black", 24 * -1),
                tags=(tag_card,)
            )
        else: # Caso o animal já esteja em processo de adoção.
            card_canvas.create_text( # Exibe a mensagem de que está em processo.
                730.0,
                145,
                anchor="nw",
                text=f"O Pet já está em processo de adoção",
                fill="#44312D",
                font=("Poppins Black", 24 * -1),
                tags=(tag_card,)
            )

            card_canvas.create_text( # Exibe a espécie do animal.
                272.0,
                69,
                anchor="nw",
                text=f"Espécie: {todos_animais.get('especie', '')}",
                fill="#44312D",
                font=("Poppins Black", 32 * -1),
                tags=(tag_card,)
            )

            card_canvas.create_text( # Exibe a espécie do animal (duplicado no código original).
                272.0,
                69,
                anchor="nw",
                text=f"Espécie: {todos_animais.get('especie', '')}",
                fill="#44312D",
                font=("Poppins Black", 32 * -1),
                tags=(tag_card,)
            )

        card_canvas.create_text( # Exibe o sexo do animal.
            272.0,
            107,
            anchor="nw",
            text=f"Sexo: {todos_animais.get('sexo', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1),
            tags=(tag_card,)
        )
        card_canvas.create_text( # Exibe a idade do animal.
            272.0,
            145,
            anchor="nw",
            text=f"Idade: {todos_animais.get('idade', '')}",
            fill="#44312D",
            font=("Poppins Black", 32 * -1),
            tags=(tag_card,)
        )