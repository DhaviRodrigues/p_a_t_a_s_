from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools


def transicao_para_menu_adm(window, canvas, usuario_logado):
    """Realiza a transição de volta para a tela de lista de animais para adoção."""
    from telas import tela_menu_adm
    tools.fade_out(window, canvas, lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar.


def criar_tela_info_pedido_recusado_aprovado(window, canvas, usuario_logado, pedido, nome_arquivo_foto):
    """
    Cria a interface gráfica para exibir informações detalhadas de um animal
    disponível para adoção e oferece o botão para iniciar o processo de adoção.
    """
    print (f"Pedido: {pedido}")  # Debug: imprime o pedido recebido

    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure( # Define a cor de fundo do canvas.
        bg="#FFFFFF"
    )

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets(
            "TelaInfoPedido",
            "image_1.png"
        )
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0,
        365.0,
        image=canvas.image_1
    )

    canvas.create_text( # Exibe o nome do animal.
        322.0,
        103.0,
        anchor="nw",
        text=f"Nome do pet: {pedido.get('nome_animal', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe o email do usuário.
        322.0,
        160.0,
        anchor="nw",
        text=f"Email do Usuário: {pedido.get('email_usuario', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe o nome do usuário.
        322.0,
        217.0,
        anchor="nw",
        text=f"Nome do usuário: {pedido.get('nome_usuario', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets(
            "TelaInfoPedido",
            "button_1.png"
        )
    )
    button_1 = Button( # Botão para voltar para a lista de animais para adoção.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_adm(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar".
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
    )

    placeholder_path = tools.relative_to_assets( # Define o caminho para a imagem placeholder.
        "TelaInfoPedido",
        "image_2.png"
    )
    placeholder_pil = Image.open(placeholder_path) # Abre a imagem placeholder.
    largura_ref, altura_ref = placeholder_pil.size # Obtém as dimensões da imagem para referência.
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil) # Converte a imagem para um formato que o Tkinter pode usar.

    canvas.create_image( # Exibe a imagem placeholder no canvas.
        184.0,
        209.0,
        image=canvas.placeholder_tk
    )

    caminho_foto = Path(__file__).parent / "fotos_animais" / nome_arquivo_foto # Constrói o caminho para a foto real do animal.
    if caminho_foto.exists(): # Verifica se o arquivo da foto existe.
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPedido", "image_2.png")) # Recarrega o placeholder para referência de tamanho.
        largura_ref, altura_ref = placeholder_pil.size

        img = Image.open(caminho_foto) # Abre a imagem real do animal.
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS) # Redimensiona a imagem para o tamanho do placeholder.
        canvas.foto_animal_tk = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem redimensionada.
        
        canvas.create_image( # Exibe a foto do animal sobre a imagem placeholder.
            184.0,
            209.0,
            image=canvas.foto_animal_tk
        )