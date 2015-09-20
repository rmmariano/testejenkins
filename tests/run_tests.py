#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# para rodar os testes: 
# - no shell entre na pasta tests/
# - execute: python run_tests.py
#

#salva os caminhos das pastas que serao testadas no sys.path

import sys
import os
# W2P_PATH - pasta que fica localizado o web2py
W2P_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-4])
sys.path.append(os.path.abspath(W2P_PATH))
print W2P_PATH
print sys.path
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
    result = TextTestRunner().run(tests)
    #se houver algum problema nos testes, fecha o programa
    if not result.wasSuccessful():
        sys.exit(1)