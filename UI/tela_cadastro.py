from tkinter import Button
import tela_inicial
import tools

def criar_tela_cadastro(window, canvas):
    canvas.delete("all")

    canvas.create_text(
        640, 100,
        text="Tela de Cadastro",
        fill="white",
        font=("Poppins Bold", 44 * -1)
    )

    def transicao_para_inicial():
        tools.fade_out(window, canvas, lambda: tela_inicial.criar_tela_inicial(window, canvas))

    voltar_button = Button(
        canvas,
        text="Voltar",
        font=("Poppins", 16),
        command=transicao_para_inicial
    )
    voltar_button.place(x=50, y=650)