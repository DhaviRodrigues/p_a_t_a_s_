from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import tools

def criar_tela_inicial(window, canvas):
    canvas.delete("all")
    canvas.configure(bg="#45312C")

    canvas.image_bg = PhotoImage(file=tools.relative_to_assets("image_1.png"))
    canvas.button_img_1 = PhotoImage(file=tools.relative_to_assets("button_1.png"))
    canvas.button_img_2 = PhotoImage(file=tools.relative_to_assets("button_2.png"))

    canvas.create_image(640.0, 360.0, image=canvas.image_bg)

    canvas.create_text(
        498.0, 380.0, anchor="nw",
        text="BEM – VINDO AO", fill="#44312D", font=("Poppins Black", 32 * -1)
    )

    def iniciar_transicao_cadastro():
        callback_function = lambda: tela_cadastro.criar_tela_cadastro(window, canvas)
        tools.fade_out(window, canvas, callback_function)

    button_1 = Button(
        canvas, image=canvas.button_img_1, borderwidth=0, highlightthickness=0,
        command=iniciar_transicao_cadastro, relief="flat"
    )
    button_1.place(x=451.8, y=584.0, width=173.69, height=72.41)

    button_2 = Button(
        canvas, image=canvas.button_img_2, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_2 clicked"), relief="flat"
    )
    button_2.place(x=641.28, y=584.0, width=173.69, height=72.41)