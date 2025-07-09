# p_a_t_a_s_
P.A.T.A.S. é um acrônimo para Plataforma de Apoio ao Tratamento e Adoção Solidária. 

Senha APP: pxys ogwp crlw foar 
-> Necessario para criar o chat bot de envio de email
<p align="center">
# P.A.T.A.S. - Plataforma de Apoio ao Tratamento e Adoção Solidária 🐾

<p align="center">
  <img src="https://raw.githubusercontent.com/DhaviRodrigues/p_a_t_a_s_/main/telas/TKassets/logopatas.png" width="400" alt="P.A.T.A.S. Logo">
</p>

<p align="center">
  <strong>Uma solução de desktop para a gestão completa do ciclo de vida de animais resgatados, desde o tratamento até à adoção.</strong>
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python" alt="Python 3.13">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status">
</p>

---

## 📖 Sobre o Projeto

O **P.A.T.A.S.** nasceu para resolver um problema central enfrentado por ONGs e projetos voluntários de resgate animal: a falta de uma ferramenta centralizada e acessível para gerir o fluxo de animais. A plataforma oferece uma solução tecnológica robusta, construída em Python, que permite o controle total sobre o registo de animais, o acompanhamento do seu estado de saúde e a sua eventual disponibilização para uma adoção responsável.

Com uma interface gráfica intuitiva, o objetivo é otimizar o trabalho dos voluntários e criar uma ponte transparente e de confiança com a comunidade de adotantes.

## 🚀 Funcionalidades

### 👤 Para Utilizadores
- **Autenticação Segura:** Sistema completo de cadastro e login.
- **Navegação Intuitiva:** Um menu principal que dá acesso a todas as funcionalidades do utilizador.
- **Listagem de Animais:** Visualize listas dinâmicas e roláveis de animais para **adoção** e em **tratamento**.
- **Gestão de Perfil:** Uma área dedicada para visualizar e editar as suas informações pessoais.
- **Interação:**
    - Tela para enviar **doações financeiras** à organização.
    - Canal para **relatar dúvidas e erros**.

### 💼 Para Administradores
- **Painel de Controle:** Um menu administrativo exclusivo com ferramentas de gestão.
- **Cadastro de Animais:** Formulário detalhado para registar novos animais, incluindo:
    - Nome, idade e espécie.
    - Seleção de sexo (M/F).
    - Upload de foto do animal a partir do computador.
    - Definição do estado: "Em Tratamento" ou "Para Adoção".
- **Gestão de Pedidos:** Visualização e gestão dos pedidos de adoção enviados pelos utilizadores.

---

## 🛠️ Tecnologias e Ferramentas

| Tecnologia | Propósito |
| :--- | :--- |
| **Python** | Linguagem principal do projeto. |
| **Tkinter** | Biblioteca nativa para a construção da interface gráfica (GUI). |
| **Pillow (PIL)** | Manipulação e redimensionamento de imagens (fotos dos animais e ícones). |
| **tkextrafont**| Carregamento de fontes personalizadas (`.ttf`) para uma identidade visual única. |
| **JSON** | Formato utilizado para o armazenamento persistente dos dados (utilizadores, animais, etc.). |

---

## ⚙️ Instalação e Execução

Para executar o P.A.T.A.S. no seu ambiente local, siga os passos abaixo.

### Pré-requisitos
- Python 3.10 ou superior
- `pip` (Gestor de Pacotes do Python)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/DhaviRodrigues/p_a_t_a_s_.git](https://github.com/DhaviRodrigues/p_a_t_a_s_.git)
    ```

2.  **Instale as bibliotecas:**
    O ficheiro `requesitos.txt` contém todas as bibliotecas necessária:
    ```bash
    pillow
    webbrowser
    tkextrafont
    shutil
    pathlib

    ```

4.  **Execute a aplicação:**
    Para iniciar a interface gráfica, execute o `gui_main.py` em **modo administrador** a partir da pasta raiz do projeto, ou adicione a pasta ao workspace do VS Code e inicie o `gui_main.py`.
    ```bash
    python gui_main.py
    ```
