from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from PIL import Image, ImageTk
import time
import tools
import tela_cadastro

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "TKassets" / "TelaInicial"

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#45312C")

canvas = Canvas(
    window,
    bg = "#45312C",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def tela_inicial():
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=tools.relative_to_assets(ASSETS_PATH, OUTPUT_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        360.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=tools.relative_to_assets(ASSETS_PATH, OUTPUT_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:tela_cadastro.tela_cadastro(),
        relief="flat"
    )
    button_1.place(
        x=451.80340576171875,
        y=584.0,
        width=173.69313049316406,
        height=72.4165267944336
    )

    button_image_2 = PhotoImage(
        file=tools.relative_to_assets(ASSETS_PATH, OUTPUT_PATH,"button_2.png"))
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

tela_inicial()