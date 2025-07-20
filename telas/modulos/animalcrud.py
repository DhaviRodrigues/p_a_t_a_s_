import json
import shutil
from pathlib import Path
from telas import tools

class Animal:
    """Classe que representa um animal e tudo que diz respeito a ele."""
    def __init__(self, id, nome, especie, sexo, idade, informacoes, foto):
        """Inicializa um novo animal com os atributos fornecidos."""

        self.id = id
        self.nome = nome
        self.especie = especie
        self.sexo = sexo
        self.idade = idade
        self.informacoes = informacoes
        self.foto = foto
        self.processo_adocao = False


    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
        """Converte os atributos do animal em um dicionário."""
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "sexo": self.sexo,
            "idade": self.idade,
            "informacoes": self.informacoes,
            "foto": self.foto,
            "processo_adocao": self.processo_adocao
        }


    def validar_animal(nome, especie, sexo, idade, foto):
        """Valida os dados fornecidos para o cadastro de um novo animal."""
        if not nome: # Verifica se o nome foi preenchido.
            return 'O nome não pode estar vazio.'
        if not nome.replace(' ', '').isalpha(): # Verifica se o nome contém apenas letras e espaços.
            return 'O nome deve conter apenas letras e espaços.'
        if not especie: # Verifica se a espécie foi preenchida.
            return 'A espécie não pode estar vazia.'
        if sexo is None or sexo.upper() not in ['M', 'F']: # Verifica se o sexo foi selecionado.
            return 'O sexo deve ser selecionado (M ou F).'
        if not idade: # Verifica se a idade foi preenchida.
            return 'A idade não pode estar vazia.'
        if not idade.replace(' ', '').isalnum(): # Verifica se a idade contém apenas letras, espaços e números.
            return 'A idade deve conter apenas letras, espaços e números.'
        if not foto: # Verifica se uma foto foi selecionada.
            return "É obrigatório inserir uma foto do animal."
            
        return True # Retorna True se todas as validações passarem.


    def criar_animal(nome, especie, sexo, idade, info, tipo_cadastro, caminho_imagem_original):
        """Cria um novo animal, salva sua foto e o adiciona ao arquivo JSON apropriado."""
        nome_arquivo_json = f"animais_{tipo_cadastro}.json" # Determina o nome do arquivo JSON com base no tipo de cadastro.
        animais = carregar_dados(nome_arquivo_json) # Carrega a lista de animais existente.

        maior_foto_id = 0 # Inicializa a variável para encontrar o maior ID de foto existente.
        pasta_fotos = Path(__file__).parent.parent / "fotos_animais" # Define o caminho para a pasta de fotos.
        pasta_fotos.mkdir(exist_ok=True) # Cria a pasta se ela não existir.
        for f in pasta_fotos.glob("*.png"): # Itera sobre todos os arquivos .png na pasta.
            try:
                id_foto = int(f.stem) # Tenta converter o nome do arquivo (sem extensão) para um inteiro.
                if id_foto > maior_foto_id: # Se o ID da foto atual for maior,
                    maior_foto_id = id_foto # atualiza o maior ID encontrado.
            except ValueError:
                continue # Ignora arquivos que não têm nomes numéricos.
        novo_nome_foto = f"{maior_foto_id + 1}.png" # Cria um novo nome de arquivo para a foto, incrementando o maior ID.
        caminho_destino_foto = pasta_fotos / novo_nome_foto # Define o caminho completo de destino para a nova foto.

        try:
            shutil.copy(caminho_imagem_original, caminho_destino_foto) # Copia a imagem selecionada para a pasta de fotos do projeto.
        except Exception as e:
            print(f"Erro ao copiar a imagem: {e}") # Imprime um erro se a cópia falhar.
            return

        maior_id = -1 # Inicializa a variável para encontrar o maior ID de animal existente.
        for animal in animais: # Itera sobre os animais para encontrar o maior ID.
            if animal.get('id', -1) > maior_id:
                maior_id = animal['id']
        novo_id = maior_id + 1 # Cria um novo ID incremental para o animal.

        novo_animal = Animal(novo_id, nome.strip(), especie.strip(), sexo, idade.strip(), info, novo_nome_foto) # Cria uma nova instância da classe Animal.
        
        animais.append(novo_animal.converter_para_dicionario()) # Adiciona o novo animal (convertido em dicionário) à lista.
        salvar_dados(nome_arquivo_json, animais) # Salva a lista atualizada no arquivo JSON.


    def editar_animal(animal_atualizado, tipo_cadastro):
        """Encontra e salva as alterações de um animal no arquivo JSON apropriado."""
        nome_arquivo = tipo_cadastro # Define o nome do arquivo de destino.
        todos_animais = carregar_dados(nome_arquivo) # Carrega todos os animais do arquivo.

        nova_lista_animais = [] # Cria uma nova lista para armazenar os animais.
        for animal in todos_animais: # Itera sobre os animais existentes.
            if animal.get("id") != animal_atualizado.get("id"): # Adiciona todos os animais, exceto o que está sendo atualizado.
                nova_lista_animais.append(animal)
        
        nova_lista_animais.append(animal_atualizado) # Adiciona a versão atualizada do animal à nova lista.
        
        salvar_dados(nome_arquivo, nova_lista_animais) # Salva a lista completa de volta no arquivo.
        return True

    def excluir_animal(animal_id, nome_arquivo):
        """Encontra e deleta um animal do arquivo JSON apropriado."""
        todos_animais = carregar_dados(nome_arquivo) # Carrega todos os animais do arquivo especificado.

        animal_encontrado = False # Flag para verificar se o animal foi encontrado.
        nova_lista_animais = [] # Cria uma nova lista para armazenar os animais.
        for animal in todos_animais: # Itera sobre os animais existentes.
            if animal.get("id") == animal_id: # Se o ID corresponder ao animal a ser excluído,
                animal_encontrado = True # marca como encontrado e não o adiciona à nova lista.
            else:
                nova_lista_animais.append(animal) # Adiciona os outros animais à nova lista.
        
        if animal_encontrado: # Se o animal foi encontrado e removido da lista,
            salvar_dados(nome_arquivo, nova_lista_animais) # salva a nova lista (sem o animal excluído) no arquivo.
            return True

    def mover_animal_para_adotados(animal_id):
        # Carrega a lista de animais para adoção
        animais_adocao = carregar_dados("animais_adocao.json")
        animal_para_mover = None
        
        # Procura pelo animal na lista de animais para adoção
        nova_lista_adocao = []
        for animal in animais_adocao:
            if animal.get("id") != animal_id: #Excluindo o animal que será movido
                nova_lista_adocao.append(animal) # Gerar nova lista de adoção sem o animal que será movido
            if animal.get("id") == animal_id: #Encontra o animal que será movido
                animal_para_mover = animal
                break

        salvar_dados("animais_adocao.json", nova_lista_adocao) #Salva a nova lista de adoção sem o animal que será movido
        
        # Adiciona o animal na lista de animais já adotados
        animais_adotados = carregar_dados("animais_adotados.json")
        animais_adotados.append(animal_para_mover)
        salvar_dados("animais_adotados.json", animais_adotados)

def carregar_dados(arquivo):
    """Carrega dados de um arquivo JSON especificado."""
    try:
        with open(arquivo, 'r') as f: # Tenta abrir o arquivo em modo de leitura ('r').
            dados = json.load(f) # Carrega o conteúdo JSON do arquivo.
            return dados # Retorna os dados carregados.
    except FileNotFoundError: # Se o arquivo não existir.
        return [] # Retorna uma lista vazia para evitar erros.

def salvar_dados(arquivo, dados):
    """Salva uma lista de dicionários em um arquivo JSON com formatação."""
    with open(arquivo, 'w') as f: # Abre o arquivo em modo de escrita ('w'), sobrescrevendo o conteúdo.
        json.dump(dados, f, indent=6) # Escreve os dados no arquivo JSON com uma indentação de 6 espaços para legibilidade.