from tkinter import Button
import tela_inicial
import tools

def _transicao_para_inicial(window, canvas):
    tools.fade_out(window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas))

def criar_tela_cadastro(window, canvas):
    tools.limpar_tela(canvas)
    canvas.configure(bg="#45312C")

    canvas.create_text(
        640, 100,
        text="Tela de Cadastro",
        fill="#FFFFFF",
        font=("Poppins Bold", 44 * -1)
    )

    voltar_button = Button(
        canvas,
        text="Voltar",
        font=("Poppins", 16),
        command=lambda: _transicao_para_inicial(window, canvas)
    )
    voltar_button.place(x=50, y=650)