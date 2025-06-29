import artes
#Importa as funções do módulo artes
from time import sleep
#Importa a função sleep do módulo time
import menus
#Importa as funções do módulo time
import json
#Permite importar dados em formato JSON
import os
#Permite a execução de  tarefas como navegar em diretórios, manipular arquivos
import usercrud
#Importa o user crud
import animalcrud
#Importa o animal crud
import pedidos
#Importa as funções do módulo pedidos


artes.conjunto() #Chama a função conjunto do módulo artes, que imprime as artes do P.A.T.A.S.
usuario = menus.menu_user_crud() #Chama a função menu_uc do módulo menus e retorna 
if usuario is not None:
    menus.menu_pos_login(usuario_logado=usuario) # Chama a função menupuc do módulo menus, caso o usuário tenha feito login com sucesso