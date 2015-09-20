#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fib
from unittest import TestCase

class TestFib(TestCase):
	def test0(self):
		self.assertEqual(fib.fib(1), 1)
	def test1(self):
		self.assertEqual(fib.fib(2), 1)
	def test10(self):
		self.assertEqual(fib.fib(10), 55)

#nao necessita do main() aqui, pois este arquivo sera chamado pelo run_tests.py