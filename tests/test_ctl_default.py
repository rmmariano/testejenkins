#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from fake_import import *

import default
from unittest import TestCase

class TestCtlDefault(TestCase):
	def test_cfib(self):
		self.assertEqual(default.cfib()['message'],'55')
	def test_text(self):
		self.assertEqual(default.ctext()['text'],'Text')

#nao necessita do main() aqui, pois este arquivo sera chamado pelo run_tests.py