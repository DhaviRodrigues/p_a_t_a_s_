from tkinter import Button, PhotoImage, Frame, Canvas, Scrollbar, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_menu_adm(window, canvas, usuario_logado):
    """Realiza a transição da lista de pedidos recusados de volta para o menu de administrador."""
    from telas import tela_menu_adm
    tools.fade_out(window, canvas, lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def criar_tela_lista_pedidos_recusado(window, canvas, usuario_logado):
    """
    Cria a interface gráfica que exibe uma lista rolável de pedidos de adoção recusados.
    Para cada pedido, um card exibe o nome do animal e as informações do usuário que solicitou.
    A tela é destinada a administradores.
    """
    from .modulos import pedidos
    from telas import tela_info_pedido_recusado_aprovado
    from .modulos import animalcrud

    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#44312D") # Define a cor de fundo do canvas.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaLista", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0,
        365.0,
        image=canvas.image_1
    )
    canvas.create_text( # Título da tela.
        449.0,
        33.0,
        anchor="nw",
        text="Pedidos Recusados",
        fill="#EED3B2",
        font=("Poppins Black", 35 * -1)
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaLista", "button_2.png")
    )
    button_voltar = Button( # Botão para voltar ao menu de administrador.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_adm(window, canvas, usuario_logado),
        relief="flat"
    )
    button_voltar.place( # Posiciona o botão "Voltar".
        x=1155.0,
        y=19.0,
        width=90.0,
        height=89.0
    )

    main_frame = Frame(canvas, bg="#44312D", bd=0, highlightthickness=0) # Frame principal que conterá a lista rolável.
    main_frame.place(x=32, y=120, width=1227, height=580) # Posiciona o frame principal.

    canvas_lista = Canvas( # Canvas que permitirá a rolagem.
        main_frame,
        bg="#44312D",
        bd=0,
        highlightthickness=0
    )
    
    frame_cards = Frame( # Frame interno que conterá todos os cards dos pedidos.
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

    pedidos_recusados = pedidos.carregar_dados("pedidos_recusado.json") # Carrega os dados dos pedidos recusados.
    todos_animais = animalcrud.carregar_dados("animais_adocao.json") # Carrega os dados de 'animais.json'

    canvas.lista_imagens_botoes = [] # Lista para manter referência das imagens dos botões.
    canvas.lista_imagens_animais = [] # Lista para manter referência das imagens dos animais.

    if not pedidos_recusados: # Se não houver pedidos recusados...
        label_vazio = Label( # Cria um label informativo.
            frame_cards,
            text="Não há nenhum pedido recusado ainda.",
            bg="#44312D",
            fg="#EED3B2",
            font=("Poppins", 24)
        )
        label_vazio.pack(pady=200) # Exibe o label.
        return # Encerra a função.

    placeholder_path = tools.relative_to_assets("TelaLista", "image_2.png") # Carrega a imagem de placeholder para ser usada nos cards.
    placeholder_pil = Image.open(placeholder_path)
    largura_ref, altura_ref = placeholder_pil.size
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil)

    for pedido in pedidos_recusados: # Itera sobre cada pedido aprovado para criar um card.
        for animal in todos_animais: # Verifica se o animal do pedido existe na lista de animais.
            if animal.get("id") == pedido.get("id_animal"):
                nome_arquivo_foto = animal.get("foto", "") # Obtém o nome do arquivo da foto do animal.
            
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

                tag_card = f"card_{pedido.get('id_mensagem')}" # Cria uma tag única para os elementos do card.
                
                card_canvas.create_image( # Desenha a imagem de fundo do card.
                    1227 / 2,
                    217 / 2,
                    image=img_botao,
                    tags=(tag_card,)
                )

                card_canvas.tag_bind(
                    tag_card,
                    "<Button-1>",  # Associa um evento de clique ao card.
                    lambda e: tools.fade_out(window,canvas,lambda: tela_info_pedido_recusado_aprovado.criar_tela_info_pedido_recusado_aprovado(window, canvas, usuario_logado, pedido, nome_arquivo_foto)))

                card_canvas.create_image( # Desenha a imagem placeholder para a foto.
                    124.0,
                    109,
                    image=canvas.placeholder_tk,
                    tags=(tag_card,)
                )

                caminho_foto = Path(__file__).parent / "fotos_animais" / nome_arquivo_foto # Constrói o caminho para a foto real do animal.
                if caminho_foto.exists(): # Verifica se o arquivo da foto existe.
                    img = Image.open(caminho_foto) # Abre a imagem do animal.
                    img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS) # Redimensiona a imagem.
                    img_tk = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem para formato Tkinter.
                    canvas.lista_imagens_animais.append(img_tk) # Adiciona à lista para evitar garbage collection.
                    
                    card_canvas.create_image( # Exibe a foto real do animal sobre o placeholder.
                        124.0,
                        109,
                        image=img_tk,
                        tags=(tag_card,)
                    )

                card_canvas.create_text( # Exibe o nome do animal do pedido.
                    272.0,
                    30,
                    anchor="nw",
                    text=f"Nome do animal: {pedido.get('nome_animal', '')}",
                    fill="#44312D",
                    font=("Poppins Black", 32 * -1),
                    tags=(tag_card,)
                )
                card_canvas.create_text( # Exibe o email do usuário do pedido.
                    272.0,
                    69,
                    anchor="nw",
                    text=f"Email do Usuário: {pedido.get('email_usuario', '')}",
                    fill="#44312D",
                    font=("Poppins Black", 32 * -1),
                    tags=(tag_card,)
                )
                card_canvas.create_text( # Exibe o nome do usuário do pedido.
                    272.0,
                    107,
                    anchor="nw",
                    text=f"Nome do Usuário: {pedido.get('nome_usuario', '')}",
                    fill="#44312D",
                    font=("Poppins Black", 32 * -1),
                    tags=(tag_card,)
                )