from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "TKassets" / "UI"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

import time

def fade_out(window, step=0.05, delay=50, on_complete=None):
    alpha = 1.0
    def step_fade():
        nonlocal alpha
        alpha -= step
        if alpha <= 0:
            alpha = 0
            window.attributes("-alpha", alpha)
            if on_complete:
                on_complete()
            return
        window.attributes("-alpha", alpha)
        window.after(delay, step_fade)
    step_fade()

def limpar_janela():
    # Remove todos os widgets do canvas
    for widget in window.winfo_children():
        if widget != canvas: # Não remova o canvas principal
            widget.destroy()
    canvas.delete("all") # Limpa todos os itens desenhados no canvas (imagens, textos)


def tela_inicial():
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        360.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: tela_cadastro(),
        relief="flat"
    )
    button_1.place(
        x=451.80340576171875,
        y=584.0,
        width=173.69313049316406,
        height=72.4165267944336
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=641.2868041992188,
        y=584.0000610351562,
        width=173.69313049316406,
        height=72.4165267944336
    )

    canvas.create_text(
        498.0,
        380.0,
        anchor="nw",
        text="BEM – VINDO AO",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def tela_cadastro():
    limpar_janela()


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#45312C")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

tela_inicial()