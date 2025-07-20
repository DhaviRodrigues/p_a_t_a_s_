from tkinter import Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_tela_perfil(window, canvas, usuario_logado):
    """Realiza a transição da tela de pedido do usuário de volta para a tela de perfil."""
    from telas import tela_perfil
    tools.fade_out(window, canvas, lambda: tela_perfil.criar_tela_perfil(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar

def criar_tela_pedido_usuario(window, canvas, usuario_logado):
    """
    Cria a interface gráfica que exibe o status do pedido de adoção do usuário.
    Carrega e exibe informações detalhadas do animal solicitado e o andamento do processo de adoção.
    """
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    from .modulos import pedidos
    from .modulos import animalcrud

    user_id = usuario_logado.get('id') # Pega o ID do usuário logado
    todos_pedidos = pedidos.carregar_dados('pedidos.json') # Carrega todos os pedidos de adoção
    todos_animais = animalcrud.carregar_dados("animais_adocao.json") # Carrega todos os dados dos animais

    id_animal_pedido = None # Inicializa o ID do animal do pedido como nulo
    
    animal_pedido = None # Inicializa a variável para os dados do animal

    for pedidos_adocao in todos_pedidos: # Itera sobre todos os pedidos para encontrar o que corresponde ao usuário logado.
        if pedidos_adocao.get('id_usuario') == user_id: # Se o ID do usuário no pedido corresponde ao usuário logado...
            id_animal_pedido = pedidos_adocao.get("id_animal") # Armazena o ID do animal
            status = pedidos_adocao.get("processo") # Armazena o status do processo de adoção

    if id_animal_pedido != None: # Se um pedido foi encontrado para o usuário...
        for animal in todos_animais: # Itera sobre a lista de animais
            if animal.get('id') == id_animal_pedido: # Para encontrar os dados do animal correspondente
                animal_pedido = animal # Armazena os dados do animal


    canvas.configure( # Configura a cor de fundo do canvas
        bg="#FFFFFF"
    )

    canvas.image_4 = PhotoImage( # Carrega a imagem de fundo da tela
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "image_4.png"
        )
    )
    canvas.create_image( # Exibe a imagem de fundo
        646.0,
        365.0,
        image=canvas.image_4
    )

    canvas.create_text( # Exibe o nome do animal
        322.0,
        103.0,
        anchor="nw",
        text=f"Nome: {animal_pedido.get('nome', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe a espécie do animal
        322.0,
        160.0,
        anchor="nw",
        text=f"Espécie: {animal_pedido.get('especie', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe o sexo do animal
        322.0,
        217.0,
        anchor="nw",
        text=f"Sexo: {animal_pedido.get('sexo', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Exibe a idade do animal
        322.0,
        271.0,
        anchor="nw",
        text=f"Idade: {animal_pedido.get('idade', '')}",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    canvas.create_text( # Título da seção de andamento da adoção
        110.0,
        343.0,
        anchor="nw",
        text= f"Andamento da adoção:",
        fill="#44312D",
        font=("Poppins Black", 30 * -1)
    )

    info_label = Label( # Cria um Label para exibir o status do processo
        canvas,
        text=f"{status}",
        font=("Poppins Black", 30 * -1),
        fg="#44312D",
        bg="#EED3B2", 
        wraplength=920, # Permite que o texto quebre a linha
        justify="left",
        anchor="nw"
    )
    info_label.place( # Posiciona o label com as informações do andamento
        x=120.0,
        y=400.0,
        width=920.0,
        height=250.0 
    )

    canvas.button_image_4 = PhotoImage( # Carrega a imagem do botão "Voltar"
        file=tools.relative_to_assets(
            "TelaInfoPet",
            "button_1.png"
        )
    )
    button_1 = Button( # Cria o botão para voltar à tela de perfil
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_tela_perfil(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Voltar"
        x=1142.0,
        y=16.0,
        width=126.0,
        height=138.0
    )

    placeholder_path = tools.relative_to_assets( # Define o caminho para a imagem placeholder
        "TelaInfoPet",
        "image_2.png"
    )
    placeholder_pil = Image.open(placeholder_path) # Abre a imagem placeholder
    largura_ref, altura_ref = placeholder_pil.size # Obtém as dimensões da imagem placeholder
    canvas.placeholder_tk = ImageTk.PhotoImage(placeholder_pil) # Converte para formato Tkinter

    canvas.create_image( # Exibe a imagem placeholder
        184.0,
        209.0,
        image=canvas.placeholder_tk
    )

    caminho_foto = Path(__file__).parent / "fotos_animais" / animal_pedido.get("foto", "") # Constrói o caminho para a foto real do animal
    if caminho_foto.exists(): # Verifica se o arquivo da foto existe
        placeholder_pil = Image.open(tools.relative_to_assets("TelaInfoPet", "image_2.png")) # Recarrega o placeholder para referência de tamanho
        largura_ref, altura_ref = placeholder_pil.size # Pega as dimensões de referência

        img = Image.open(caminho_foto) # Abre a foto do animal
        img_redimensionada = img.resize((largura_ref, altura_ref), Image.Resampling.LANCZOS) # Redimensiona a foto do animal para o tamanho do placeholder
        canvas.foto_animal_pedido_tk = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem redimensionada para o formato do Tkinter
        
        canvas.create_image( # Exibe a foto do animal sobre o placeholder
            184.0,
            209.0,
            image=canvas.foto_animal_pedido_tk
        )