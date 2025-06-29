from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
import tela_inicial

window = Tk()
window.title("P.A.T.A.S")
window.geometry("1280x720")

icon_path = Path(__file__).parent / "TKassets" / "pata_256.png"
icon = PhotoImage(
    file=icon_path
)
window.iconphoto(
    True,
    icon
)

canvas = Canvas(
    window,
    bg="#45312C",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.pack(
    fill="both",
    expand=True
)

tela_inicial.criar_tela_inicial(window, canvas)

window.resizable(False, False)
window.mainloop()