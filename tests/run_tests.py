#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# para rodar os testes: 
# - no shell entre na pasta tests/
# - execute: python run_tests.py
# assim este arquivo de encarregara de rodar os testes nesta pasta tests/
#

#salva os caminhos das pastas que serao testadas no sys.path

import sys
import os
# W2P_PATH - pasta que fica localizado o web2py
W2P_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-4])
#W2P_PATH = "/home/rodrigo/Arquivos/web2py" #o comando acima pegara este caminho
sys.path.append(os.path.abspath(W2P_PATH))
sys.path.append(os.path.abspath(W2P_PATH+'/gluon'))
sys.path.append(os.path.abspath(W2P_PATH+'/site-packages'))
# PROJECT_PATH - pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
# ROOT_PATH - pasta atual, onde o run_tests.py esta
ROOT_PATH = os.path.dirname(__file__)
#adiciona no sys.path os diretorios que contem arquivos ou modulos a serem testados
mods=['controllers','modules']
for m in mods:
    sys.path.append(os.path.abspath(PROJECT_PATH+'/'+m))

#roda os testes da pasta test/

from unittest import TestLoader, TextTestRunner
if __name__ == '__main__':
    #pega todos os arquivos da pasta corrente que sejam .py
    tests = TestLoader().discover(ROOT_PATH, "*.py")
    #roda os testes
    #result = TextTestRunner(verbosity=2).run(tests) #verbosity=2 aumenta o nivel de detalhe da said
    result = TextTestRunner().run(tests)
    #se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys.exit(1)


# #
# #
# # from gluon import *
#     import gluon.languages.translator as T 
#     from gluon.cache import Cache 
#     from gluon.contrib.gql import GQLDB 
#     from gluon.globals import Request 
#     from gluon.globals import Response 
#     from gluon.globals import Session 
#     from gluon.html import * 
#     from gluon.http import HTTP 
#     from gluon.http import redirect 
#     from gluon.sql import DAL 
#     from gluon.sql import Field 
#     from gluon.sql import SQLDB 
#     from gluon.sqlhtml import SQLFORM 
#     from gluon.validators import * 
#     cache = Cache() 
#     request = Request() 
#     response = Response() 
#     session = Session() 
# #
# #