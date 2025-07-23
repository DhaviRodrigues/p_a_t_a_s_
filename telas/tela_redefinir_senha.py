from tkinter import Button, PhotoImage, Entry
from telas import tools
from telas import tela_login

def transicao_para_login(window, canvas):
    """Realiza a transição para a tela de login."""
    tools.fade_out(window, canvas, lambda: tela_login.criar_tela_login(window, canvas))


def tentar_redefinir_senha(entry_nova_senha,entry_confirma_senha, usuario,window,canvas):
    from .modulos import usercrud
    nova_senha = entry_nova_senha.get()
    confirma_senha = entry_confirma_senha.get()

#----------------------Verifica a senha da entrada----------------------
    if len(nova_senha) < 8:
        tools.custom_messagebox(window, "Erro na Redefinição", "A senha deve ter no mínimo 8 caracteres.")
        return

    elif len(nova_senha) > 16:
        tools.custom_messagebox(window, "Erro na Redefinição", "A senha deve ter no máximo 16 caracteres.")
        return
    
    elif not nova_senha or not confirma_senha:
        tools.custom_messagebox(window, "Erro na Redefinição", "Todos os campos devem ser preenchidos.")
        return
        
    elif nova_senha != confirma_senha:
        tools.custom_messagebox(window, "Erro na Redefinição", "As senhas não coincidem.")
        return
#------------------------------------------------------------------------

    resultado = usercrud.Usuario.recuperar_senha(usuario, nova_senha) # Tenta redefinir a senha do usuário.

    if resultado is True:
        tools.custom_messagebox(window, "Sucesso", "A sua senha foi redefinida com sucesso!\nPor favor, faça o login novamente.")
        transicao_para_login(window, canvas)


def criar_tela_redefinir_senha(window, canvas, email):
    """Cria a tela de redefinição de senha.
    O usuario preenche os campos de nova senha e confirmação de senha.
    Se as senhas coincidirem, a senha é redefinida e o usuário é redirecionado para a tela de login."""

    tools.limpar_tela(canvas) # Limpa a tela do canvas.
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "image_1.png"))

    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "button_1.png"))

    entry_nova_senha = Entry( #Cria o campo de entrada para a nova senha.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )

    entry_nova_senha.place( # Posiciona o campo de entrada para a nova senha.
        x=293.0,
        y=268.0,
        width=694.0,
        height=56.0
    )

    entry_confirma_senha = Entry( # Cria o campo de entrada para a confirmação da senha.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )

    entry_confirma_senha.place( # Posiciona o campo de entrada para a confirmação da senha.
        x=293.0,
        y=396.0,
        width=694.0,
        height=56.0
    )
    
    button_1 = Button( # Cria o botão para tentar redefinir a senha.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_redefinir_senha(entry_nova_senha, entry_confirma_senha, email, window, canvas),
        relief="flat"
    )

    button_1.place( # Posiciona o botão de redefinição de senha.
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text( # Cria o texto "Nova senha:" na tela.
        293.0,
        229.0,
        anchor="nw",
        text="Nova senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.create_text( # Cria o texto "(De 8 a 16 caracteres)" na tela.
        453.0,
        239.0,
        anchor="nw",
        text="(De 8 a 16 caracteres)",
        fill="#44302C",
        font=("Poppins Black", 16 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "button_2.png"))

    button_2 = Button( # Cria o botão para voltar à tela de login.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_login(window, canvas), # Redireciona para a tela de login.
        relief="flat"
    )
    button_2.place( # Posiciona o botão de voltar.
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text( # Cria o texto "Redefinição de senha" na tela.
        360.0,
        154.0,
        anchor="nw",
        text="Redefinição de senha",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "entry_1.png"))
    
    canvas.create_image(
        640.0,
        297.0,
        image=canvas.entry_image_1
    )

    canvas.create_text( # Cria o texto "Confirmação de senha:" na tela.
        293.0,
        357.0,
        anchor="nw",
        text="Confirmação de senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "entry_2.png"))
    
    canvas.create_image(
        640.0,
        425.0,
        image=canvas.entry_image_2
    )