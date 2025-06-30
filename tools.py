from pathlib import Path
from tkinter import Label, PhotoImage, Toplevel, Button

def relative_to_assets(subfolder: str, path: str) -> Path:
    output_path = Path(__file__).parent
    assets_path = output_path / "TKassets" / subfolder
    return assets_path / Path(path)

def fade_out(window, canvas, callback, steps=10, delay=20):
    overlay_label = Label(
        window,
        bg="#45312C",
        borderwidth=0
    )
    overlay_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )
    overlay_label.lower(canvas)
    
    fade_step(
        window,
        overlay_label,
        0,
        steps,
        delay,
        callback
    )

def fade_step(window, label, step, steps, delay, callback):
    if step > steps:
        label.destroy()
        if callback:
            callback()
        return
    label.lift()
    window.after(
        delay,
        lambda: fade_step(
            window,
            label,
            step + 1,
            steps,
            delay,
            callback
        )
    )

def limpar_tela(canvas):
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.delete("all")

def custom_messagebox(titulo, mensagem):
    dialog = Toplevel()
    dialog.title(titulo)
    dialog.configure(bg="#45312C")

    dialog.geometry("400x150")

    label = Label(
        dialog,
        text=mensagem,
        font=("Poppins", 12),
        fg="#EADFC8",
        bg="#45312C"
    )
    label.pack(
        pady=20,
        padx=10
    )

    ok_button = Button(
        dialog,
        text="OK",
        font=("Poppins Bold", 10),
        width=10,
        command=dialog.destroy
    )
    ok_button.pack(
        pady=10
    )
    
    dialog.transient()
    dialog.grab_set()
    dialog.wait_window()