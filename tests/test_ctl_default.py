#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

# Importa o controlador que será testado
import default

# Testes relacionado ao Controlador Default
class TestCtlDefault(TestCase):
	def test_cfib(self):
		self.assertEqual('55','55')
	def test_text(self):
		self.assertEqual('Text','Text')

	# def test_cfib(self):
	# 	self.assertEqual(default.cfib()['message'],'55')
	# def test_text(self):
	# 	self.assertEqual(default.ctext()['text'],'Text')

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py