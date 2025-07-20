from tkinter import Button, PhotoImage, Text
from telas import tools


def transicao_para_menu_principal(window, canvas, usuario_logado):
    """Realiza a transição de volta para a tela do menu principal."""
    from telas import tela_menu_principal
    tools.fade_out(window, canvas, lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar.

def criar_tela_doacao(window, canvas, usuario_logado):
    """Cria a interface gráfica da tela de doação, com botões para diferentes métodos de doação."""
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo do canvas.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaDoacao", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaDoacao", "button_1.png")
    )
    button_1 = Button( # Botão para voltar ao menu principal.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_principal(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar".
        x=1159.9130859375,
        y=0.0,
        width=104.08695983886719,
        height=114.0
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão de opção 3 de doação.
        file=tools.relative_to_assets("TelaDoacao", "button_2.png")
    )
    button_2 = Button( # Botão para a terceira opção de doação.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"), # Ação de placeholder.
        relief="flat"
    )
    button_2.place( # Posiciona o botão.
        x=665.0,
        y=428.0,
        width=420.0,
        height=75.0
    )

    canvas.button_image_3 = PhotoImage( # Carrega a imagem do botão de opção 2 de doação.
        file=tools.relative_to_assets("TelaDoacao", "button_3.png")
    )
    button_3 = Button( # Botão para a segunda opção de doação.
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"), # Ação de placeholder.
        relief="flat"
    )
    button_3.place( # Posiciona o botão.
        x=665.0,
        y=275.0,
        width=420.0,
        height=75.0
    )

    canvas.button_image_4 = PhotoImage( # Carrega a imagem do botão de opção 1 de doação.
        file=tools.relative_to_assets("TelaDoacao", "button_4.png")
    )
    button_4 = Button( # Botão para a primeira opção de doação.
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"), # Ação de placeholder.
        relief="flat"
    )
    button_4.place( # Posiciona o botão.
        x=665.0,
        y=197.0,
        width=420.0,
        height=75.0
    )

    canvas.image_2 = PhotoImage( # Carrega o QR Code para doação.
        file=tools.relative_to_assets("TelaDoacao", "image_2.png")
    )
    canvas.create_image( # Exibe o QR Code na tela.
        874.0,
        594.0,
        image=canvas.image_2
    )

    canvas.image_3 = PhotoImage( # Carrega os textos(que são imagens) que explicam as opções de doação.
        file=tools.relative_to_assets("TelaDoacao", "image_3.png")
    )
    canvas.create_image(  # Exibe o texto explicativo na tela.
        874.0,
        252.0,
        image=canvas.image_3
    )