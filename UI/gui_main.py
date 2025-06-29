from tkinter import Tk, Canvas
import tela_inicial

if __name__ == "__main__":
    window = Tk()
    window.title("P.A.T.A.S")
    window.geometry("1280x720")

    canvas = Canvas(
        window, bg="#45312C", height=720, width=1280,
        bd=0, highlightthickness=0, relief="ridge"
    )
    canvas.pack(fill="both", expand=True)

    tela_inicial.criar_tela_inicial(window, canvas)

    window.resizable(False, False)
    window.mainloop()