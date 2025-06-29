from pathlib import Path
from tkinter import Label, PhotoImage

def relative_to_assets(path: str) -> Path:
    output_path = Path(__file__).parent
    assets_path = output_path / "TKassets" / "TelaInicial"
    return assets_path / Path(path)

def fade_out(window, canvas, callback, steps=10, delay=20):
    overlay_label = Label(window, bg="#45312C", borderwidth=0)
    overlay_label.place(x=0, y=0, relwidth=1, relheight=1)
    overlay_label.lower(canvas)
    
    fade_step(window, overlay_label, 0, steps, delay, callback)

def fade_step(window, label, step, steps, delay, callback):
    if step > steps:
        label.destroy()
        if callback:
            callback()
        return

    label.lift()
    
    window.after(delay, lambda: fade_step(window, label, step + 1, steps, delay, callback))