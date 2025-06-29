#importando 
import usercrud
import menus
import animalcrud
from time import sleep

def ver_perfil(usuario_logado): #Considera como parâmetro o dicionário do usuário logado
    """
    Exibe o nome e e-mail do usuário logado."""

    print("\n--- Seus dados ---")
    print(f"Nome: {usuario_logado.get('nome', 'Não informado')}") # Imprime o nome do usuário logado
    print(f"E-mail: {usuario_logado.get('email', 'Não informado')}") # Imprime o e-mail do usuário logado
    sleep(2)
    print("-" * 20)
    input("Pressione ENTER para voltar ao menu.")

def atualizar_perfil(usuario_logado):
    """
    Permite que o usuário logado atualize seu nome, e-mail e senha."""
    print('\n--- Atualizar Perfil ---')
    
    arquivo_usuario = usercrud.carregar_dados('usuarios.json') #Carrega os a lista de usuarios
    
    print(f"\nNome atual: {usuario_logado['nome']}")
    while True:
        novo_nome = input(str("Digite o novo nome (ou ENTER para manter): ")).strip() #Altera o nome do usuário
        if not novo_nome:
            break
        elif not novo_nome.replace(' ', '').isalpha():
            print('Nome deve conter apenas letras. Tente novamente.')
        else:
            usuario_logado['nome'] = novo_nome
            break
    
    print(f"\nE-mail atual: {usuario_logado['email']}")
    while True:
        novo_email = input(str("Digite o novo e-mail (ou ENTER para manter): ")).strip().lower() #Altera o email do usuário
        if not novo_email:
            break
        
        email_existe = False
        for usuario_id in arquivo_usuario:
            if usuario_id['email'] == novo_email and usuario_id['id'] != usuario_logado['id']:
                email_existe = True
                break
        
        if email_existe:
            print('Este e-mail já está em uso por outro usuário. Por favor, digite outro e-mail.')
            continue
        
        if not ('@gmail.com' in novo_email or \
                '@hotmail.com' in novo_email or \
                '@yahoo.com' in novo_email or \
                '@outlook.com' in novo_email or \
                '@ufrpe.br' in novo_email or \
                'ufpe' in novo_email):
            print('Formato de e-mail inválido ou domínio não permitido. Por favor, digite um e-mail válido (ex: @gmail.com, @ufrpe.br, etc.).')
            continue
        else:
            usuario_logado['email'] = novo_email
            break

    print('\n--- Atualizar Senha ---')
    print('Deixe em branco para manter a senha atual.')
    while True:
        nova_senha = input(str("Digite a nova senha (mínimo 8 caracteres): ")).strip() #Altera a senha do usuário
        if not nova_senha:
            break
        
        if len(nova_senha) < 8:
            print('A senha deve ter no mínimo 8 caracteres.')
            continue
        
        confirmar_nova_senha = input(str("Confirme a nova senha: ")).strip()
        if nova_senha != confirmar_nova_senha:
            print('As senhas não coincidem. Por favor, tente novamente.')
            continue
        
        usuario_logado['senha'] = nova_senha
        break

    novo_arquivo_usuarios = []
    for usuarios in arquivo_usuario:
        if usuarios['id'] != usuario_logado['id']: #Exclui o usuario antigo
            novo_arquivo_usuarios.append(usuarios) #Cria uma lista sem o usuario antigo
    
    novo_arquivo_usuarios.append(usuario_logado) #Adiciona o usuario novo
        
    usercrud.salvar_dados('usuarios.json', novo_arquivo_usuarios) #Salva os dados
    
    print('\nPerfil atualizado com sucesso!')
    sleep(2)
    
    return usuario_logado

def deletar_conta(usuario_logado):
    """
    Exclui permanentemente a conta do usuário logado após confirmação da senha e consentimento.

    Requer que a senha atual seja informada e em seguida, solicita confirmação
    do usuário para excluir a conta. Caso confirmado, remove o usuário do arquivo 'usuarios.json'.
    """
    print('\n--- Excluir Conta ---')
    
    senha = input(str("Digite sua senha para confirmar a exclusão da conta: ")).strip() #Pede confirmação da senha
    if senha != usuario_logado['senha']:
        print('Senha incorreta. Exclusão de conta cancelada.')
        sleep(2)
        return False
    
    while True:
        confirmacao = input(str("Tem certeza que deseja EXCLUIR PERMANENTEMENTE sua conta? (S/N): ")).strip().lower() #Confirmação de exclusão
        if confirmacao == 's':
            break
        elif confirmacao == 'n':
            print('Exclusão de conta cancelada.')
            sleep(2)
            return False
        else:
            print('Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')
            sleep(1)

    arquivo_usuario = usercrud.carregar_dados('usuarios.json')
    
    novo_arquivo_usuarios = []
    for usuarios in arquivo_usuario:
        if usuarios['id'] != usuario_logado['id']:#Exclui o usuario da lista
            novo_arquivo_usuarios.append(usuarios) #Cria uma lista sem o usario logado
    
    usercrud.salvar_dados('usuarios.json', novo_arquivo_usuarios) #Salva os dados
    
    print('\nSua conta foi excluída com sucesso. Você será deslogado.')
    sleep(2)
    return True