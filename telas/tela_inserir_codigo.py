from tkinter import Button, PhotoImage, Entry
from telas import tools

def transicao_para_tela_inicial(window, canvas):
    """Realiza a transição para a tela inicial do programa."""
    from telas import tela_inicial
    tools.fade_out(window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas)) # Efeito de fade-out antes de transicionar.

def transicao_para_login(window, canvas):
    """Realiza a transição para a tela de login."""
    from telas import tela_login
    tools.fade_out(window, canvas, lambda: tela_login.criar_tela_login(window, canvas)) # Efeito de fade-out antes de transicionar.

def tentar_verificar_codigo(window, codigo, entry_codigo, pre_usuario, canvas, usuario):
    """
    Verifica se o código inserido pelo usuário corresponde ao código enviado por e-mail.
    Se o código estiver correto, finaliza o cadastro de um novo usuário ou
    redireciona um usuário existente para a tela de redefinição de senha.
    """
    from .modulos import usercrud
    from telas import tela_redefinir_senha

    if codigo == entry_codigo.strip(): # Compara o código esperado com o código digitado, removendo espaços extras.
        if not pre_usuario == {}: # Se houver dados de pré-usuário, significa que é um novo cadastro.
            nome = pre_usuario["nome"] # Extrai os dados do dicionário de pré-cadastro.
            email = pre_usuario["email"]
            senha = pre_usuario["senha"]
            user_icon = pre_usuario["icone"]

            usercrud.Usuario.criar_usuario(nome, email, senha, user_icon) # Chama a função para criar o usuário no banco de dados.
            tools.custom_messagebox(window, "Cadastro Bem-Sucedido", "Cadastro realizado com sucesso! Você será redirecionado para a tela de login.") # Exibe mensagem de sucesso.
            transicao_para_login(window, canvas) # Redireciona para a tela de login.

        elif pre_usuario == {}: # Se não houver dados de pré-usuário, significa que é uma recuperação de senha.
            tools.custom_messagebox(window, "Codigo Correto", "Iremos redirecionar você para a redefinição da sua senha.") # Exibe mensagem de sucesso.
            tools.fade_out(window,canvas,lambda: tela_redefinir_senha.criar_tela_redefinir_senha(window, canvas, usuario)) # Redireciona para a tela de redefinir senha.
    else: # Se o código estiver incorreto.
        tools.custom_messagebox(window, "Erro no cadastro", "O código está incorreto, verifique novamente") # Exibe mensagem de erro.


def criar_tela_inserir_codigo(window, canvas, pre_usuario, codigo, usuario):
    """
    Cria a interface gráfica para o usuário inserir o código de verificação
    enviado por e-mail, seja para concluir um cadastro ou para redefinir a senha.
    """
    print (f'Código: {codigo}') # Imprime o código no console para fins de depuração.
    print(f'Pré Usuario: {pre_usuario}') # Imprime os dados de pré-cadastro para depuração.
    print(f'Usuario: {usuario}') # Imprime os dados do usuário (se houver) para depuração.

    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure( # Define a cor de fundo do canvas.
        bg="#FFFFFF"
    )

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo da tela.
        file=tools.relative_to_assets("TelaInserirCodigo", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        360.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage( # Carrega a imagem do botão "Verificar".
        file=tools.relative_to_assets("TelaInserirCodigo", "button_1.png")
    )
    entry_codigo = Entry( # Cria o campo de entrada para o código.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 18)
    )
    entry_codigo.place( # Posiciona o campo de entrada.
        x=293.0,
        y=375.0,
        width=694.0,
        height=56.0
    )
    
    button_1 = Button( # Cria o botão "Verificar".
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_verificar_codigo(window, codigo, entry_codigo.get(), pre_usuario, canvas, usuario), # Define a ação do botão.
        relief="flat"
    )
    button_1.place( # Posiciona o botão.
        x=454.0,
        y=514.0,
        width=371.0,
        height=78.0
    )

    canvas.button_image_2 = PhotoImage( # Carrega a imagem do botão "Voltar".
        file=tools.relative_to_assets("TelaInserirCodigo", "button_2.png")
    )
    button_2 = Button( # Cria o botão "Voltar" para a tela inicial.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_tela_inicial(window, canvas),
        relief="flat"
    )
    button_2.place( # Posiciona o botão.
        x=1139.0,
        y=41.0,
        width=67.0,
        height=73.0
    )

    canvas.entry_image_1 = PhotoImage( # Carrega a imagem de fundo do campo de entrada.
        file=tools.relative_to_assets("TelaInserirCodigo", "entry_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo do campo de entrada.
        640.0,
        404.0,
        image=canvas.entry_image_1
    )