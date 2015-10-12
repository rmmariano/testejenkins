#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Para rodar os testes: 
# - no shell entre na pasta: tests/
# - execute: python run_tests.py
# Assim este arquivo de encarregará de rodar os testes na pasta tests/
#


# Salva os caminhos das pastas que serão testadas no sys.path
from sys import path as sys_path
from sys import exit as sys_exit
from os import path as os_path
sys_path_append=sys_path.append
os_path_abspath=os_path.abspath

# Localizando a pasta onde o web2py está para colocá-lo no sys.path
W2P = '/web2py/applications/'
JNKS = '/jenkins/jobs/'
PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep))
print '\nPATH='+str(PATH)

if W2P in PATH:
    W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-4])
elif JNKS in PATH:
    W2P_PATH = os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-6])
    W2P_PATH = W2P_PATH+'/web2py'
else:
    raise Exception('Problem with the PATH. Please contact an administrator!')
    sys_exit(1)

#W2P_PATH = "/docs/projects/web2py" #o comando acima pegara este caminho
sys_path_append(os_path_abspath(W2P_PATH))
print '\nW2P_PATH='+str(W2P_PATH)

# sys.path.append(os.path.abspath(W2P_PATH+'/gluon'))
# sys.path.append(os.path.abspath(W2P_PATH+'/site-packages'))
# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path_abspath(__file__).split(os_path.sep)[:-2])
# Pasta atual, onde o run_tests.py está
ROOT_PATH=os_path.dirname(__file__)
#adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
mods=['controllers','modules']
for m in mods:
    sys_path_append(os_path_abspath(PROJECT_PATH+'/'+m))

# Roda os testes da pasta test/
from unittest import TestLoader, TextTestRunner
if __name__=='__main__':
    # Pega todos os arquivos da pasta corrente que sejam .py
    tests=TestLoader().discover(ROOT_PATH,"*.py")
    # Roda os testes
    # verbosity=2 aumenta o nível de detalhe da saida
    result=TextTestRunner(verbosity=2).run(tests) 
    #result = TextTestRunner().run(tests)
    # Se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys_exit(1)