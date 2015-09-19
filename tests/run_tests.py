#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
ROOT_PATH = os.path.dirname(__file__)

print PROJECT_PATH #pasta anterior a pasta atual
print ROOT_PATH #pasta atual, onde o run_tests.py esta

#sys.path.append(os.path.abspath(PROJECT_PATH))
mods=['controller','modules'] #diretorios que contem modulos a serem testados
for m in mods:
    sys.path.append(os.path.abspath(PROJECT_PATH+'/'+m))



print sys.path


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
