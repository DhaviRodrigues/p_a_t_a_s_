from tkinter import Button, PhotoImage, Entry
from telas import tools

def transicao_para_inicial(window, canvas):
    """Realiza a transição da tela de login para a tela inicial."""

    from telas import tela_inicial
    tools.fade_out(window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas))


def transicao_para_redefinir_senha(window, canvas): 
    """Realiza a transição da tela de login para a tela de redefinição de senha."""

    from telas import tela_esqueceu_senha
    tools.fade_out(window, canvas, lambda: tela_esqueceu_senha.criar_tela_esqueceu_senha(window, canvas))

def tentar_login(window, canvas, email_entry, senha_entry):
    """
    Tenta realizar o login com os dados inseridos.
    Se for admin, redireciona para o menu admin.
    Se for usuário comum, redireciona para o menu principal.
    Caso contrário, mostra mensagem de erro.
    """
    from telas import tela_menu_adm
    from telas import tela_menu_principal
    from .modulos import usercrud

    email = email_entry.get()  # Obtém o e-mail digitado
    senha = senha_entry.get()  # Obtém a senha digitada

    resultado = usercrud.Usuario.fazer_login(email, senha)  # Verifica se o login é válido

    if isinstance(resultado, dict):  # Login bem-sucedido
        if resultado.get("adm") is True: #Se o usuário for admin
            tools.fade_out(window, canvas, lambda: tela_menu_adm.criar_tela_menu_adm(window, canvas, resultado))  # Vai para o menu admin
        else: # Se o usuário for nao for admin
            tools.fade_out(window, canvas, lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, resultado))  # Vai para o menu principal do usuário
    else:
        tools.custom_messagebox(window, "Erro de Login", resultado)  # Mostra mensagem de erro


def criar_tela_login(window, canvas):
    """
    Cria a interface gráfica da tela de login.
    Possui campos para email e senha, além de botões para logar, redefinir senha e voltar.
    """
    
    tools.limpar_tela(canvas)  # Limpa os elementos atuais do canvas
    canvas.configure(bg="#FFFFFF")  # Define fundo branco

    canvas.image_1 = PhotoImage(  # Carrega imagem de fundo
        file=tools.relative_to_assets("TelaLogin", "image_1.png")
    )
    canvas.create_image(  # Insere imagem de fundo
        640.0,
        360.0,
        image=canvas.image_1
    )

    entry_email = Entry(  # Campo de entrada para email
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_email.place(  # Posiciona campo de email
        x=293.0,
        y=308.0,
        width=694.0,
        height=56.0
    )

    entry_senha = Entry(  # Campo de entrada para senha
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )
    entry_senha.place(  # Posiciona campo de senha
        x=293.0,
        y=420.0,
        width=694.0,
        height=56.0
    )

    canvas.button_image_1 = PhotoImage(  # Imagem do botão "Login"
        file=tools.relative_to_assets("TelaLogin", "button_1.png")
    )
    button_1 = Button(  # Botão de login
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_login(
            window,
            canvas,
            entry_email,
            entry_senha
        ),
        relief="flat"
    )
    button_1.place(  # Posiciona botão de login
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text(  # Texto "Email:"
        293.0,
        269.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text(  # Texto "Senha:"
        293.0,
        381.0,
        anchor="nw",
        text="Senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.button_image_2 = PhotoImage(  # Imagem do botão "Voltar"
        file=tools.relative_to_assets("TelaLogin", "button_2.png")
    )
    button_2 = Button(  # Botão de voltar para tela inicial
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place(  # Posiciona botão de voltar
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text(  # Título da tela
        403.0,
        202.0,
        anchor="nw",
        text="Preencha as informações: ",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(  # Imagem de fundo do campo de email
        file=tools.relative_to_assets("TelaLogin", "entry_1.png")
    )
    canvas.create_image(
        640.0,
        337.0,
        image=canvas.entry_image_1
    )

    canvas.entry_image_2 = PhotoImage(  # Imagem de fundo do campo de senha
        file=tools.relative_to_assets("TelaLogin", "entry_2.png")
    )
    canvas.create_image(
        640.0,
        449.0,
        image=canvas.entry_image_2
    )

    canvas.button_image_3 = PhotoImage(  # Imagem do botão "Esqueceu a senha"
        file=tools.relative_to_assets("TelaLogin", "button_3.png")
    )
    button_3 = Button(  # Botão para redefinir senha
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_redefinir_senha(window, canvas),
        relief="flat"
    )
    button_3.place(  # Posiciona botão "Esqueceu a senha"
        x=463.0,
        y=592.0,
        width=343.0,
        height=43.0
    )
