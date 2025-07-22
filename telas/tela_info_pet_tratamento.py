from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_lista_tratamento(window, canvas, usuario_logado):
    """Realiza a transição de volta para a tela de lista de animais em tratamento."""
    from telas import tela_lista_tratamento
    tools.fade_out(window, canvas, lambda: tela_lista_tratamento.criar_tela_lista_tratamento(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar.

def criar_tela_info_pet_tratamento(window, canvas, usuario_logado, animal_clicado):
    """
    Cria a interface gráfica para exibir informações detalhadas de um animal específico
    que está em tratamento, incluindo nome, espécie, sexo, idade, foto e outras informações.
    """
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure( # Define a cor de fundo do canvas.
        bg="#FFFFFF"
    )

    canvas.image_4 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "image_4.png"
        )
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0,
        365.0,
        image=canvas.image_4
    )

    canvas.create_text( # Exibe o nome do animal.
        322.0,
        103.0,
        anchor="nw",
        text=f"Nome: {animal_clicado.get('nome', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe a espécie do animal.
        322.0,
        160.0,
        anchor="nw",
        text=f"Espécie: {animal_clicado.get('especie', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe o sexo do animal.
        322.0,
        217.0,
        anchor="nw",
        text=f"Sexo: {animal_clicado.get('sexo', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe a idade do animal.
        322.0,
        271.0,
        anchor="nw",
        text=f"Idade: {animal_clicado.get('idade', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Título da seção "Outras informações".
        129.0,
        343.0,
        anchor="nw",
        text="Outras informações:",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    info_label = Label( # Cria um Label para exibir informações adicionais do animal.
        canvas,
        text=animal_clicado.get('informacoes', 'Nenhuma informação adicional.'),
        font=("Poppins", 15),
        fg="#44312D",
        bg="#EED3B2", 
        wraplength=920, # Define a largura máxima do texto antes de quebrar a linha.
        justify="left", # Alinha o texto à esquerda.
        anchor="nw"
    )
    info_label.place( # Posiciona o label de informações.
        x=120.0,
        y=400.0,
        width=920.0,
        height=250.0 
    )

    canvas.button_image_4 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_1.png"
        )
    )
    button_1 = Button( # Botão para voltar para a lista de animais em tratamento.
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_tratamento(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar".
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
    )

    placeholder_path = tools.relative_to_assets( # Define o caminho para a imagem placeholder.
        "TelaInfoPet",
        "image_2.png"
    )
    placeholder_pil = Image.open(placeholder_path) # Abre a imagem placeholder com a biblioteca Pillow.
    largura_ref, altura_ref = placeholder_pil.size # Obtém as dimensões da imagem para referência.
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil) # Converte a imagem para um formato que o Tkinter pode usar.

    canvas.create_image( # Exibe a imagem placeholder no canvas.
        184.0,
        209.0,
        image=canvas.placeholder_tk
    )

    caminho_foto = Path(__file__).parent / "fotos_animais" / animal_clicado.get("foto", "") # Constrói o caminho para a foto real do animal.
    if caminho_foto.exists(): # Verifica se o arquivo da foto existe no caminho especificado.
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPet", "image_2.png")) # Recarrega o placeholder para obter as dimensões de referência.
        largura_ref, altura_ref = placeholder_pil.size

        img = Image.open(caminho_foto) # Abre a imagem real do animal.
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS) # Redimensiona a imagem para o tamanho do placeholder.
        canvas.foto_animal_tk = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem redimensionada para o formato do Tkinter.
        
        canvas.create_image( # Exibe a foto do animal sobre a imagem placeholder.
            184.0,
            209.0,
            image=canvas.foto_animal_tk
        )