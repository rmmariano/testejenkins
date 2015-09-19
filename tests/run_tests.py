#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# para rodar os testes: 
# - no shell entre na pasta tests/
# - execute: python run_tests.py
#

#inicializa os testes

import sys
import os
# PROJECT_PATH - pasta anterior a pasta atual
PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
# ROOT_PATH - pasta atual, onde o run_tests.py esta
ROOT_PATH = os.path.dirname(__file__)
#adiciona no sys.path os diretorios que contem arquivos ou modulos a serem testados
mods=['controllers','modules']
for m in mods:
    sys.path.append(os.path.abspath(PROJECT_PATH+'/'+m))

#roda os testes da pasta test/

import unittest
if __name__ == '__main__':
    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)

    if result.wasSuccessful():
        print result
    else:
        sys.exit(1)

'''
if __name__ == '__main__':
    if 'GAE_SDK' in os.environ:

        SDK_PATH = os.environ['GAE_SDK']

        sys.path.insert(0, SDK_PATH)

        import dev_appserver
        dev_appserver.fix_sys_path()

    sys.path.append(os.path.join(PROJECT_PATH, 'appengine'))
    sys.path.append(os.path.join(PROJECT_PATH, 'apps'))

if __name__ == '__main__':
    sys.path.append(os.path.join(ROOT_PATH, 'fibo'))
    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)

'''
