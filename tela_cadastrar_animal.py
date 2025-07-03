from tkinter import Button, PhotoImage, Entry, Text, filedialog
from pathlib import Path
from PIL import Image, ImageTk
import tools
import tela_menu_adm
from modulos import animalcrud

sexo_selecionado = None
tipo_cadastro_selecionado = None
caminho_imagem_animal = None

def transicao_para_menu_adm(window, canvas, usuario_logado):
    tools.fade_out(
        window,
        canvas,
        lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, usuario_logado)
    )

def selecionar_imagem_animal(canvas):
    global caminho_imagem_animal
    
    caminho_imagem_animal = filedialog.askopenfilename(
        title="Selecione a imagem do animal",
        filetypes=[("Ficheiros de Imagem", "*.png *.jpg *.jpeg")]
    )

    if not caminho_imagem_animal:
        return

    imagem_referencia = Image.open(tools.relative_to_assets("TelaCadastrarAnimal", "image_7.png"))
    largura_referencia, altura_referencia = imagem_referencia.size

    img = Image.open(caminho_imagem_animal)
    img_redimensionada = img.resize((largura_referencia, altura_referencia))

    canvas.imagem_preview_animal = ImageTk.PhotoImage(img_redimensionada)

    if hasattr(canvas, "preview_id"):
        canvas.delete(canvas.preview_id)
    if hasattr(canvas, "image_7_id"):
        canvas.delete(canvas.image_7_id)

    canvas.preview_id = canvas.create_image(
        146.0,
        468.0,
        image=canvas.imagem_preview_animal
    )
    canvas.tag_raise(canvas.preview_id)

def selecionar_sexo(canvas, x, y, imagem_selecao, valor):
    global sexo_selecionado
    sexo_selecionado = valor

    if hasattr(canvas, "selecao_sexo_id"):
        canvas.delete(canvas.selecao_sexo_id)

    canvas.imagem_selecao_sexo = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", imagem_selecao)
    )
    canvas.selecao_sexo_id = canvas.create_image(
        x,
        y,
        image=canvas.imagem_selecao_sexo
    )

def selecionar_tipo_cadastro(canvas, x, y, imagem_selecao, valor):
    global tipo_cadastro_selecionado
    tipo_cadastro_selecionado = valor
    
    if hasattr(canvas, "selecao_tipo_id"):
        canvas.delete(canvas.selecao_tipo_id)

    canvas.imagem_selecao_tipo = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", imagem_selecao)
    )
    canvas.selecao_tipo_id = canvas.create_image(
        x,
        y,
        image=canvas.imagem_selecao_tipo
    )

def tentar_cadastrar_animal(entries, window, canvas):
    nome = entries["nome"].get()
    idade = entries["idade"].get()
    info = entries["info"].get("1.0", "end-1c")
    especie = "Não especificado"

    resultado_validacao = animalcrud.Animal.validar_animal(
        nome,
        especie,
        sexo_selecionado,
        idade,
        caminho_imagem_animal
    )

    if resultado_validacao is not True:
        tools.custom_messagebox(window, "Erro de Validação", resultado_validacao)
        return

    if tipo_cadastro_selecionado is None:
        tools.custom_messagebox(window, "Erro de Validação", "Selecione o tipo de cadastro (Tratamento ou Adoção).")
        return

    animalcrud.Animal.criar_animal(
        nome, 
        especie, 
        sexo_selecionado, 
        idade, 
        info, 
        tipo_cadastro_selecionado,
        caminho_imagem_animal
    )

    tools.custom_messagebox(window, "Sucesso", "Animal cadastrado com sucesso!")

    for widget in entries.values():
        if isinstance(widget, Entry):
            widget.delete(0, 'end')
        elif isinstance(widget, Text):
            widget.delete("1.0", 'end')

    if hasattr(canvas, "selecao_sexo_id"):
        canvas.delete(canvas.selecao_sexo_id)
    if hasattr(canvas, "selecao_tipo_id"):
        canvas.delete(canvas.selecao_tipo_id)
    if hasattr(canvas, "preview_id"):
        canvas.delete(canvas.preview_id)

def criar_tela_cadastrar_animal(window, canvas, usuario_logado):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_1.png")
    )
    canvas.create_image(
        646.0,
        365.0,
        image=canvas.image_1
    )

    entry_nome = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_nome.place(
        x=254.0,
        y=176.0,
        width=333.0,
        height=56.0
    )

    entry_idade = Entry(
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

    text_info = Text(
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

    entries = {
        "nome": entry_nome,
        "idade": entry_idade,
        "info": text_info
    }

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_1.png")
    )
    button_cadastrar = Button(
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

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_2.png")
    )
    button_inserir_imagem = Button(
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
    
    canvas.image_6 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_6.png")
    )
    canvas.create_image(
        146.0,
        467.0,
        image=canvas.image_6
    )

    canvas.image_7_img = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "image_7.png")
    )
    canvas.image_7_id = canvas.create_image(
        146.0,
        468.0,
        image=canvas.image_7_img
    )

    canvas.button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastrarAnimal", "button_3.png")
    )
    button_voltar = Button(
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_menu_adm(window, canvas, usuario_logado),
        relief="flat"
    )
    button_voltar.place(
        x=93.0,
        y=74.0,
        width=106.7,
        height=102.0
    )

    canvas.button_image_macho = PhotoImage(
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

    canvas.button_image_femea = PhotoImage(
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

    canvas.button_image_adocao = PhotoImage(
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

    canvas.button_image_tratamento = PhotoImage(
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

    canvas.create_text(
        254.0,
        150.0,
        anchor="nw",
        text="Nome do animal:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text(
        254.0,
        276.0,
        anchor="nw",
        text="Outras informações e características:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text(
        623.0,
        150.0,
        anchor="nw",
        text="Idade:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text(
        691.0,
        160.0,
        anchor="nw",
        text="ex(8meses/2anos)",
        fill="#44302C",
        font=("Poppins ExtraLight", 10 * -1)
    )

    canvas.create_text(
        391.0,
        83.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.create_text(
        880.0,
        150.0,
        anchor="nw",
        text="Sexo:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )

    canvas.create_text(
        1015.0,
        150.0,
        anchor="nw",
        text="Animal / Tratamento:",
        fill="#44302C",
        font=("Poppins Black", 20 * -1)
    )