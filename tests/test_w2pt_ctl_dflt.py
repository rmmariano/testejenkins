#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa a classe de teste W2PTestCase do pacote w2ptests
from w2ptests import W2PTestCase

# Importa o controlador que será testado
import default

# Testes relacionado ao Controlador Default
class TestCtlDefault(W2PTestCase):
	def setUp(self):
		# Chama o metodo do setUp() do W2PTestCase para inicializar os mocks
		# passando apos o self os controllers que serao testados
		W2PTestCase.setUp(self,default)
		# construirDependencias()
	def test_cfib(self):
		# inicializarDb(default.db)
		self.assertEqual(default.cfib()['message'],'55')
	def test_text(self):
		self.assertEqual(default.ctext()['text'],'Text')

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py

# def inicializarDb(__db__):
# 	id_marca1 = __db__.marca.insert(nome="marca1")
# 	id_marca2 = __db__.marca.insert(nome="marca2")

# 	__db__.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,estado="Novo",
# 						cor="Preto",valor=30000,descr="um carro preto novo",
# 						itens=['item1','item2'])
# 	__db__.carro.insert(marca=id_marca2,modelo="modelo2",ano=1950,estado="Usado",
# 						cor="Azul",valor=20000,descr="um carro azul usado",
# 						itens=['item3'])

# def construirDependencias():
# 	default.db=carros.db
# 	vitrine.Moeda=_web2py_brasil_utils.Moeda
# 	default.VITRINE=vitrine.VITRINE