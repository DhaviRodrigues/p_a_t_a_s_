from pathlib import Path
from tkinter import Label, PhotoImage, Toplevel, Button, Frame

def relative_to_assets(subfolder: str, path: str) -> Path:
    """Monta um caminho absoluto para um arquivo de asset, facilitando o acesso."""
    output_path = Path(__file__).parent  # Pega o caminho do diretório onde este script está localizado.
    assets_path = output_path / "TKassets" / subfolder  # Constrói o caminho para a subpasta de assets especificada.
    return assets_path / Path(path)  # Retorna o caminho completo para o arquivo de asset final.


def fade_out(window, canvas, callback, steps=10, delay=20):
    """Cria uma sobreposição e inicia uma animação de fade para transição de tela."""
    overlay_label = Label(
        window,
        bg="#45312C",  # Cor de fundo que combina com o tema da aplicação.
        borderwidth=0)  # Remove qualquer borda para uma aparência limpa.
    
    overlay_label.place(
        x=0, y=0,  # Posiciona o label no canto superior esquerdo.
        relwidth=1, relheight=1)  # Faz o label ocupar 100% da largura e altura da janela.
    
    overlay_label.lower(canvas)  # Inicialmente, coloca o label de fade *atrás* do canvas.
    
    fade_step(window,overlay_label,0,steps,delay,callback)  # Inicia a animação de fade.


def fade_step(window, label, step, steps, delay, callback):
    """Executa um único passo da animação de fade de forma recursiva."""
    if step > steps:  # Condição de parada: se a animação completou todos os passos. No caso, 10 passos.
        label.destroy()  # Destrói o label de sobreposição para liberar memória.
        if callback:  # Se uma função de callback foi fornecida...
            callback()  # ...a executa.
        return  # Encerra a função para parar a recursão.
    
    label.lift()  # Traz o label de fade para a frente, tornando-o visível.
    window.after(
        delay,  # Atraso em milissegundos para a próxima execução. 20ms no caso.
        lambda: fade_step(window,label,step + 1,steps,delay,callback))  # Agenda a próxima chamada recursiva.
    

def limpar_tela(canvas):
    """Remove todos os widgets filhos e todos os itens desenhados de um Canvas."""
    for widget in canvas.winfo_children():  # Itera sobre todos os widgets (botões, etc.) dentro do canvas.
        widget.destroy()  # Destrói cada widget encontrado.
    canvas.delete("all")  # Apaga todos os itens desenhados (imagens, formas, etc.).


def custom_messagebox(master,titulo, mensagem):
    """Exibe uma caixa de diálogo modal com mensagem e botão "OK"."""
    dialog = Toplevel(master)  # Cria uma nova janela (Toplevel) que pertence à janela 'master'.
    dialog.title(titulo)  # Define o texto da barra de título.
    dialog.configure(bg="#EADFC8")  # Define a cor de fundo da janela.
    dialog.resizable(False, False)  # Impede que o usuário redimensione a caixa de diálogo.

    dialog.update_idletasks()  # Força o Tkinter a renderizar a janela para que suas dimensões sejam conhecidas.
    
    width = 400  # Define a largura fixa da caixa.
    height = 200  # Define a altura fixa da caixa.
    x = master.winfo_x() + (master.winfo_width() - width) // 2  # Calcula a coordenada X para centralizar a caixa.
    y = master.winfo_y() + (master.winfo_height() - height) // 2  # Calcula a coordenada Y para centralizar a caixa.
    dialog.geometry(f'{width}x{height}+{x}+{y}')  # Aplica o tamanho e a posição calculados.

    label = Label(
        dialog,
        text=mensagem,  # O texto a ser exibido.
        font=("Poppins", 12),  # A fonte do texto.
        fg="#45312C",  # A cor do texto.
        bg="#EADFC8",  # A cor de fundo do label.
        wraplength=350,  # Quebra a linha do texto após 350 pixels.
        justify='center'  # Centraliza o texto com quebra de linha.
    )

    label.pack(
        pady=(20, 10),  # Adiciona espaçamento vertical (20 em cima, 10 embaixo).
        padx=10  # Adiciona espaçamento horizontal.
    )

    ok_button = Button( # Cria um botão "OK" na caixa de diálogo.
        dialog,
        text="OK",  # O texto do botão.
        font=("Poppins Black", 12),  # A fonte do botão.
        bg="#45312C",  # A cor de fundo do botão.
        fg="#EADFC8",  # A cor do texto do botão.
        borderwidth=0,  # A largura da borda.
        relief="raised",  # O estilo de relevo do botão.
        padx=10,
        pady=3,
        width=6,  # A largura do botão.
        command=dialog.destroy  # Define que o comando do botão é fechar a própria caixa.
    )

    ok_button.pack(
        pady=15  # Adiciona espaçamento vertical.
    )
    
    dialog.transient(master)  # Associa a caixa à janela mestre (exemplo minimiza junto).
    dialog.grab_set()  # Torna a caixa de diálogo modal (bloqueia a janela de trás).
    dialog.wait_window()  # Pausa o código aqui até que a 'dialog' seja fechada.


def sim_ou_nao(dialog, resultado):
    """
    Função auxiliar que define o resultado e fecha a janela.
    """
    dialog.result = resultado  # Atribui o resultado a um atributo da janela de diálogo.
    dialog.destroy()  # Fecha a janela de diálogo.


def custom_yn(master, titulo, mensagem):
    """
    Cria uma caixa de diálogo Sim/Não, para confirmar decisões importantes do usuário.
    """
    dialog = Toplevel(master)  # Cria a janela de diálogo.
    dialog.title(titulo)  # Define seu título.
    dialog.configure(bg="#EADFC8")  # Define sua cor de fundo.
    dialog.resizable(False, False)  # Impede seu redimensionamento.

    dialog.result = False  # Define um resultado padrão (será alterado se "Sim" for clicado).

    dialog.update_idletasks()  # Força a renderização para obter as dimensões corretas.
    
    width = 400  # Largura fixa.
    height = 150  # Altura inicial.
    x = master.winfo_x() + (master.winfo_width() - width) // 2  # Calcula a posição X.
    y = master.winfo_y() + (master.winfo_height() - height) // 2  # Calcula a posição Y.
    dialog.geometry(f'{width}x{height}+{x}+{y}')  # Aplica a geometria inicial.

    label = Label(
        dialog,
        text=mensagem, #Define o texto da mensagem.
        font=("Poppins", 12), # Define a fonte do texto.
        fg="#45312C", # Define a cor do texto.
        bg="#EADFC8", # Define a cor de fundo.
        wraplength=380, # Define a largura máxima do texto.
        justify='center' # Centraliza o texto.
    )

    label.pack(pady=(20, 10), padx=20, expand=True, fill='both')  # Adiciona o label.

    button_frame = Frame(dialog, bg="#EADFC8")  # Cria um Frame para agrupar os botões horizontalmente.
    button_frame.pack(pady=(0, 20))  # Adiciona o frame à janela.

    sim_button = Button(
        button_frame,
        text="Sim", # Define o texto do botão "Sim".
        font=("Poppins Black", 12), # Define a fonte do botão.
        bg="#45312C", # Define a cor de fundo do botão.
        fg="#EADFC8", # Define a cor do texto do botão.
        borderwidth=0, 
        relief="raised",
        padx=10,
        pady=10,
        width=8,
        command=lambda: sim_ou_nao(dialog, True)  # Ao clicar, chama a função auxiliar com o resultado True.
    )

    sim_button.pack(side='left', padx=(0, 15))  # Posiciona o botão à esquerda dentro do frame.

    nao_button = Button(
        button_frame,
        text="Não", # Define o texto do botão "Não".
        font=("Poppins Black", 12), # Define a fonte do botão.
        bg="#45312C", # Define a cor de fundo do botão.
        fg="#EADFC8", # Define a cor do texto do botão.
        borderwidth=0,
        relief="raised",
        padx=10,
        pady=10,
        width=8,
        command=lambda: sim_ou_nao(dialog, False)  # Ao clicar, chama a função auxiliar com o resultado False.
    )
    nao_button.pack(side='left')  # Posiciona o botão à esquerda, ao lado do botão "Sim".

    width = 400  # Define a largura novamente para o cálculo final.
    height = dialog.winfo_reqheight()  # Pega a altura mínima requerida pelos widgets para um ajuste perfeito.
    
    x = master.winfo_x() + (master.winfo_width() - width) // 2  # Recalcula a posição X.
    y = master.winfo_y() + (master.winfo_height() - height) // 2  # Recalcula a posição Y com a nova altura.
    
    dialog.geometry(f'{width}x{height}+{x}+{y}')  # Aplica a nova geometria com a altura ajustada.
    
    dialog.transient(master)  # Associa a caixa à janela mestre.
    dialog.grab_set()  # Bloqueia a janela de trás.
    master.wait_window(dialog)  # Pausa a janela mestre até que esta seja fechada.
    
    return dialog.result  # Retorna o resultado (True ou False) que foi definido.