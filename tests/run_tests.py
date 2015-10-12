#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Para rodar os testes: 
# - no shell entre na pasta: tests/
# - execute: python run_tests.py
# Assim este arquivo de encarregará de rodar os testes na pasta tests/
#

from sys import path as sys_path
from sys import exit as sys_exit
from os import path as os_path
from os import remove as os_remove
from unittest import TestLoader, TextTestRunner
sys_path_append=sys_path.append
os_path_abspath=os_path.abspath

# Localizando a pasta onde o Web2py está para colocá-lo no sys.path
W2P = '/web2py/applications/' # se estiver rodando dentro do Web2py, o caminho deve conter esta string
JNKS = '/jenkins/jobs/' # se estiver rodando dentro do Jenkins, o caminho deve conter esta string
PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep))
if W2P in PATH:
    W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-4])
elif JNKS in PATH:
    W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-6])
    W2P_PATH = W2P_PATH+'/web2py'
else:
    raise Exception('Problem with the PATH. Please, contact an administrator!')
    sys_exit(1)
#W2P_PATH = "/docs/projects/web2py"
sys_path_append(os_path_abspath(W2P_PATH))

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path_abspath(__file__).split(os_path.sep)[:-2])
# Pasta atual, onde o run_tests.py está
ROOT_PATH=os_path.dirname(__file__)
#adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
mods=['controllers','modules']
for m in mods:
    sys_path_append(os_path_abspath(PROJECT_PATH+'/'+m))

def clear():
    print '\n'
    file_name = '/storage.sqlite'
    DB_PATH = (os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-1])) + file_name
    print DB_PATH
    try:
        os_remove(DB_PATH)
    except:
        print 'WARNING: Not found the file: \n'+DB_PATH

# Roda os testes da pasta test/
if __name__=='__main__':
    # Pega todos os arquivos da pasta corrente que sejam .py
    tests=TestLoader().discover(ROOT_PATH,"*.py")
    # Roda os testes
    # verbosity=2 aumenta o nível de detalhe da saida
    result=TextTestRunner(verbosity=2).run(tests) 
    #result = TextTestRunner().run(tests)
    clear()
    # Se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys_exit(1)