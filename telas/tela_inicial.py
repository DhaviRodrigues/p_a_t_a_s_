from tkinter import Button, PhotoImage
from pathlib import Path
import webbrowser
from telas import tools

def abrir_link_github():
    """Abre o link do repositório do projeto no GitHub em uma nova aba do navegador."""
    url = "https://github.com/DhaviRodrigues/p_a_t_a_s_" # Define a URL do repositório.
    webbrowser.open_new_tab(url) # Abre a URL em uma nova aba.


def iniciar_transicao_cadastro(window, canvas):
    """Inicia a transição com efeito de fade-out para a tela de cadastro."""
    from telas import tela_cadastro
    
    callback_function = lambda: tela_cadastro.criar_tela_cadastro(window, canvas) # Define a função a ser chamada após o fade-out.
    tools.fade_out( # Chama a função de fade-out.
        window,
        canvas,
        callback_function
    )


def transicao_para_login(window, canvas):
    """Inicia a transição com efeito de fade-out para a tela de login."""
    from telas import tela_login
    
    callback_function = lambda: tela_login.criar_tela_login(window, canvas) # Define a função a ser chamada após o fade-out.
    tools.fade_out( # Chama a função de fade-out.
        window,
        canvas,
        callback_function
    )


def criar_tela_inicial(window, canvas):
    """Cria a interface gráfica da tela inicial, com opções de login, cadastro e acesso ao GitHub."""
    
    tools.limpar_tela(canvas) # Limpa a tela para desenhar os novos elementos.
    canvas.configure(bg="#45312C") # Define a cor de fundo do canvas.

    canvas.image_bg = PhotoImage(file=tools.relative_to_assets("TelaInicial", "image_1.png")) # Carrega a imagem de fundo.
    canvas.button_img_1 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_1.png")) # Carrega a imagem do botão de cadastro.
    canvas.button_img_2 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_2.png")) # Carrega a imagem do botão de login.
    canvas.button_img_3 = PhotoImage(file=tools.relative_to_assets("TelaInicial", "button_3.png")) # Carrega a imagem do botão do GitHub.

    canvas.create_image( # Exibe a imagem de fundo.
        640.0,
        360.0,
        image=canvas.image_bg
    )

    canvas.create_text( # Exibe o texto de boas-vindas.
        498.0,
        380.0,
        anchor="nw",
        text="BEM – VINDO AO",
        fill="#44312D",
        font=("Poppins Black", 32 * -1)
    )

    button_1 = Button( # Botão para ir para a tela de cadastro.
        canvas,
        image=canvas.button_img_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciar_transicao_cadastro(window, canvas),
        relief="flat"
    )
    button_1.place( # Posiciona o botão de cadastro.
        x=451.8,
        y=584.0,
        width=173.69,
        height=72.41
    )

    button_2 = Button( # Botão para ir para a tela de login.
        canvas,
        image=canvas.button_img_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transicao_para_login(window, canvas),
        relief="flat"
    )
    button_2.place( # Posiciona o botão de login.
        x=641.28,
        y=584.0,
        width=173.69,
        height=72.41
    )

    button_3 = Button( # Botão para abrir o link do GitHub.
        canvas,
        image=canvas.button_img_3,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_link_github,
        relief="flat"
    )
    button_3.place( # Posiciona o botão do GitHub.
        x=465.0,
        y=664.0,
        width=343.0,
        height=43.0
    )