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
		#inicializarDb(carros)
		#construirDependencias()
	# def tearDown(self):
	# 	# truncate apaga todos os registros e começa a contar os ids a partir do 1 novamente
	# 	for table_name in carros.db.tables():
	# 		carros.db[table_name].truncate()
	# 	carros.db.commit()
	def test_cfib(self):
		# inicializarDb(carros)
		self.assertEqual(default.cfib()['message'],'55')
	def test_text(self):
		self.assertEqual(default.ctext()['text'],'Text')

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py

# def inicializarDb(foo):
# 	# o id dos registros começam do 1
# 	id_marca1 = foo.db.marca.insert(nome="marca1")
# 	id_marca2 = foo.db.marca.insert(nome="marca2")
# 	foo.db.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,estado="Novo",
# 						cor="Preto",valor=30000,descr="um carro preto novo",
# 						itens=['item1','item2'])
# 	foo.db.carro.insert(marca=id_marca2,modelo="modelo2",ano=1950,estado="Usado",
# 						cor="Azul",valor=20000,descr="um carro azul usado",
# 						itens=['item3'])

# def construirDependencias():
# 	default.db = carros.db = DB_CARROS
# 	default.request = carros.request
# 	default.response = carros.response
# 	default.session = carros.session
# 	default.cache = carros.cache
# 	vitrine.Moeda=_web2py_brasil_utils.Moeda
# 	default.VITRINE=vitrine.VITRINE

# def row_with_result_test(self,row,result):
# 	self.assertEqual(True,self.inside(default.URL('detalhes', args=row.id),result['vitrine']))
# 	self.assertEqual(True,self.inside(row.marca,result['vitrine']))
# 	self.assertEqual(True,self.inside(row.modelo,result['vitrine']))
# 	self.assertEqual(True,self.inside(row.ano,result['vitrine']))
# 	self.assertEqual(True,self.inside(row.estado,result['vitrine']))
# 	self.assertEqual(True,self.inside(row.cor,result['vitrine']))
# 	for item in row.itens:
# 		self.assertEqual(True,self.inside(item,result['vitrine']))	
# 	self.assertEqual(True,self.inside(row.descr,result['vitrine']))
# 	self.assertEqual(True,self.inside(_web2py_brasil_utils.Moeda(row.valor),result['vitrine']))

# # serve somente para verificar os registros existentes no inicializarDB
# def verificarRegistros(self):
# 	inicializarDb(carros)
# 	query=default.db.carro.id>0
# 	rows=default.db(query).select(orderby=default.db.carro.id) 
# 	for r in rows:
# 		print r
# 		print '\n'
# 	self.assertEqual('55','55')