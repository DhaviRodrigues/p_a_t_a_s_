from pathlib import Path
from tkinter import Label, PhotoImage, Toplevel, Button, Frame

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

def custom_messagebox(master,titulo, mensagem):
    dialog = Toplevel(master)
    dialog.title(titulo)
    dialog.configure(bg="#EADFC8")
    dialog.resizable(False, False)

    dialog.update_idletasks()
    
    width = 400
    height = 150
    x = master.winfo_x() + (master.winfo_width() - width) // 2
    y = master.winfo_y() + (master.winfo_height() - height) // 2
    dialog.geometry(f'{width}x{height}+{x}+{y}')

    label = Label(
        dialog,
        text=mensagem,
        font=("Poppins", 12),
        fg="#45312C",
        bg="#EADFC8",
        wraplength=350,
        justify='center'
    )
    label.pack(
        pady=(20, 10),
        padx=10
    )

    ok_button = Button(
        dialog,
        text="OK",
        font=("Poppins Black", 12),
        bg="#45312C",
        fg="#EADFC8",
        borderwidth=0,
        relief="raised",
        padx=10,
        pady=3,
        width=6,
        command=dialog.destroy
    )
    ok_button.pack(
        pady=15
    )
    
    dialog.transient(master)
    dialog.grab_set()
    dialog.wait_window()

def custom_yn(master, titulo, mensagem):
    """
    Cria uma caixa de diálogo Sim/Não personalizada.
    """
    dialog = Toplevel(master)
    dialog.title(titulo)
    dialog.configure(bg="#EADFC8")
    dialog.resizable(False, False)

    dialog.result = False

    dialog.update_idletasks()
    
    width = 400
    height = 150
    x = master.winfo_x() + (master.winfo_width() - width) // 2
    y = master.winfo_y() + (master.winfo_height() - height) // 2
    dialog.geometry(f'{width}x{height}+{x}+{y}')

    label = Label(
        dialog,
        text=mensagem,
        font=("Poppins", 12),
        fg="#45312C",
        bg="#EADFC8",
        wraplength=380,
        justify='center'
    )
    label.pack(pady=(20, 10), padx=20, expand=True, fill='both')

    button_frame = Frame(dialog, bg="#EADFC8")
    button_frame.pack(pady=(0, 20))

    def on_sim():
        dialog.result = True
        dialog.destroy()

    def on_nao():
        dialog.result = False
        dialog.destroy()

    sim_button = Button(
        button_frame,
        text="Sim",
        font=("Poppins Black", 12),
        bg="#45312C",
        fg="#EADFC8",
        borderwidth=0,
        relief="raised",
        padx=10,
        pady=3,
        width=8,
        command=on_sim
    )
    sim_button.pack(side='left', padx=(0, 15))

    nao_button = Button(
        button_frame,
        text="Não",
        font=("Poppins Black", 12),
        bg="#45312C",
        fg="#EADFC8",
        borderwidth=0,
        relief="raised",
        padx=10,
        pady=3,
        width=8,
        command=on_nao
    )
    nao_button.pack(side='left')
    
    dialog.transient(master)
    dialog.grab_set()
    master.wait_window(dialog)
    
    return dialog.result