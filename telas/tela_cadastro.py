from tkinter import Button, PhotoImage, Entry, messagebox
from .modulos import usercrud
from telas import tools

user_icon = None # Variável global para armazenar o nome do ícone selecionado.

def transicao_para_inicial(window, canvas):
    """Realiza a transição de volta para a tela inicial."""
    from telas import tela_inicial
    tools.fade_out(window,canvas,lambda: tela_inicial.criar_tela_inicial(window, canvas)) # Efeito de fade-out antes de transicionar.


def transicao_para_tela_inserir_codigo(window, canvas, pre_usuario, codigo):
    """Realiza a transição para a tela de inserção de código de verificação."""
    from telas import tela_inserir_codigo
    tools.fade_out(window,canvas,lambda: tela_inserir_codigo.criar_tela_inserir_codigo(window, canvas, pre_usuario, codigo)) # Efeito de fade-out antes de transicionar.


def selecionar_icone(canvas, x, y, nome_imagem_selecao, nome_icone):
    """
    Atualiza o ícone selecionado pelo usuário e exibe um feedback visual (uma imagem de seleção) sobre o ícone escolhido.
    """
    global user_icon # Informa que estamos usando a variável global.
    user_icon = nome_icone # Atualiza a variável global com o nome do arquivo do ícone.
    print(f"Ícone selecionado: {user_icon}") # Imprime o ícone selecionado para depuração.

    if hasattr(canvas, "selecao_atual_id"): # Verifica se já existe uma seleção anterior.
        canvas.delete(canvas.selecao_atual_id) # Apaga a imagem de seleção anterior.

    canvas.imagem_selecionada = PhotoImage( # Carrega a imagem que indica a seleção.
        file=tools.relative_to_assets("TelaCadastro", nome_imagem_selecao)
    )
    canvas.selecao_atual_id = canvas.create_image( # Desenha a nova imagem de seleção.
        x,
        y,
        image=canvas.imagem_selecionada
    )
    canvas.tag_raise(canvas.selecao_atual_id) # Garante que a imagem de seleção fique na frente.

def tentar_cadastro(entries,canvas,window,):
    """
    Valida os dados de cadastro inseridos. Se válidos, envia um e-mail de verificação
    e transiciona para a tela de inserção de código. Caso contrário, exibe uma mensagem de erro.
    """
    global user_icon # Informa que estamos usando a variável global.

    nome = entries['nome'].get() # Obtém o nome do campo de entrada.
    email = entries['email'].get() # Obtém o email do campo de entrada.
    senha = entries['senha'].get() # Obtém a senha do campo de entrada.
    confirma_senha = entries['confirma_senha'].get() # Obtém a confirmação de senha do campo.

    resultado = usercrud.Usuario.validar_usuario(nome, email, senha, confirma_senha, user_icon) # Valida todos os dados inseridos.

    pre_usuario= { # Cria um dicionário com os dados de pré-cadastro para uso posterior.
        "nome": nome,
        "email": email,
        "senha": senha,
        "icone": user_icon
    }

    if resultado is True: # Se a validação for bem-sucedida.
        codigo = usercrud.Usuario.gerar_codigo(email) # Gera e envia o código de verificação para o e-mail.
        tools.custom_messagebox(window,"Código Enviado",f"Um código de verificação foi enviado para {email}.") # Exibe mensagem de sucesso.
        transicao_para_tela_inserir_codigo(window, canvas, pre_usuario, codigo) # Transiciona para a tela de inserir o código.
        for entry in entries.values(): # Itera sobre todos os campos de entrada.
            entry.delete(0, 'end') # Limpa cada campo.
    else: # Se a validação falhar.
        tools.custom_messagebox(window,"Erro de Cadastro", resultado) # Exibe a mensagem de erro retornada pela validação.
        

def criar_tela_cadastro(window, canvas):
    """Cria a interface gráfica da tela de cadastro, com campos para os dados do novo usuário e uma grade de ícones selecionáveis."""
    
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#EADFC8") # Define a cor de fundo do canvas.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaCadastro", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        646.0373306274414,
        365.037353515625,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Cadastrar".
        file=tools.relative_to_assets("TelaCadastro", "button_1.png")
    )
    button_1 = Button( # Botão para tentar realizar o cadastro.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_cadastro(entries, canvas, window),
        relief="flat"
    )
    button_1.place( # Posiciona o botão "Cadastrar".
        x=649.0,
        y=588.0,
        width=371.0,
        height=78.0
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaCadastro", "button_2.png")
    )
    button_2 = Button( # Botão para voltar à tela inicial.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place( # Posiciona o botão "Voltar".
        x=1158.0,
        y=60.0,
        width=67.0,
        height=73.0
    )
    
    canvas.icon_images = [] # Lista para manter referência das imagens dos ícones e evitar que sejam apagadas.


#---------------------------- Criação dos ícones selecionáveis ----------------------------#
#------------------------------------------------------------------------------------------#

    icon_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_3.png")
    )
    canvas.icon_images.append(icon_image_3)
    canvas.create_image(
        155.0, 
        199.0, 
        image=icon_image_3, 
        tags=("icon_3",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_3",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 155.0, 199.0, "image_8.png", "button_3.png")
    )

    icon_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_4.png")
    )
    canvas.icon_images.append(icon_image_4)
    canvas.create_image(
        262.0, 
        199.0, 
        image=icon_image_4, 
        tags=("icon_4",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_4",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 262.0, 199.0, "image_5.png", "button_4.png")
    )

    icon_image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_5.png")
    )
    canvas.icon_images.append(icon_image_5)
    canvas.create_image(
        369.0, 
        198.0, 
        image=icon_image_5, 
        tags=("icon_5",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_5",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 369.0, 198.0, "image_7.png", "button_5.png")
    )

    icon_image_6 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_6.png")
    )
    canvas.icon_images.append(icon_image_6)
    canvas.create_image(
        155.0, 
        322.0, 
        image=icon_image_6, 
        tags=("icon_6",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_6",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 155.0, 322.0, "image_10.png", "button_6.png")
    )

    icon_image_7 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_7.png")
    )
    canvas.icon_images.append(icon_image_7)
    canvas.create_image(
        262.0, 
        322.0, 
        image=icon_image_7, 
        tags=("icon_7",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_7",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 262.0, 322.0, "image_9.png", "button_7.png")
    )

    icon_image_8 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_8.png")
    )
    canvas.icon_images.append(icon_image_8)
    canvas.create_image(
        370.0, 
        322.0, 
        image=icon_image_8, 
        tags=("icon_8",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_8",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 370.0, 322.0, "image_6.png", "button_8.png")
    )

    icon_image_9 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_9.png")
    )
    canvas.icon_images.append(icon_image_9)
    canvas.create_image(
        155.0, 
        452.0, 
        image=icon_image_9, 
        tags=("icon_9",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_9",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 155.0, 452.0, "image_3.png", "button_9.png")
    )

    icon_image_10 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_10.png")
    )
    canvas.icon_images.append(icon_image_10)
    canvas.create_image(
        261.0, 
        452.0, 
        image=icon_image_10, 
        tags=("icon_10",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_10",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 261.0, 452.0, "image_2.png", "button_10.png")
    )

    icon_image_11 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_11.png")
    )
    canvas.icon_images.append(icon_image_11)
    canvas.create_image(
        370.0, 
        451.0, 
        image=icon_image_11, 
        tags=("icon_11",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_11",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 370.0, 451.0, "image_4.png", "button_11.png")
    )

    icon_image_12 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_12.png")
    )
    canvas.icon_images.append(icon_image_12)
    canvas.create_image(
        155.0, 
        580.0, 
        image=icon_image_12, 
        tags=("icon_12",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_12",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 155.0, 580.0, "image_12.png", "button_12.png")
    )

    icon_image_13 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_13.png")
    )
    canvas.icon_images.append(icon_image_13)
    canvas.create_image(
        261.0, 
        580.0, 
        image=icon_image_13, 
        tags=("icon_13",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_13",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 261.0, 580.0, "image_11.png", "button_13.png")
    )

    icon_image_14 = PhotoImage(
        file=tools.relative_to_assets("TelaCadastro", "button_14.png")
    )
    canvas.icon_images.append(icon_image_14)
    canvas.create_image(
        370.0, 
        580.0, 
        image=icon_image_14, 
        tags=("icon_14",)
    )
    canvas.tag_bind( # Torna o ícone clicável.
        "icon_14",
        "<Button-1>",
        lambda e: selecionar_icone(canvas, 370.0, 580.0, "image_13.png", "button_14.png")
    )

#------------------------- Fim da criação dos ícones selecionáveis ------------------------#
#------------------------------------------------------------------------------------------#

    canvas.create_text( # Texto "Nome:".
        489.0,
        132.0,
        anchor="nw",
        text="Nome:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text( # Texto "Email:".
        489.0,
        248.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text( # Texto "Senha:".
        489.0,
        364.0,
        anchor="nw",
        text="Senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text( # Texto "Confirme sua senha:".
        489.0,
        475.0,
        anchor="nw",
        text="Confirme sua senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text( # Título da seção de ícones.
        153.0,
        76.0,
        anchor="nw",
        text="Escolha um ícone \n               de perfil ",
        fill="#EED3B2",
        font=("Poppins Black", 24 * -1)
    )
    
    canvas.create_text( # Título da seção de formulário.
        588.0,
        70.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    entry_nome = Entry( # Campo de entrada para o nome.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(window.font_poppins_regular, 18)
    )
    entry_nome.place(
        x=489.0,
        y=171.0,
        width=694.0,
        height=56.0
    )

    entry_email = Entry( # Campo de entrada para o email.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(window.font_poppins_regular, 18)
    )
    entry_email.place(
        x=489.0,
        y=287.0,
        width=694.0,
        height=56.0
    )

    entry_senha = Entry( # Campo de entrada para a senha.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(window.font_poppins_regular, 18),
        show="*" # Oculta os caracteres digitados.
    )
    entry_senha.place(
        x=489.0,
        y=403.0,
        width=694.0,
        height=56.0
    )

    entry_confirma_senha = Entry( # Campo de entrada para confirmar a senha.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=(window.font_poppins_regular, 18),
        show="*" # Oculta os caracteres digitados.
    )
    entry_confirma_senha.place(
        x=489.0,
        y=519.0,
        width=694.0,
        height=56.0
    )

    entries = { # Dicionário para criar o usuário depois.
        "nome": entry_nome,
        "email": entry_email,
        "senha": entry_senha,
        "confirma_senha": entry_confirma_senha
    }