from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from PIL import Image, ImageTk
import time
import tools

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

def tela_cadastro():
    tools.limpar_janela()
    window.attributes("-alpha", 1.0)



