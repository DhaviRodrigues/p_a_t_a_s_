from tkinter import Button, PhotoImage, Entry
from telas import tools
from telas import tela_login
import random

def transicao_para_login(window, canvas,):
    """Realiza a transição de volta para a tela de login."""
    tools.fade_out(window, canvas, lambda: tela_login.criar_tela_login(window, canvas,)) # Efeito de fade-out antes de transicionar.


def tentar_enviar_codigo(entry_email, window, canvas,):
    """
    Verifica o e-mail inserido para iniciar a recuperação de senha.
    Se o e-mail for válido e existir no sistema, um código de verificação é enviado
    e o usuário é redirecionado para a tela de inserção de código.
    """
    from telas import tela_inserir_codigo
    from .modulos import usercrud
   
    email = entry_email.get() # Obtém o e-mail do campo de entrada.
    usuario = usercrud.Usuario.email_existe(email) # Verifica se o e-mail está cadastrado.
    pre_usuario={} # Dicionário vazio, pois esta tela não lida com pré-cadastro.

    if not email: # Verifica se o campo de e-mail foi preenchido.
        tools.custom_messagebox(window,"Código Enviado","Preencha o campo do email.") # Exibe mensagem de erro.
    elif usuario: # Se o e-mail existir no sistema.
        codigo = usercrud.Usuario.gerar_codigo(email) # Gera e envia o código de verificação para o e-mail.
        tools.custom_messagebox(window,"Código Enviado",f"Um código de verificação foi enviado para {email}.") # Exibe mensagem de sucesso.
        tools.fade_out(window, canvas, lambda: tela_inserir_codigo.criar_tela_inserir_codigo(window, canvas, pre_usuario, codigo, usuario)) # Transiciona para a tela de inserir o código.
    else: # Se o e-mail não for encontrado.
        tools.custom_messagebox( # Exibe mensagem de erro.
            window,
            "Email não encontrado",
            "Não encontramos nenhum email cadastrado no P.A.T.A.S. que corresponda ao email inserido."
        )
        

def criar_tela_esqueceu_senha(window, canvas):
    """Cria a interface gráfica da tela 'Esqueceu a Senha', onde o usuário pode solicitar um código de redefinição."""
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo do canvas.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaEsqueceuSenha", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Enviar".
        file=tools.relative_to_assets("TelaEsqueceuSenha", "button_1.png")
    )
    button_enviar = Button( # Botão para enviar o e-mail de recuperação.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_enviar_codigo(entry_1, window, canvas),
        relief="flat"
    )
    button_enviar.place( # Posiciona o botão "Enviar".
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text( # Texto "Email:".
        293.0,
        336.0,
        anchor="nw",
        text="Email:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaEsqueceuSenha", "button_2.png")
    )
    button_voltar = Button( # Botão para voltar à tela de login.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_login(window, canvas),
        relief="flat"
    )
    button_voltar.place( # Posiciona o botão "Voltar".
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text( # Título da tela.
        440.0,
        140.0,
        anchor="nw",
        text="Redefinição de senha",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage( # Carrega a imagem de fundo para o campo de e-mail.
        file=tools.relative_to_assets("TelaEsqueceuSenha", "entry_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo do campo.
        640.0,
        404.0,
        image=canvas.entry_image_1
    )
    entry_1 = Entry( # Campo de entrada para o e-mail do usuário.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_1.place( # Posiciona o campo de e-mail.
        x=293.0,
        y=375.0,
        width=694.0,
        height=56.0
    )