from tkinter import Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
from telas import tools

def transicao_para_menu_principal(window, canvas, usuario_logado):
    """Realiza a transição da tela de perfil para o menu principal."""
    from telas import tela_menu_principal

    tools.fade_out( window,canvas,lambda: tela_menu_principal.criar_tela_menu_principal(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_editar_perfil(window, canvas, usuario_logado):
    """Realiza a transição da tela de perfil para editar perfil."""
    from telas import tela_editar_perfil
    print(f'Usuário Logado: {usuario_logado}') # Imprime o usuário logado para depuração.
    tools.fade_out( window,canvas,lambda: tela_editar_perfil.criar_tela_editar_perfil(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_logout(window, canvas):
    """Realiza o logout do usuário e retorna para a tela inicial."""
    from telas import tela_inicial

    tools.fade_out( window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas)) # Efeito de fade-out antes de transicionar


def verificar_pedido_adocao(window,canvas, usuario_logado):
    """Verifica se o usuário possui um pedido de adoção ativo e o 
    redireciona para a tela do pedido ou exibe uma mensagem de erro."""
    from .modulos import pedidos
    from telas import tela_pedido_usuario

    if usuario_logado.get("pedido") == False: # Verifica se o usuário não tem um pedido de adoção.
        tools.custom_messagebox(window, "Erro na visualização do pedido", "Você ainda não possui um pedido de adoção ativo.")

    else: # Caso tenha um pedido, transiciona para a tela de visualização do pedido.
        tools.fade_out(window, canvas, lambda: tela_pedido_usuario.criar_tela_pedido_usuario(window, canvas, usuario_logado,))


def criar_tela_perfil(window, canvas, usuario_logado,):
    """
    Cria a interface gráfica da tela de perfil do usuário.
    Exibe informações como nome, email, ID e ícone de perfil.
    Oferece opções para editar perfil, deletar conta, fazer logout, verificar pedidos e voltar ao menu principal.
    """
    from telas import tela_editar_perfil
    from .modulos import usercrud
    from telas import tela_pedido_usuario

    tools.limpar_tela(canvas) # Limpa os elementos atuais do canvas
    canvas.configure(bg="#FFFFFF") # Define o fundo como branco

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo
        file=tools.relative_to_assets("TelaPerfil", "image_1.png"))
    
    canvas.create_image( # Insere a imagem de fundo
        646.0,
        365.0,
        image=canvas.image_1
    )

    canvas.create_text( # Texto "Nome:"
        521.8,
        156.2,
        anchor="nw",
        text="Nome:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )
    
    nome_usuario = usuario_logado.get("nome", "") # Obtém o nome do usuário
    if len(nome_usuario) > 28: # Trunca o nome do usuário se for muito longo para exibição
        nome_perfil = nome_usuario[:28] + "..."
    else:
        nome_perfil = nome_usuario

    canvas.create_text( # Exibe o nome do usuário
        630.0,
        156.2,
        anchor="nw",
        text=nome_perfil,
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.create_text( # Texto "Email:"
        521.8,
        231.2,
        anchor="nw",
        text="Email:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )
    
    email_usuario = usuario_logado.get("email", "") # Obtém o email do usuário
    if len(email_usuario) > 28: # Trunca o email do usuário se for muito longo para exibição
        email_perfil = email_usuario[:28] + "..."
    else:
        email_perfil = email_usuario

    canvas.create_text( # Exibe o email do usuário
        630.0,
        231.2,
        anchor="nw",
        text=email_perfil,
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.create_text( # Texto "ID:"
        522.0,
        301.5,
        anchor="nw",
        text="ID:",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )

    canvas.create_text( # Exibe o ID do usuário
        580.0,
        301.5,
        anchor="nw",
        text=str(usuario_logado.get("id", "")),
        fill="#44312D",
        font=("Poppins", 32 * -1)
    )

    canvas.button_image_1 = PhotoImage( # Imagem do botão "Editar Perfil"
        file=tools.relative_to_assets("TelaPerfil", "button_1.png"))
    
    button_1 = Button( # Botão para editar o perfil
        canvas, 
        image=canvas.button_image_1, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: transicao_para_editar_perfil(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão de editar perfil
        x=701.0, 
        y=532.0, 
        width=181.0, 
        height=115.0
    )

    canvas.button_image_2 = PhotoImage( # Imagem do botão "Deletar Conta"
        file=tools.relative_to_assets("TelaPerfil", "button_2.png"))
    
    button_2 = Button( # Botão para deletar a conta
        canvas, 
        image=canvas.button_image_2, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: confirmar_e_deletar_conta(window, canvas, usuario_logado), 
        relief="flat"
    )
    button_2.place( # Posiciona o botão de deletar conta
        x=941.0, 
        y=533.0, 
        width=181.0, 
        height=115.0
    )

    canvas.button_image_3 = PhotoImage( # Imagem do botão "Logout"
        file=tools.relative_to_assets("TelaPerfil", "button_3.png"))
    
    button_3 = Button( # Botão para fazer logout
        canvas, 
        image=canvas.button_image_3, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: transicao_para_logout(window, canvas), 
        relief="flat"
    )
    button_3.place( # Posiciona o botão de logout
        x=461.0, 
        y=532.0, 
        width=181.0, 
        height=115.0
    )

    canvas.button_image_4 = PhotoImage( # Imagem do botão "Verificar Pedido"
        file=tools.relative_to_assets("TelaPerfil", "button_4.png"))
    
    button_4 = Button( # Botão para verificar o pedido de adoção
        canvas, 
        image=canvas.button_image_4, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: verificar_pedido_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_4.place( # Posiciona o botão de verificar pedido
        x=170.0, 
        y=535.0, 
        width=232.0, 
        height=113.0
    )

    canvas.button_image_5 = PhotoImage( # Imagem do botão "Voltar"
        file=tools.relative_to_assets("TelaPerfil", "button_5.png"))
    
    button_5 = Button( # Botão para voltar ao menu principal
        canvas, 
        image=canvas.button_image_5, 
        borderwidth=0, 
        highlightthickness=0,
        command=lambda: transicao_para_menu_principal(window, canvas, usuario_logado), 
        relief="flat"
    )
    button_5.place( # Posiciona o botão de voltar
        x=1122.5, 
        y=63.0, 
        width=109.4, 
        height=111.0
    )

    canvas.create_text( # Título da seção de configurações
        364.0,
        462.0,
        anchor="nw",
        text="CONFIGURAÇÕES DE USUÁRIO:",
        fill="#44312D",
        font=("Poppins Black", 35 * -1)
    )

    user_icon_filename = usuario_logado.get("icone", "button_3.png") # Obtém o nome do arquivo do ícone do usuário
    clean_icon_filename = user_icon_filename.replace("button_", "icon_") # Ajusta o nome do arquivo para o ícone de perfil
    
    icon_path = Path(__file__).parent / "perfil_icons" / clean_icon_filename # Constrói o caminho para o arquivo do ícone
    
    img = Image.open(icon_path) # Abre a imagem do ícone
    max_size = (257, 257) # Define o tamanho máximo do ícone
    img.thumbnail(max_size) # Redimensiona a imagem
    canvas.user_icon_image = ImageTk.PhotoImage(img) # Converte a imagem para um formato que o Tkinter pode usar
    
    canvas.create_image( # Exibe a imagem do ícone de perfil
        302.0,
        252.0,
        image=canvas.user_icon_image
    )

def confirmar_e_deletar_conta(window, canvas, usuario_logado):
    """Exibe uma caixa de diálogo para confirmar a exclusão da conta. Se confirmado, deleta a conta do usuário e o redireciona para a tela inicial."""
    from .modulos import usercrud
    resposta = tools.custom_yn( # Exibe uma caixa de diálogo de confirmação (Sim/Não)
        window,
        "Confirmar Exclusão", 
        "Tem a certeza de que deseja excluir a sua conta permanentemente? Esta ação não pode ser desfeita."
    )

    if resposta: # Se o usuário confirmar a exclusão
        sucesso = usercrud.Usuario.deletar_conta(usuario_logado) # Tenta deletar a conta do usuário
        if sucesso: # Se a exclusão for bem-sucedida
            tools.custom_messagebox( # Exibe mensagem de sucesso
                window, 
                "Conta Excluída", 
                "A sua conta foi excluída com sucesso. Será redirecionado para a tela inicial."
            )
            transicao_para_logout(window, canvas) # Redireciona para a tela inicial