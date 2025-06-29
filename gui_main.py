from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
from tkextrafont import Font
import tela_inicial
from modulos import usercrud

window = Tk()
window.title("P.A.T.A.S")
window.geometry("1280x720")

try:
    font_path_regular = Path(__file__).parent / "fonts" / "Poppins-Regular.ttf"
    font_path_black = Path(__file__).parent / "fonts" / "Poppins-Black.ttf"
    
    window.font_poppins_regular = Font(file=font_path_regular, family="Poppins")
    window.font_poppins_black = Font(file=font_path_black, family="Poppins Black")
    
    print("Fontes 'Poppins' carregadas com sucesso.")
except Exception as e:
    print(f"Erro ao carregar fontes: {e}. A usar fontes padrão.")
    window.font_poppins_regular = ("Arial", 18)
    window.font_poppins_black = ("Arial", 24, "bold")

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