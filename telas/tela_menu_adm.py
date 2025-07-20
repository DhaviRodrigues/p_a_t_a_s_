from tkinter import Button, PhotoImage, Entry
from telas import tools

def transicao_para_inicial(window, canvas):
    """Realiza a transição do menu de administrador para a tela inicial (logout)."""
    from telas import tela_inicial
    tools.fade_out(window,canvas,lambda: tela_inicial.criar_tela_inicial(window, canvas)) # Efeito de fade-out antes de transicionar


def transicao_para_cadastrar_animal(window, canvas, usuario_logado):
    """Realiza a transição para a tela de cadastro de animal."""
    from telas import tela_cadastrar_animal
    tools.fade_out(window,canvas,lambda: tela_cadastrar_animal.criar_tela_cadastrar_animal(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_pedidos_pendente(window, canvas, usuario_logado):
    """Realiza a transição para a tela com a lista de pedidos de adoção pendentes."""
    from telas import tela_lista_pedidos_pendente
    tools.fade_out(window,canvas, lambda: tela_lista_pedidos_pendente.criar_tela_lista_pedidos_pendente(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_pedidos_recusado(window, canvas, usuario_logado):
    """Realiza a transição para a tela com a lista de pedidos de adoção recusados."""
    from telas import tela_lista_pedidos_recusado
    tools.fade_out(window,canvas,lambda: tela_lista_pedidos_recusado.criar_tela_lista_pedidos_recusado(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_pedidos_aprovado(window, canvas, usuario_logado):
    """Realiza a transição para a tela com a lista de pedidos de adoção aprovados."""
    from telas import tela_lista_pedidos_aprovado
    tools.fade_out(window,canvas,lambda: tela_lista_pedidos_aprovado.criar_tela_lista_pedidos_aprovado(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_adocao(window, canvas, usuario_logado):
    """Realiza a transição para a tela de lista de animais para adoção."""
    from telas import tela_lista_adocao
    tools.fade_out(window,canvas,lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar


def transicao_para_lista_tratamento(window, canvas, usuario_logado):
    """Realiza a transição para a tela de lista de animais em tratamento."""
    from telas import tela_lista_tratamento
    tools.fade_out(window,canvas,lambda: tela_lista_tratamento.criar_tela_lista_tratamento(window, canvas, usuario_logado)) # Efeito de fade-out antes de transicionar

def tentar_alterar_status_adm(entry_widget, novo_status, window):
    """Tenta alterar o status de administrador de um usuário com base no e-mail fornecido. Exibe uma mensagem de sucesso ou erro e limpa o campo de entrada."""
    from .modulos import usercrud

    print (f"{entry_widget.get()}")

    email = entry_widget.get() # Obtém o email do campo de entrada
    resultado = usercrud.Usuario.alterar_status_adm(email, novo_status) # Chama a função para alterar o status

    if "sucesso" in resultado: # Se a operação foi bem-sucedida
        tools.custom_messagebox(window, "Operação Concluída", resultado) # Mostra mensagem de sucesso
    else: # Caso contrário
        tools.custom_messagebox(window, "Erro", resultado) # Mostra mensagem de erro
    
    entry_widget.delete(0, 'end') # Limpa o campo de entrada


def criar_tela_menu_adm(window, canvas, usuario_logado):
    """
    Cria a interface gráfica do menu de administrador.
    Oferece funcionalidades como cadastrar animais, gerenciar pedidos de adoção,
    visualizar listas de animais e gerenciar permissões de outros administradores.
    """
    
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#FFFFFF") # Define a cor de fundo do canvas.

    canvas.image_1 = PhotoImage( # Carrega a imagem de fundo do menu de administrador.
        file=tools.relative_to_assets("TelaMenuAdm", "image_1.png")
    )
    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        423.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage( # Imagem do botão "Cadastrar Animal".
        file=tools.relative_to_assets("TelaMenuAdm", "button_1.png")
    )
    button_1 = Button( # Botão para cadastrar um novo animal.
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_cadastrar_animal(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place( # Posiciona o botão.
        x=98.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.image_2 = PhotoImage( # Carrega imagem decorativa da seção "Cadastrar Animal".
        file=tools.relative_to_assets("TelaMenuAdm", "image_2.png")
    )
    canvas.create_image( # Exibe a imagem decorativa.
        163.0,
        455.0,
        image=canvas.image_2
    )

    canvas.button_image_2 = PhotoImage( # Imagem do botão "Logout".
        file=tools.relative_to_assets("TelaMenuAdm", "button_2.png")
    )
    button_2 = Button( # Botão para fazer logout e voltar à tela inicial.
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place( # Posiciona o botão.
        x=1133.0,
        y=29.0,
        width=106.74418640136719,
        height=102.0
    )

    canvas.button_image_3 = PhotoImage( # Imagem do botão "Remover ADM".
        file=tools.relative_to_assets("TelaMenuAdm", "button_3.png")
    )
    button_3 = Button( # Botão para revogar permissão de administrador.
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_alterar_status_adm(entry_adicionar_adm, True, window),
        relief="flat"
    )
    button_3.place( # Posiciona o botão.
        x=1032.0,
        y=432.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_4 = PhotoImage( # Imagem do botão "Pedidos Pendentes".
        file=tools.relative_to_assets("TelaMenuAdm", "button_4.png")
    )
    button_4 = Button( # Botão para ver a lista de pedidos pendentes.
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_pedidos_pendente(window, canvas, usuario_logado),
        relief="flat"
    )
    button_4.place( # Posiciona o botão.
        x=725.0,
        y=393.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_5 = PhotoImage( # Imagem do botão "Pedidos Recusados".
        file=tools.relative_to_assets("TelaMenuAdm", "button_5.png")
    )
    button_5 = Button( # Botão para ver a lista de pedidos recusados.
        canvas,
        image=canvas.button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_pedidos_recusado(window, canvas, usuario_logado),
        relief="flat"
    )
    button_5.place( # Posiciona o botão.
        x=725.0,
        y=479.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_6 = PhotoImage( # Imagem do botão "Pedidos Aprovados".
        file=tools.relative_to_assets("TelaMenuAdm", "button_6.png")
    )
    button_6 = Button( # Botão para ver a lista de pedidos aprovados.
        canvas,
        image=canvas.button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_pedidos_aprovado(window, canvas, usuario_logado),
        relief="flat"
    )
    button_6.place( # Posiciona o botão.
        x=714.0,
        y=565.0,
        width=167.0,
        height=48.0
    )

    canvas.button_image_7 = PhotoImage( # Imagem do botão "Lista Adoção".
        file=tools.relative_to_assets("TelaMenuAdm", "button_7.png")
    )
    button_7 = Button( # Botão para ver a lista de animais para adoção.
        canvas,
        image=canvas.button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_lista_adocao(window, canvas, usuario_logado),
        relief="flat"
    )
    button_7.place( # Posiciona o botão.
        x=378.0,
        y=393.0,
        width=205.0,
        height=48.0
    )

    canvas.button_image_8 = PhotoImage( # Imagem do botão "Lista Tratamento".
        file=tools.relative_to_assets("TelaMenuAdm", "button_8.png")
    )
    button_8 = Button( # Botão para ver a lista de animais em tratamento.
        canvas,
        image=canvas.button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:transicao_para_lista_tratamento(window, canvas, usuario_logado),
        relief="flat"
    )
    button_8.place( # Posiciona o botão.
        x=378.0,
        y=483.0,
        width=216.0,
        height=48.0
    )

    canvas.button_image_10 = PhotoImage( # Imagem do botão "Adicionar ADM".
        file=tools.relative_to_assets("TelaMenuAdm", "button_10.png")
    )
    button_10 = Button( # Botão para conceder permissão de administrador.
        canvas,
        image=canvas.button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_alterar_status_adm(entry_remover_adm, False, window),
        relief="flat"
    )
    button_10.place( # Posiciona o botão.
        x=1032.0,
        y=657.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    entry_image_1 = PhotoImage( # Carrega a imagem de fundo para o campo de entrada.
        file=tools.relative_to_assets("TelaMenuAdm", "entry_1.png")
    )
    entry_bg_1 = canvas.create_image( # Exibe a imagem de fundo do campo.
        1108.0,
        394.0,
        image=entry_image_1
    )

    entry_adicionar_adm = Entry( # Campo de entrada para adicionar o email de um administrador.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 14)
    )
    entry_adicionar_adm.place( # Posiciona o campo de entrada.
        x=995.0,
        y=365.0,
        width=226.0,
        height=56.0
    )

    entry_image_2 = PhotoImage( # Carrega a imagem de fundo para o campo de entrada.
        file=tools.relative_to_assets("TelaMenuAdm", "entry_2.png")
    )
    entry_bg_2 = canvas.create_image( # Exibe a imagem de fundo do campo.
        1108.0,
        619.0,
        image=entry_image_2
    )

    entry_remover_adm = Entry( # Campo de entrada para remover o email de um administrador.
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 14)
    )
    entry_remover_adm.place( # Posiciona o campo de entrada.
        x=995.0,
        y=590.0,
        width=226.0,
        height=56.0
    )