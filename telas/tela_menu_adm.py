from tkinter import Button, PhotoImage, Entry
from telas import tools

def transicao_para_inicial(window, canvas):
    from telas import tela_inicial
    tools.fade_out(
        window,
        canvas,
        lambda: tela_inicial.criar_tela_inicial(window, canvas)
    )

def transicao_para_cadastrar_animal(window, canvas, usuario_logado):
    from telas import tela_cadastrar_animal
    tools.fade_out(
        window,
        canvas,
        lambda: tela_cadastrar_animal.criar_tela_cadastrar_animal(window, canvas, usuario_logado)
    )

def tentar_alterar_status_adm(entry_widget, novo_status, window):
    from .modulos import usercrud

    email = entry_widget.get()
    resultado = usercrud.alterar_status_adm(email, novo_status)

    if "sucesso" in resultado:
        tools.custom_messagebox(window, "Operação Concluída", resultado)
    else:
        tools.custom_messagebox(window, "Erro", resultado)
    
    entry_widget.delete(0, 'end')

def transicao_para_lista_adocao(window, canvas, usuario_logado):
    """
    Inicia a transição para a tela de feedback.
    """
    from telas import tela_lista_adocao
    tools.fade_out(
        window,
        canvas,
        lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado)
    )

def transicao_para_lista_tratamento(window, canvas, usuario_logado):
    """
    Inicia a transição para a tela de feedback.
    """
    from telas import tela_lista_tratamento
    tools.fade_out(
        window,
        canvas,
        lambda: tela_lista_tratamento.criar_tela_lista_tratamento(window, canvas, usuario_logado)
    )

def criar_tela_menu_adm(window, canvas, usuario_logado):
    from telas import tela_lista_adocao
    from telas import tela_lista_tratamento
    
    tools.limpar_tela(canvas)
    canvas.configure(bg="#FFFFFF")

    canvas.image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_1.png")
    )
    canvas.create_image(
        640.0,
        423.0,
        image=canvas.image_1
    )

    canvas.button_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_1.png")
    )
    button_1 = Button(
        canvas,
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_cadastrar_animal(window, canvas, usuario_logado),
        relief="flat"
    )
    button_1.place(
        x=98.0,
        y=556.0,
        width=136.0,
        height=140.0
    )

    canvas.image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "image_2.png")
    )
    canvas.create_image(
        163.0,
        455.0,
        image=canvas.image_2
    )

    canvas.button_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_2.png")
    )
    button_2 = Button(
        canvas,
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_inicial(window, canvas),
        relief="flat"
    )
    button_2.place(
        x=1133.0,
        y=29.0,
        width=106.74418640136719,
        height=102.0
    )

    canvas.button_image_3 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_3.png")
    )
    button_3 = Button(
        canvas,
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_alterar_status_adm(entry_remover_adm, False, window),
        relief="flat"
    )
    button_3.place(
        x=1032.0,
        y=432.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_4 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_4.png")
    )
    button_4 = Button(
        canvas,
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=725.0,
        y=393.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_5 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_5.png")
    )
    button_5 = Button(
        canvas,
        image=canvas.button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=725.0,
        y=479.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    canvas.button_image_6 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_6.png")
    )
    button_6 = Button(
        canvas,
        image=canvas.button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=714.0,
        y=565.0,
        width=167.0,
        height=48.0
    )

    canvas.button_image_7 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_7.png")
    )
    button_7 = Button(
        canvas,
        image=canvas.button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tools.fade_out(window, canvas, lambda: tela_lista_adocao.criar_tela_lista_adocao(window, canvas, usuario_logado)),
        relief="flat"
    )
    button_7.place(
        x=378.0,
        y=393.0,
        width=205.0,
        height=48.0
    )

    canvas.button_image_8 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_8.png")
    )
    button_8 = Button(
        canvas,
        image=canvas.button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tools.fade_out(window, canvas, lambda: tela_lista_tratamento.criar_tela_lista_tratamento(window, canvas, usuario_logado)),
        relief="flat"
    )
    button_8.place(
        x=378.0,
        y=483.0,
        width=216.0,
        height=48.0
    )

    canvas.button_image_10 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "button_10.png")
    )
    button_10 = Button(
        canvas,
        image=canvas.button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tentar_alterar_status_adm(entry_adicionar_adm, True, window),
        relief="flat"
    )
    button_10.place(
        x=1032.0,
        y=657.0,
        width=147.75509643554688,
        height=48.020408630371094
    )

    entry_image_1 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "entry_1.png")
    )
    entry_bg_1 = canvas.create_image(
        1108.0,
        394.0,
        image=entry_image_1
    )

    entry_adicionar_adm = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 14)
    )
    entry_adicionar_adm.place(
        x=995.0,
        y=365.0,
        width=226.0,
        height=56.0
    )

    entry_image_2 = PhotoImage(
        file=tools.relative_to_assets("TelaMenuAdm", "entry_2.png")
    )
    entry_bg_2 = canvas.create_image(
        1108.0,
        619.0,
        image=entry_image_2
    )

    entry_remover_adm = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 14)
    )
    entry_remover_adm.place(
        x=995.0,
        y=590.0,
        width=226.0,
        height=56.0
    )