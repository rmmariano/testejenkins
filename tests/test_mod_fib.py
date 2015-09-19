import sys
import os

#PROJECT_PATH - pasta anterior a pasta atual
PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
#ROOT_PATH - pasta atual, onde o run_tests.py esta
ROOT_PATH = os.path.dirname(__file__)
#faz o sys.path apontar para a pasta modules, para que possa ser feito o import do modulo fib.py
sys.path.append(os.path.abspath(PROJECT_PATH+"/modules"))

import fib
from unittest import TestCase, main

class TestFib(TestCase):
	def test0(self):
		self.assertEqual(fib.fib(1), 1)
	def test1(self):
		self.assertEqual(fib.fib(2), 1)
	def test10(self):
		self.assertEqual(fib.fib(10), 55)

if __name__ ==  '__main__':
	main()