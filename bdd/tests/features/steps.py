# -*- coding: utf-8 -*-
from lettuce import step, world
from edad import Edad

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, entrada):
    world.edad = Edad()
    world.edad.evaluar(entrada)
@step(u'entoces obtengo la respuesta "([^"]*)"')
def entoces_obtengo_la_respuesta_group1(step, esperado):
    obtenido =  world.edad.soy()
    assert esperado == obtenido, 'El resultado esperado es' + esperado + ' y el obtenido es ' + obtenido
