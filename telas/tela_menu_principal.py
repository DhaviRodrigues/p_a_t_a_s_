from tkinter import Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_feedback(window, canvas, usuario_logado):
    """Realiza a transição do menu principal para a tela de feedback."""
    from telas import tela_feedback
    tools.fade_out(window,canvas,lambda: tela_feedback.criar_tela_feedback(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_adocao(window, canvas, usuario_logado):
    """Realiza a transição do menu principal para a lista de adoção."""
    from telas import tela_lista_adocao
    tools.fade_out(window,canvas,lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_tratamento(window, canvas, usuario_logado):
    """Realiza a transição do menu principal para a lista de tratamentos."""
    from telas import tela_lista_tratamento
    tools.fade_out(window,canvas, lambda: tela_lista_tratamento.criar_tela_lista_tratamento(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_doacao(window, canvas, usuario_logado):
    """Realiza a transição do menu principal para a tela de doação."""
    from telas import tela_doacao
    tools.fade_out(window, canvas, lambda: tela_doacao.criar_tela_doacao(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_perfil(window, canvas, usuario_logado):
    """Realiza a transição do menu principal para a tela de perfil do usuário."""
    from telas import tela_perfil
    tools.fade_out(window, canvas, lambda: tela_perfil.criar_tela_perfil(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def criar_tela_menu_principal(window, canvas, usuario_logado):
    """
    Cria a interface gráfica do menu principal do usuário.
    Apresenta botões para navegar para as seções de adoção, tratamento, e feedback,
    além de um botão de doação. Também exibe um atalho textual para o perfil do usuário.
    """
    from telas import tela_perfil
    from telas import tela_lista_adocao
    from telas import tela_lista_tratamento 
    from telas import tela_feedback
    
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo do canvas.

    canvas.image_bg = PhotoImage( # Carrega a imagem de fundo do menu.
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        400.0,
        image=canvas.image_bg
    )

    canvas.button_feedback = PhotoImage( # Imagem do botão "Feedback".
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_1.png")
    )
    button_1 = Button( # Botão para a tela de Feedback.
        canvas,
        image=canvas.button_feedback,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_feedback(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão de Feedback.
        x=950.0,
        y=545.0,
        width=165.0,
        height=168.0
    )

    canvas.button_adocao = PhotoImage( # Imagem do botão "Adoção".
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_2.png")
    )
    button_2 = Button( # Botão para a lista de Adoção.
        canvas,
        image=canvas.button_adocao,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:transicao_para_lista_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_2.place( # Posiciona o botão de Adoção.
        x=160.0,
        y=545.0,
        width=165.0,
        height=168.0
    )

    canvas.button_tratamento = PhotoImage( # Imagem do botão "Tratamento".
        file=tools.relative_to_assets("TelaMenuPrincipal", "button_3.png")
    )
    button_3 = Button( # Botão para a lista de Tratamentos.
        canvas,
        image=canvas.button_tratamento,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_tratamento(window, canvas, usuario_logado),
        relief="flat"
    )
    button_3.place( # Posiciona o botão de Tratamento.
        x=562.0,
        y=545.0,
        width=164.0,
        height=168.0
    )
    
    canvas.button_image_4 = PhotoImage( # Imagem do botão "Doação".
    file=tools.relative_to_assets("TelaMenuPrincipal", "button_4.png")

    )
    button_voltar = Button( # Botão para a tela de Doação.
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_doacao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_voltar.place( # Posiciona o botão de Doação.
        x=1155.0,
        y=19.0,
        width=90.0,
        height=89.0
    )

    canvas.image_2 = PhotoImage( # Carrega imagem decorativa para a seção de feedback.
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_2.png")
    )
    canvas.create_image( # Exibe a imagem decorativa.
        1034.0,
        409.0,
        image=canvas.image_2
    )

    canvas.image_3 = PhotoImage( # Carrega imagem decorativa para a seção de adoção.
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_3.png")
    )
    canvas.create_image( # Exibe a imagem decorativa.
        242.2,
        410.0,
        image=canvas.image_3
    )

    canvas.image_4 = PhotoImage( # Carrega imagem decorativa para a seção de tratamento.
        file=tools.relative_to_assets("TelaMenuPrincipal", "image_4.png")
    )
    canvas.create_image( # Exibe a imagem decorativa.
        645.0,
        410.0,
        image=canvas.image_4
    )

    canvas.create_text( # Título principal da tela.
        576.0,
        25.0,
        anchor="nw",
        text="Menu",
        fill="#EED3B2",
        font=("Poppins Black", 45 * -1)
    )

    canvas.create_text( # Texto clicável que leva ao perfil do usuário.
        109.0,
        15.0,
        anchor="nw",
        text="Ver\nPerfil",
        fill="#44312D",
        font=("Poppins Black", 32 * -1),
        justify="left",
        tags=("ver_perfil_link",)
    )
    canvas.tag_bind( # Associa o evento de clique ao texto para chamar a função de transição para o perfil.
        "ver_perfil_link",
        "<Button-1>",
        lambda e: transicao_para_perfil(window, canvas, usuario_logado)
    )

    user_icon_filename = usuario_logado.get("icone", "button_3.png") # Obtém o nome do arquivo do ícone do usuário.
    clean_icon_filename = user_icon_filename.replace("button_", "icon_") # Ajusta o nome do arquivo para o padrão de ícone.
    
    icon_path = Path(__file__).parent / "perfil_icons" / clean_icon_filename # Constrói o caminho completo para o ícone.
    
    img = Image.open(icon_path) # Abre a imagem do ícone.
    max_size = (80, 80) # Define o tamanho máximo para o ícone.
    img.thumbnail(max_size) # Redimensiona a imagem.
    canvas.user_icon_image = ImageTk.PhotoImage(img) # Converte a imagem para um formato que o Tkinter pode usar.
    
    canvas.create_image( # Exibe o ícone de perfil do usuário.
        53.0,
        65.0,
        image=canvas.user_icon_image
    )