# -*- coding: utf-8 -*-

class Edad():

	def __init__(self):
		self.descripcion = ''

	def soy(self):
		return self.descripcion
		
	def evaluar(self, edad):
		try:
			edad = int(edad)
			if(edad < 0):
				self.descripcion = 'No existo'
			elif(edad < 13):
				self.descripcion = 'Eres un ninio'
			elif(edad < 18):
				self.descripcion = 'Eres un adolesente'
			elif(edad < 65):
				self.descripcion = 'Eres un adulto'
			elif(edad < 120):
				self.descripcion = 'Eres un adulto mayor'
			else:
				self.descripcion = 'Eres Mumm-Ra'
		except:
			self.descripcion = 'Que eres?'