import json
import os
from time import sleep

class Animal:
    """Classe que representa um animal"""
    def __init__(self, id, nome, especie, sexo, idade, informacoes):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.sexo = sexo
        self.idade = idade
        self.informacoes = informacoes
    
    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "sexo": self.sexo,
            "idade": self.idade,
            "informacoes": self.informacoes
        }

def validar_animal(nome, especie, sexo, idade):
    """Valida os dados de entrada para o cadastro de um novo animal."""
    if not nome:
        return 'O nome não pode estar vazio.'
    if not nome.replace(' ', '').isalpha():
        return 'O nome deve conter apenas letras e espaços.'
    if not especie:
        return 'A espécie não pode estar vazia.'
    if sexo is None or sexo.upper() not in ['M', 'F']:
        return 'O sexo deve ser selecionado (M ou F).'
    if not idade:
        return 'A idade não pode estar vazia.'
    if not idade.replace(' ', '').isalnum():
        return 'A idade deve conter apenas letras, espaços e números.'
    return True

def criar_animal(nome, especie, sexo, idade, info, nome_arquivo):
    """Cria um novo objeto Animal e o salva no arquivo JSON apropriado."""
    animais = carregar_dados(nome_arquivo)
    
    maior_id = -1
    for animal in animais:
        if animal.get('id', -1) > maior_id:
            maior_id = animal['id']
    novo_id = maior_id + 1

    novo_animal = Animal(novo_id, nome.strip(), especie, sexo, idade, info)
    
    animais.append(novo_animal.converter_para_dicionario())
    salvar_dados(nome_arquivo, animais)

def lista_animais_tratamento():
    """ Imprime uma lista dos animais que estão em processo de tratamento."""
    print("\n--- Animais em Processo de Tratamento ---")
    animais_tratamento = carregar_dados('animais_tratamento.json') # Carrega os dados do arquivo 'animais_tratamento.json'

    if not animais_tratamento: #Caso não jaka animais em tratamento, ele irá imprimir a mensagem abaixo
        print("Não há animais cadastrados em tratamento no momento.")
        sleep(2)
        return

    for animal in animais_tratamento: #Imprime uma lista com os animais em tratamento
        print("-" * 30)
        print(f"ID: {animal.get('id')}")
        print(f"Nome: {animal.get('nome')}")
        print(f"Espécie: {animal.get('especie')}")
        print(f"Sexo: {animal.get('sexo')}")
        print(f"Idade: {animal.get('idade')}")
        if animal.get('informações'):
            print(f"Informações: {animal.get('informações')}")
        print("-" * 30)
    sleep(3)

def lista_animais_adocao():
    """ Imprime uma lista dos animais que estão em processo de adoçao."""
    print("\n--- Animais em Processo de Adoção ---")
    animais_adocao = carregar_dados('animais_adocao.json') # Carrega os dados do arquivo 'animais_adocao.json'

    if not animais_adocao: #Caso não jaka animais em tratamento, ele irá imprimir a mensagem abaixo
        print("Não há animais cadastrados em adoção no momento.")
        sleep(2)
        return

    for animal in animais_adocao: #Imprime uma lista com os animais em tratamento
        print("-" * 30)
        print(f"ID: {animal.get('id')}")
        print(f"Nome: {animal.get('nome')}")
        print(f"Espécie: {animal.get('especie')}")
        print(f"Sexo: {animal.get('sexo')}")
        print(f"Idade: {animal.get('idade')}")
        if animal.get('informações'):
            print(f"Informações: {animal.get('informações')}")
        print("-" * 30)
    sleep(3)

def editar_animal_adocao():
    """Permite que o administrador possa editar livrimente as informações dos animais em adoção"""

    print(f"\n--- Editar Animal para Adoção ---")
    nome_arquivo = 'animais_adocao.json'
    animais_da_lista = carregar_dados(nome_arquivo) #Adicona a lista de animais a variável
    
    if not animais_da_lista: #Caso nao haja animais na lista:
        print(f"Não há animais para adoção para editar.")
        sleep(2)
        return

    animal_para_atualizar = None 

    while True:
        id_str = input(str(f"Digite o ID do animal para adoção que deseja editar (ou 'VOLTAR' para cancelar): ")).strip().lower()
        
        if id_str == 'voltar': #Opção de voltar ao menu
            print("Operação de edição cancelada.")
            sleep(1)
            return

        try:
            id_num = int(id_str) #Converte o valor do input para int
        except ValueError: #Caso o usuario nao digite um número, daria um erro na conversão, por isso o tratamento
            print("ID inválido. Por favor, digite um número.")
            sleep(1)
            continue

        verificação_id = None
        for animais in animais_da_lista: #Para cada animal na lista:
            if animais.get('id') == id_num: #Se o id do animal for igual ao id numerico:
                verificação_id = animais #Verificação id receberá o dicionário daquele animal
                break
        
        if verificação_id:
            animal_para_atualizar = verificação_id #Informa qual animal iremos editar
            break 
        else:
            print(f"ID {id_num} não encontrado. Por favor, informe um ID existente.")
            sleep(1)
            
    print("\n--- Informações Atuais ---") #Imprime as atuais informações
    print(f"ID: {animal_para_atualizar.get('id')}")
    print(f"Nome: {animal_para_atualizar.get('nome')}")
    print(f"Espécie: {animal_para_atualizar.get('especie')}")
    print(f"Sexo: {animal_para_atualizar.get('sexo')}")
    print(f"Idade: {animal_para_atualizar.get('idade')}")
    print(f"Informações: {animal_para_atualizar.get('informacões')}")

    print("\n--- Digite o novo valor ou deixe em branco para manter o atual ---")
    
    while True: #Permite que o adm modifique o nome do animal
        novo_nome = input("Nome: ").strip()
        if not novo_nome:
            break
        elif novo_nome.replace(' ', '').isalnum() == False:
            print('Nome deve conter apenas letras e espaços. Tente novamente.')
        else:
            animal_para_atualizar['nome'] = novo_nome
            break

    while True:  #Permite que o adm modifique a espécie do animal
        nova_especie = input("Espécie: ").strip()
        if not nova_especie:
            break
        elif nova_especie.replace(' ', '').isalnum() == False:
            print('A espécie deve conter apenas letras, números e parênteses. Tente novamente.')
        else:
            animal_para_atualizar['especie'] = nova_especie
            break

    while True:  #Permite que o adm modifique o sexo do animal
        novo_sexo = input("Sexo [M/F]: ").strip().upper()
        if not novo_sexo:
            break
        elif novo_sexo not in ('M', 'F'):
            print('Digite um valor válido (M ou F). Tente novamente.')
        else:
            animal_para_atualizar['sexo'] = novo_sexo
            break

    while True:  #Permite que o adm modifique a idade do animal
        nova_idade = input("Idade: ").strip()
        if not nova_idade:
            break
        elif nova_idade.replace(' ', '').isalnum() == False:
            print('A idade deve conter apenas letras e números. Tente novamente.')
        else:
            animal_para_atualizar['idade'] = nova_idade
            break

    nova_info = input("Informações: ").strip()  #Permite que o adm modifique as informações do animal
    if nova_info:
        animal_para_atualizar['informacões'] = nova_info


    salvar_dados(nome_arquivo, animais_da_lista) #Salva os dados
    
    print('\nAnimal atualizado com sucesso!')
    sleep(2)

def editar_animal_tratamento():
    """Permite que o administrador possa editar livrimente as informações dos animais em tratamento"""

    print(f"\n--- Editar Animal em Tratamento ---")
    nome_arquivo = 'animais_tratamento.json'
    animais_da_lista = carregar_dados(nome_arquivo) #Adicona a lista de animais a variável
    
    if not animais_da_lista: #Caso nao haja animais na lista:
        print(f"Não há animais em tratamento para editar.")
        sleep(2)
        return

    animal_para_atualizar = None 

    while True:
        id_str = input(str(f"Digite o ID do animal em tratamento que deseja editar (ou 'VOLTAR' para cancelar): ")).strip().lower()
        
        if id_str == 'voltar': #Opção de voltar ao menu
            print("Operação de edição cancelada.")
            sleep(1)
            return

        try:
            id_num = int(id_str) #Converte o valor do input para int
        except ValueError: #Caso o usuario nao digite um número, daria um erro na conversão, por isso o tratamento
            print("ID inválido. Por favor, digite um número.")
            sleep(1)
            continue

        verificação_id = None
        for animais in animais_da_lista: #Para cada animal na lista: (Mantendo seu nome de variável 'animais')
            if animais.get('id') == id_num: #Se o id do animal for igual ao id numerico:
                verificação_id = animais #Verificação id receberá o dicionário daquele animal
                break
        
        if verificação_id:
            animal_para_atualizar = verificação_id #Informa qual animal iremos editar
            break 
        else:
            print(f"ID {id_num} não encontrado na lista de tratamento. Por favor, informe um ID existente.")
            sleep(1)
            
    print("\n--- Informações Atuais ---") #Imprime as atuais informações
    print(f"ID: {animal_para_atualizar.get('id')}")
    print(f"Nome: {animal_para_atualizar.get('nome')}")
    print(f"Espécie: {animal_para_atualizar.get('especie')}")
    print(f"Sexo: {animal_para_atualizar.get('sexo')}")
    print(f"Idade: {animal_para_atualizar.get('idade')}")
    print(f"Informações: {animal_para_atualizar.get('informacões')}")

    print("\n--- Digite o novo valor ou deixe em branco para manter o atual ---")
    
    while True: #Permite que o adm modifique o nome do animal
        novo_nome = input("Nome: ").strip()
        if not novo_nome:
            break
        elif novo_nome.replace(' ', '').isalnum() == False:
            print('Nome deve conter apenas letras e espaços. Tente novamente.')
        else:
            animal_para_atualizar['nome'] = novo_nome
            break

    while True:  #Permite que o adm modifique a espécie do animal
        nova_especie = input("Espécie: ").strip()
        if not nova_especie:
            break
        elif nova_especie.replace(' ', '').isalnum() == False:
            print('A espécie deve conter apenas letras, números e parênteses. Tente novamente.')
        else:
            animal_para_atualizar['especie'] = nova_especie
            break

    while True:  #Permite que o adm modifique o sexo do animal
        novo_sexo = input("Sexo [M/F]: ").strip().upper()
        if not novo_sexo:
            break
        elif novo_sexo not in ('M', 'F'):
            print('Digite um valor válido (M ou F). Tente novamente.')
        else:
            animal_para_atualizar['sexo'] = novo_sexo
            break

    while True:  #Permite que o adm modifique a idade do animal
        nova_idade = input("Idade: ").strip()
        if not nova_idade:
            break
        elif nova_idade.replace(' ', '').isalnum() == False:
            print('A idade deve conter apenas letras e números. Tente novamente.')
        else:
            animal_para_atualizar['idade'] = nova_idade
            break

    nova_info = input("Informações: ").strip()  #Permite que o adm modifique as informações do animal
    if nova_info:
        animal_para_atualizar['informacões'] = nova_info


    salvar_dados(nome_arquivo, animais_da_lista) #Salva os dados
    
    print('\nAnimal atualizado com sucesso!')
    sleep(2)

def carregar_dados(arquivo):
    """Carrega o arquivo json dos animais"""
    try:
        with open(arquivo, 'r') as arquivo:
            #Tenta abrir o arquivo em modo 'r'(leitura)
            dados = json.load(arquivo)
            #Insere as informações do arquivo json em "dados"
            return dados
    except FileNotFoundError:
        #Se o arquivo não for encontrado, ele retornará o arquivo com uma lista em branco no nome informado na variável "arquivo"
        return []

def salvar_dados(arquivo, dados):
    """Salva as informações no arquivo json dos animais"""
    with open(arquivo, 'w') as arquivo:
        #Abre o arquivo json em modo 'w'(write)
        json.dump(dados, arquivo, indent=6)
        #json é a biblioteca importada, .dump() é a função que vai jogar da primeira variável, dentro do "arquivo" de animais.json, indent=6 é apenas para deixar mais organizado na hora da escrita do arquivo
