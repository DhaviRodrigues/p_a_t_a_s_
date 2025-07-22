import sys
import os
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from tkextrafont import Font

# Isso garante que a importação do módulo 'telas' funcione corretamente.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from telas import tela_inicial

window = Tk() # Cria a janela principal da aplicação.
window.title("P.A.T.A.S") # Define o título da janela.
window.geometry("1280x720") # Define o tamanho fixo da janela em pixels.

# Este bloco 'try...except' carrega fontes customizadas de forma segura.
try:
    # Define os caminhos para os arquivos de fonte 'Poppins' regular e black.
    font_path_regular = Path(__file__).parent / "telas" / "fonts" / "Poppins-Regular.ttf"
    font_path_black = Path(__file__).parent / "telas"/ "fonts" / "Poppins-Black.ttf"
    
    # Carrega os arquivos de fonte
    window.font_poppins_regular = Font(file=font_path_regular, family="Poppins")
    window.font_poppins_black = Font(file=font_path_black, family="Poppins Black")
    
    # Imprime uma mensagem que confirma que as fontes foram carregadas com sucesso.
    print("Fontes 'Poppins' carregadas com sucesso.")

# Se ocorrer qualquer erro no bloco 'try' (ex: arquivo não encontrado)...
except Exception as e:
    print(f"Erro ao carregar fontes: {e}. A usar fontes padrão.")
    # E define fontes do padrão do sistema para garantir que a aplicação continue funcionando.
    window.font_poppins_regular = ("Arial", 18)
    window.font_poppins_black = ("Arial", 24, "bold")

icon_path = Path(__file__).parent / "telas" / "TKassets" / "pata_256.png" # Define o caminho para o ícone da janela.

icon = PhotoImage(file=icon_path) # Carrega a imagem do ícone em um formato compatível com o Tkinter.

window.iconphoto(True,icon)# Define a imagem carregada como o ícone da janela.

# Cria o widget Canvas, que funcionará como uma "tela de pintura" para a interface.
canvas = Canvas(
    window,
    bg="#45312C",  # Cor de fundo.
    height=720, # Altura
    width=1280, # Largura
    bd=0,  # Remove a borda.
    highlightthickness=0,  # Remove a borda de foco.
    relief="ridge" # Define o estilo de borda como "ridge".
)

canvas.pack(fill="both",expand=True) # Expande o canvas para preencher a janela.

# Chama a função do módulo 'tela_inicial' para  impri,or a interface no canvas.
tela_inicial.criar_tela_inicial(window, canvas)

# Impede que o usuário redimensione a janela.
window.resizable(False, False)
# Inicia o loop de eventos da aplicação, que a mantém em execução e responsiva.
window.mainloop()