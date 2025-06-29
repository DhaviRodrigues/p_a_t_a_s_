from tkinter import Button, PhotoImage
from pathlib import Path
import webbrowser
import tools
import tela_cadastro

def _abrir_link_github():
    url = "https://github.com/DhaviRodrigues/p_a_t_a_s_"
    webbrowser.open_new_tab(url)

def _iniciar_transicao_cadastro(window, canvas):
    callback_function = lambda: tela_cadastro.criar_tela_cadastro(window, canvas)
    tools.fade_out(
        window,
        canvas,
        callback_function
    )

def criar_tela_inicial(window, canvas):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#45312C")

    canvas.image_bg = PhotoImage(file=tools.relative_to_assets("TelaInicial", "image_1.png"))
    canvas.button_img_1 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_1.png"))
    canvas.button_img_2 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_2.png"))
    canvas.button_img_3 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_3.png"))

    canvas.create_image(
        640.0,
        360.0,
        image=canvas.image_bg
    )

    canvas.create_text(
        498.0,
        380.0,
        anchor="nw",
        text="BEM – VINDO AO",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )

    button_1 = Button(
        canvas,
        image=canvas.button_img_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: _iniciar_transicao_cadastro(window, canvas),
        relief="flat"
    )
    button_1.place(
        x=451.8,
        y=584.0,
        width=173.69,
        height=72.41
    )

    button_2 = Button(
        canvas,
        image=canvas.button_img_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=641.28,
        y=584.0,
        width=173.69,
        height=72.41
    )

    button_3 = Button(
        canvas,
        image=canvas.button_img_3,
        borderwidth=0,
        highlightthickness=0,
        command=_abrir_link_github,
        relief="flat"
    )
    button_3.place(
        x=465.0,
        y=664.0,
        width=343.0,
        height=43.0
    )