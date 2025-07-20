from tkinter import Button, PhotoImage, Entry, Text, filedialog
from pathlib import Path
from PIL import Image, ImageTk
from .modulos import animalcrud
from telas import tools

sexo_selecionado = None # Variável global para guardar o sexo selecionado (M/F).
tipo_cadastro_selecionado = None # Variável global para guardar o tipo de cadastro (adoção/tratamento).
caminho_imagem_animal = None # Variável global para guardar o caminho da imagem selecionada.

def transicao_para_menu_adm(window, canvas, usuario_logado):
    """Realiza a transição de volta para a tela do menu de administrador."""
    from telas import tela_menu_adm
    tools.fade_out( window,canvas,lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, usuario_logado))

def selecionar_imagem_animal(canvas):
    """Abre uma janela para o usuário selecionar um arquivo de imagem e exibe um preview na tela."""
    global caminho_imagem_animal # Informa que estamos usando a variável global.
    
    caminho_imagem_animal = filedialog.askopenfilename( # Abre a janela de seleção de arquivo.
        title="Selecione a imagem do animal",
        filetypes=[("Ficheiros de Imagem", "*.png *.jpg *.jpeg")]
    )

    if not caminho_imagem_animal: # Se o usuário cancelar a seleção, a função termina.
        return

    imagem_referencia = Image.open(tools.relative_to_assets("TelaCadastrarAnimal", "image_7.png")) # Abre uma imagem de referência para obter o tamanho do preview.
    largura_referencia, altura_referencia = imagem_referencia.size # Pega as dimensões da imagem de referência.

    img = Image.open(caminho_imagem_animal) # Abre a imagem selecionada pelo usuário.
    img_redimensionada = img.resize((largura_referencia, altura_referencia)) # Redimensiona a imagem para o tamanho do preview.

    canvas.imagem_preview_animal = ImageTk.PhotoImage(img_redimensionada) # Converte a imagem para um formato que o Tkinter pode usar.

    if hasattr(canvas, "preview_id"): # Se já existir um preview anterior,
        canvas.delete(canvas.preview_id) # ele é apagado.
    if hasattr(canvas, "image_7_id"): # Apaga a imagem de placeholder inicial.
        canvas.delete(canvas.image_7_id)

    canvas.preview_id = canvas.create_image( # Exibe a nova imagem de preview no canvas.
        146.0,
        468.0,
        image=canvas.imagem_preview_animal
    )
    canvas.tag_raise(canvas.preview_id) # Garante que o preview fique na frente de outros elementos.

def selecionar_sexo(canvas, x, y, imagem_selecao, valor):
    """Atualiza a variável global de sexo e exibe um feedback visual de seleção na tela."""
    global sexo_selecionado # Informa que estamos usando a variável global.
    sexo_selecionado = valor # Atualiza a variável com o sexo selecionado ('M' ou 'F').

    if hasattr(canvas, "selecao_sexo_id"): # Se uma seleção de sexo já existir,
        canvas.delete(canvas.selecao_sexo_id) # ela é apagada.

    canvas.imagem_selecao_sexo = PhotoImage( # Carrega a imagem que indica a seleção.
        file=tools.relative_to_assets("TelaCadastrarAnimal", imagem_selecao)
    )
    canvas.selecao_sexo_id = canvas.create_image( # Desenha a imagem de seleção na posição do botão clicado.
        x,
        y,
        image=canvas.imagem_selecao_sexo
    )

def selecionar_tipo_cadastro(canvas, x, y, imagem_selecao, valor):
    """Atualiza a variável global de tipo de cadastro e exibe um feedback visual."""
    global tipo_cadastro_selecionado # Informa que estamos usando a variável global.
    tipo_cadastro_selecionado = valor # Atualiza a variável com o tipo selecionado.
    
    if hasattr(canvas, "selecao_tipo_id"): # Se uma seleção de tipo já existir,
        canvas.delete(canvas.selecao_tipo_id) # ela é apagada.

    canvas.imagem_selecao_tipo = PhotoImage( # Carrega a imagem que indica a seleção.
        file=tools.relative_to_assets("TelaCadastrarAnimal", imagem_selecao)
    )
    canvas.selecao_tipo_id = canvas.create_image( # Desenha a imagem de seleção na posição do botão clicado.
        x,
        y,
        image=canvas.imagem_selecao_tipo
    )

def tentar_cadastrar_animal(entries, window, canvas):
    """Valida os dados do formulário e, se corretos, cria um novo registro de animal e limpa a tela."""
    
    nome = entries["nome"].get() # Pega o nome do campo de entrada.
    idade = entries["idade"].get() # Pega a idade do campo de entrada.
    info = entries["info"].get("1.0", "end-1c") # Pega as informações do campo de texto.
    especie = entries["especie"].get() # Pega a espécie do campo de entrada.

    resultado_validacao = animalcrud.Animal.validar_animal( # Valida os dados inseridos.
        nome,
        especie,
        sexo_selecionado,
        idade,
        caminho_imagem_animal
    )

    if resultado_validacao is not True: # Se a validação falhar,
        tools.custom_messagebox(window, "Erro de Validação", resultado_validacao) # exibe uma mensagem de erro.
        return # e interrompe a função.

    if tipo_cadastro_selecionado is None: # Verifica se o tipo de cadastro foi selecionado.
        tools.custom_messagebox(window, "Erro de Validação", "Selecione o tipo de cadastro (Tratamento ou Adoção).")
        return

    animalcrud.Animal.criar_animal( # Chama a função para criar o novo animal no banco de dados.
        nome, 
        especie, 
        sexo_selecionado, 
        idade, 
        info, 
        tipo_cadastro_selecionado,
        caminho_imagem_animal
    )

    tools.custom_messagebox(window, "Sucesso", "Animal cadastrado com sucesso!") # Exibe mensagem de sucesso.

    for widget in entries.values(): # Itera sobre todos os campos do formulário.
        if isinstance(widget, Entry): # Se for um campo de entrada de linha única,
            widget.delete(0, 'end') # apaga o conteúdo.
        elif isinstance(widget, Text): # Se for um campo de texto de múltiplas linhas,
            widget.delete("1.0", 'end') # apaga o conteúdo.

    if hasattr(canvas, "selecao_sexo_id"): # Remove os feedbacks visuais de seleção.
        canvas.delete(canvas.selecao_sexo_id)
    if hasattr(canvas, "selecao_tipo_id"):
        canvas.delete(canvas.selecao_tipo_id)
    if hasattr(canvas, "preview_id"):
        canvas.delete(canvas.preview_id)

def criar_tela_cadastrar_animal(window, canvas, usuario_logado):
    """Cria a interface gráfica para cadastrar um novo animal no sistema."""
    
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0,
        365.0,
        image=canvas.image_1
    )

    entry_nome = Entry( # Campo de entrada para o nome.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_nome.place(
        x=70.0,
        y=176.0,
        width=270.0,
        height=56.0
    )
    entry_especie = Entry( # Campo de entrada para a espécie.
        canvas, 
        bd=0, 
        bg="#FFFFFF", 
        fg="#000716",
        highlightthickness=0, 
        font=("Poppins", 18)
    )
    entry_especie.place(
        x=380.0, 
        y=176.0, 
        width=200.0, 
        height=56.0
    )
    
    entry_idade = Entry( # Campo de entrada para a idade.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_idade.place(
        x=623.0,
        y=176.0,
        width=167.0,
        height=56.0
    )

    text_info = Text( # Campo de texto para outras informações.
        canvas,
        bd=0,
        bg="#EED3B2",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 14)
    )
    text_info.place(
        x=259.0,
        y=312.0,
        width=958.0,
        height=248.0
    )

    entries = { # Dicionário para agrupar os campos de entrada e facilitar o acesso.
        "nome": entry_nome,
        "idade": entry_idade,
        "info": text_info,
        "especie": entry_especie
    }

    canvas.button_image_1 = PhotoImage( # Carrega imagem do botão "Cadastrar".
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_1.png")
    )
    button_cadastrar = Button( # Botão para tentar cadastrar o animal.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_cadastrar_animal(entries, window, canvas),
        relief="flat"
    )
    button_cadastrar.place(
        x=521.0,
        y=581.0,
        width=371.0,
        height=78.0
    )

    canvas.button_image_2 = PhotoImage( # Carrega imagem do botão "Inserir Imagem".
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_2.png")
    )
    button_inserir_imagem = Button( # Botão para abrir a seleção de imagem.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selecionar_imagem_animal(canvas),
        relief="flat"
    )
    button_inserir_imagem.place(
        x=52.0,
        y=326.0,
        width=187.875,
        height=36.0
    )
    
    canvas.image_6 = PhotoImage( # Carrega a borda do preview da imagem.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_6.png")
    )
    canvas.create_image( # Exibe a borda.
        146.0,
        467.0,
        image=canvas.image_6
    )

    canvas.image_7_img = PhotoImage( # Carrega o placeholder do preview.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_7.png")
    )
    canvas.image_7_id = canvas.create_image( # Exibe o placeholder.
        146.0,
        468.0,
        image=canvas.image_7_img
    )

    canvas.button_image_3 = PhotoImage( # Carrega imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_3.png")
    )
    button_voltar = Button( # Botão para voltar ao menu adm.
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_adm(window, canvas, usuario_logado),
        relief="flat"
    )
    button_voltar.place(
        x=93.0,
        y=50.0,
        width=106.7,
        height=102.0
    )

    canvas.button_image_macho = PhotoImage( # Carrega o botão para selecionar 'Macho'.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_5.png")
    )
    button_macho = Button(
        canvas,
        image=canvas.button_image_macho,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selecionar_sexo(canvas, 865.0, 206.0, "image_2.png", "M"),
        relief="flat"
    )
    button_macho.place(
        x=829.0,
        y=181.0,
        width=73.0,
        height=51.0
    )

    canvas.button_image_femea = PhotoImage( # Carrega o botão para selecionar 'Fêmea'.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_4.png")
    )
    button_femea = Button(
        canvas,
        image=canvas.button_image_femea,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selecionar_sexo(canvas, 955.0, 206.0, "image_3.png", "F"),
        relief="flat"
    )
    button_femea.place(
        x=919.0,
        y=181.0,
        width=73.0,
        height=51.0
    )

    canvas.button_image_adocao = PhotoImage( # Carrega o botão para selecionar 'Adoção'.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_6.png")
    )
    button_adocao = Button(
        canvas,
        image=canvas.button_image_adocao,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selecionar_tipo_cadastro(canvas, 1087.0, 206.0, "image_5.png", "adocao"),
        relief="flat"
    )
    button_adocao.place(
        x=1051.0,
        y=181.0,
        width=73.0,
        height=51.0
    )

    canvas.button_image_tratamento = PhotoImage( # Carrega o botão para selecionar 'Tratamento'.
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_7.png")
    )
    button_tratamento = Button(
        canvas,
        image=canvas.button_image_tratamento,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selecionar_tipo_cadastro(canvas, 1170.0, 206.0, "image_4.png", "tratamento"),
        relief="flat"
    )
    button_tratamento.place(
        x=1134.0,
        y=181.0,
        width=73.0,
        height=51.0
    )

    canvas.create_text( # Rótulo do campo "Nome".
        70.0,
        150.0,
        anchor="nw",
        text="Nome do animal:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )
    canvas.create_text( # Rótulo do campo "Espécie".
        380.0, 
        150.0, 
        anchor="nw", 
        text="Espécie:",
        fill="#44302C", 
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text( # Rótulo do campo "Outras informações".
        254.0,
        276.0,
        anchor="nw",
        text="Outras informações e características:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text( # Rótulo do campo "Idade".
        623.0,
        150.0,
        anchor="nw",
        text="Idade:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text( # Texto de exemplo para o campo "Idade".
        691.0,
        160.0,
        anchor="nw",
        text="ex(8meses/2anos)",
        fill="#44302C",
        font=("Poppins Black", 12 * -1)
    )

    canvas.create_text( # Título da tela.
        391.0,
        50.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.create_text( # Rótulo da seleção "Sexo".
        880.0,
        150.0,
        anchor="nw",
        text="Sexo:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text( # Rótulo da seleção "Tipo de Cadastro".
        1015.0,
        150.0,
        anchor="nw",
        text="Adoção / Tratamento:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )