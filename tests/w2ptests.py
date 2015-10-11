#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cria os falsos objetos de: request, response, session, cache e T,
# pois são os objetos globais principais do web2py.

# TODO: colocar os demais objetos globais aqui.

# importa o TestCase, para a criacao do W2PTestCase
from unittest import TestCase

# importa o Mock, para a criação dos objetos falsos.
from mock import Mock

# objeto fake do T
def __T__(f):
	return f

# W2PTestCase herda da TestCase
class W2PTestCase(TestCase):
	# Inicia os atributos do W2PTestCase, criando os mocks necessarios para os
	# imports automaticos do web2py
	def setUp(self,*controllers):
		for c in controllers:
			# Quando T() for chamado, será retornado o valor que entrar, porque não é necessário
			# testar a funcionalidade do T(), pois é uma função do sistema, não do desenvolvedor.
			c.T=Mock(side_effect=__T__)
			# objeto fake do cache
			c.cache=Mock()
			# objeto fake do request
			c.request=Mock()
			# objeto fake do response
			c.response=Mock()
			# objeto fake do session
			c.session=Mock()



# #
# #
# # Alguns imports globais do web2py

# # Ja feitos
# import gluon.languages.translator as T 
# from gluon.cache import Cache 
# from gluon.globals import Request 
# from gluon.globals import Response 
# from gluon.globals import Session  
# request = Request() #request = Request({})
# cache = Cache() #cache = Cache(request)
# response = Response() #funciona sem parametro
# session = Session()  #funciona sem parametro

# from gluon.contrib.gql import GQLDB #error
# from gluon.html import * 
# from gluon.http import HTTP 
# from gluon.http import redirect 
# from gluon.sql import DAL 
# from gluon.sql import Field 
# from gluon.sql import SQLDB 
# from gluon.sqlhtml import SQLFORM 
# from gluon.validators import * 

# #
# #