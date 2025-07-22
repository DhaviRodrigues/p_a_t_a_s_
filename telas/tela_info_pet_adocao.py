from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools


def transicao_para_lista_adocao(window, canvas, usuario_logado):
    """Realiza a transição de volta para a tela de lista de animais para adoção."""
    from telas import tela_lista_adocao
    tools.fade_out(window, canvas, lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar.

def tentar_adotar(window, canvas, animal_clicado, usuario_logado):
    """
    Processa a tentativa de adoção de um animal. Verifica se o usuário ou o animal
    já estão em um processo de adoção. Se estiverem livres, pede confirmação e
    cria um novo pedido de adoção.
    """
    from .modulos import pedidos

    if usuario_logado.get('pedido', True): # Verifica se o usuário já tem um pedido ativo.
        tools.custom_messagebox( # Exibe mensagem de erro se o usuário já tiver um pedido.
            window,
            "Adoção Pendente",
            "Você já possui um pedido de adoção pendente.\n Para mais informações, veja seu perfil."
        )
    elif animal_clicado.get('processo_adoacao', True): # Verifica se o animal já está em processo de adoção.
        tools.custom_messagebox( # Exibe mensagem de erro se o animal já estiver sendo adotado.
            window,
            "Adoção Pendente",
            "Este animal já está em processo de adoção.\n Caso queira, adote outro animal."
        )
    else: # Se não houver impedimentos, prossegue com o pedido.
        resposta = tools.custom_yn( # Pede a confirmação do usuário em uma caixa de diálogo Sim/Não.
            window,
            "Confirmar Pedido de Adoção", 
            "Tem a certeza de que deseja adotar este animal?"
        )
        if resposta: # Se o usuário confirmar...

            pedidos.Pedidos.criar_pedido_adocao(animal_clicado, usuario_logado) # Chama a função para criar o pedido.
            if pedidos.Pedidos.criar_pedido_adocao: # Verifica se a função de criação foi executada (condição pode ser melhorada).
                tools.custom_messagebox( # Exibe mensagem de sucesso.
                    window,
                    "Pedido Enviado",
                    "O seu pedido de adoção foi enviado com sucesso!\nVeja mais informações no seu perfil."
                )
            else: # Caso ocorra um erro.
                tools.custom_messagebox( # Exibe mensagem de erro.
                    window,
                    "Erro",
                    "Ocorreu um erro ao enviar o pedido de adoção. Por favor, tente novamente mais tarde\n\n Peço que nos envie uma mensagem relatando o erro."
                )


def criar_tela_info_pet_adocao(window, canvas, usuario_logado, animal_clicado):
    """
    Cria a interface gráfica para exibir informações detalhadas de um animal
    disponível para adoção e oferece o botão para iniciar o processo de adoção.
    """
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure( # Define a cor de fundo do canvas.
        bg="#FFFFFF"
    )

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets(
            "TelaInfoPet",
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

    canvas.create_text( # Título da seção "Outras informações".
        129.0,
        343.0,
        anchor="nw",
        text="Outras informações:",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_1.png"
        )
    )
    button_1 = Button( # Botão para voltar para a lista de animais para adoção.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar".
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão "Adotar".
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_2.png"
        )
    )
    button_2 = Button( # Botão para iniciar a tentativa de adoção.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_adotar(window, canvas, animal_clicado, usuario_logado),
        relief="flat"
    )
    button_2.place( # Posiciona o botão "Adotar".
        x=1079.0,
        y=557.0,
        width=181.0,
        height=116.0
    )

    placeholder_path = tools.relative_to_assets( # Define o caminho para a imagem placeholder.
        "TelaInfoPet",
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

    caminho_foto = Path(__file__).parent / "fotos_animais" / animal_clicado.get("foto", "") # Constrói o caminho para a foto real do animal.
    if caminho_foto.exists(): # Verifica se o arquivo da foto existe.
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPet", "image_2.png")) # Recarrega o placeholder para referência de tamanho.
        largura_ref, altura_ref = placeholder_pil.size

        img = Image.open(caminho_foto) # Abre a imagem real do animal.
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS) # Redimensiona a imagem para o tamanho do placeholder.
        canvas.foto_animal_tk = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem redimensionada.
        
        canvas.create_image( # Exibe a foto do animal sobre a imagem placeholder.
            184.0,
            209.0,
            image=canvas.foto_animal_tk
        )