# -*- coding: utf-8 -*-

import unittest

from edad import Edad

class EdadTest(unittest.TestCase):

	def setUp(self):
		self.ed = Edad()

	def test_menos_10(self):
		self.ed.evaluar(-10)
		self.assertEquals(self.ed.soy(), 'No existo')

	def test_edad_5(self):
		self.ed.evaluar(5)
		self.assertEquals(self.ed.soy(), 'Eres un ninio')

	def test_edad_15(self):
		self.ed.evaluar(15)
		self.assertEquals(self.ed.soy(), 'Eres un adolesente')

	def test_edad_40(self):
		self.ed.evaluar(40)
		self.assertEquals(self.ed.soy(), 'Eres un adulto')

	def test_edad_80(self):
		self.ed.evaluar(80)
		self.assertEquals(self.ed.soy(), 'Eres un adulto mayor')

	def test_edad_150(self):
		self.ed.evaluar(150)
		self.assertEquals(self.ed.soy(), 'Eres Mumm-Ra')

	def test_edad_A(self):
		self.ed.evaluar('A')
		self.assertEquals(self.ed.soy(), 'Que eres?')

if __name__ == '__main__':
	unittest.main()