Feature: Quiero saber que soy
	Como usuario de la aplicacion
	deseo introducir mi edad
	para obtener la descripción de lo que soy

	Scenario: Edad -1
		Dado que ingreso la edad "-1"
		cuando realizo la operacion
		entoces obtengo la respuesta "No existo"

	Scenario: Edad 10
		Dado que ingreso la edad "10"
		cuando realizo la operacion
		entoces obtengo la respuesta "Eres un ninio"

	Scenario: Edad 17
		Dado que ingreso la edad "17"
		cuando realizo la operacion
		entoces obtengo la respuesta "Eres un adolesente"

	Scenario: Edad 20
		Dado que ingreso la edad "20"
		cuando realizo la operacion
		entoces obtengo la respuesta "Eres un adulto"

	Scenario: Edad -1
		Dado que ingreso la edad "80"
		cuando realizo la operacion
		entoces obtengo la respuesta "Eres un adulto mayor"

	Scenario: Edad 125
		Dado que ingreso la edad "125"
		cuando realizo la operacion
		entoces obtengo la respuesta "Eres Mumm-Ra"

	Scenario: Edad A
		Dado que ingreso la edad "A"
		cuando realizo la operacion
		entoces obtengo la respuesta "Que eres?"