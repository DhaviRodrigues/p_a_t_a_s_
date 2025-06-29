from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from PIL import Image, ImageTk
import time


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def fade_out(callback, steps=10, delay=30):
    base_img = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    overlay_label = Label(window, bg="", borderwidth=0)
    overlay_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Armazena imagens em lista para evitar garbage collection
    fade_out.imgs = []
    # Começa a animação
    fade_step(0, steps, delay, callback, overlay_label)


def fade_step(step, steps, delay, callback, overlay_label):
    if step > steps:
        overlay_label.destroy()
        callback()
        return

    alpha = int(255 * (step / steps))
    img = Image.new("RGBA", (1280, 720), (0, 0, 0, alpha))
    photo = ImageTk.PhotoImage(img)
    fade_out.imgs.append(photo)  # impede o GC de deletar a imagem
    overlay_label.config(image=photo)

    window.after(delay, lambda: fade_step(step + 1, steps, delay, callback, overlay_label))


def limpar_janela():
    # Remove todos os widgets do canvas
    for widget in window.winfo_children():
        if widget != canvas: # Não remova o canvas principal
            widget.destroy()
    canvas.delete("all") # Limpa todos os itens desenhados no canvas (imagens, textos)
