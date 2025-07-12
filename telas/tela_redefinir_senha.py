from tkinter import Button, PhotoImage, Entry
from telas import tools
from telas import tela_login

def transicao_para_login(window, canvas):
    tools.fade_out(window, canvas, lambda: tela_login.criar_tela_login(window, canvas))

def tentar_redefinir_senha(entry_nova_senha,entry_confirma_senha, usuario,window,canvas):
    from .modulos import usercrud
    nova_senha = entry_nova_senha.get()
    confirma_senha = entry_confirma_senha.get()

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

    resultado = usercrud.Usuario.recuperar_senha(usuario, nova_senha)

    if resultado is True:
        tools.custom_messagebox(
            window,
            "Sucesso",
            "A sua senha foi redefinida com sucesso!\nPor favor, faça o login novamente."
        )
        transicao_para_login(window, canvas)
    # else:
    #     tools.custom_messagebox(window, "Erro", "Ocorreu um erro ao redefinir a senha.")


def criar_tela_redefinir_senha(window, canvas, email):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "image_1.png")
    )
    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "button_1.png")
    )
    entry_nova_senha = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )
    entry_nova_senha.place(
        x=293.0,
        y=268.0,
        width=694.0,
        height=56.0
    )

    entry_confirma_senha = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18),
        show="*"
    )
    entry_confirma_senha.place(
        x=293.0,
        y=396.0,
        width=694.0,
        height=56.0
    )
    
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_redefinir_senha(
            entry_nova_senha,
            entry_confirma_senha,
            email,
            window,
            canvas
        ),
        relief="flat"
    )
    button_1.place(
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.create_text(
        293.0,
        229.0,
        anchor="nw",
        text="Nova senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_login(window, canvas),
        relief="flat"
    )
    button_2.place(
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.create_text(
        360.0,
        154.0,
        anchor="nw",
        text="Redefinição de senha",
        fill="#44312D",
        font=("Poppins Black", 36 * -1)
    )

    canvas.entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "entry_1.png")
    )
    canvas.create_image(
        640.0,
        297.0,
        image=canvas.entry_image_1
    )

    canvas.create_text(
        293.0,
        357.0,
        anchor="nw",
        text="Confirmação de senha:",
        fill="#44302C",
        font=("Poppins Black", 24 * -1)
    )

    canvas.entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaRedefinirSenha", "entry_2.png")
    )
    canvas.create_image(
        640.0,
        425.0,
        image=canvas.entry_image_2
    )