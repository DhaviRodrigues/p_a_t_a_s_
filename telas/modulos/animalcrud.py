import json
import shutil
from pathlib import Path
from telas import tools

class Animal:
    """Classe que representa um animal"""
    def __init__(self, id, nome, especie, sexo, idade, informacoes, foto):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.sexo = sexo
        self.idade = idade
        self.informacoes = informacoes
        self.foto = foto
        self.processo_adocao = False


    def converter_para_dicionario(self): #Converte todas as intâncias em dicionarios
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
        if not foto:
            return "É obrigatório inserir uma foto do animal."
            
        return True


    def criar_animal(nome, especie, sexo, idade, info, tipo_cadastro, caminho_imagem_original):
        nome_arquivo_json = f"animais_{tipo_cadastro}.json"
        animais = carregar_dados(nome_arquivo_json)

        maior_foto_id = 0
        pasta_fotos = Path(__file__).parent.parent / "fotos_animais"
        pasta_fotos.mkdir(exist_ok=True)
        for f in pasta_fotos.glob("*.png"):
            try:
                id_foto = int(f.stem)
                if id_foto > maior_foto_id:
                    maior_foto_id = id_foto
            except ValueError:
                continue
        novo_nome_foto = f"{maior_foto_id + 1}.png"
        caminho_destino_foto = pasta_fotos / novo_nome_foto

        try:
            shutil.copy(caminho_imagem_original, caminho_destino_foto)
        except Exception as e:
            print(f"Erro ao copiar a imagem: {e}")
            return

        maior_id = -1
        for animal in animais:
            if animal.get('id', -1) > maior_id:
                maior_id = animal['id']
        novo_id = maior_id + 1

        novo_animal = Animal(novo_id, nome.strip(), especie.strip(), sexo, idade.strip(), info, novo_nome_foto)
        
        animais.append(novo_animal.converter_para_dicionario())
        salvar_dados(nome_arquivo_json, animais)


    def editar_animal(animal_atualizado, tipo_cadastro):
        """Encontra e salva as alterações de um animal no arquivo JSON apropriado."""
        nome_arquivo = tipo_cadastro
        todos_animais = carregar_dados(nome_arquivo)

        nova_lista_animais = []
        for animal in todos_animais:
            if animal.get("id") != animal_atualizado.get("id"):
                nova_lista_animais.append(animal)
        
        # Adiciona a versão atualizada do animal à nova lista.
        nova_lista_animais.append(animal_atualizado)
        
        # Salva a lista completa de volta no ficheiro.
        salvar_dados(nome_arquivo, nova_lista_animais)
        return True

    def excluir_animal(animal_id, tipo_cadastro):
        """Encontra e deleta um animal do arquivo JSON apropriado."""
        nome_arquivo = f"animais_{tipo_cadastro}.json"
        todos_animais = carregar_dados(nome_arquivo)

        animal_encontrado = False
        nova_lista_animais = []
        for animal in todos_animais:
            if animal.get("id") == animal_id:
                animal_encontrado = True
            else:
                nova_lista_animais.append(animal)
        
        if animal_encontrado:
            salvar_dados(nome_arquivo, nova_lista_animais)
            return True

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
