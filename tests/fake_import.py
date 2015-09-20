#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fazer objetos fakes de: request, response, session, cache e T
# pois sao objetos globais

from mock import Mock

# objeto fake do T
def foo(f):
	return f

#quando T() for chamado, sera retornado o valor que entrar
T = Mock(side_effect = foo)

# objeto fake do cache
cache = Mock()

# objeto fake do request
request = Mock()

# objeto fake do session
session = Mock()

# objeto fake do session
session = Mock()