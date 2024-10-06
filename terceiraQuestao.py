from automatos import MaquinaMealy

estados = {0, 25, 75, 100}
alfabeto = {25, 50, 100}
estado_inicial = 0

funcao_transicao = {
	(0, 25): 25,
	(0, 50): 50,
	(0, 100): 100,
	(25, 25): 50,
	(25, 50): 75,
	(25, 100): 25,
	(50, 25): 75,
	(50, 50): 100,
	(50, 100): 50,
	(75, 25): 100,
	(75, 50): 25,
	(75, 100): 75,
	(100, 25): 25,
	(100, 50): 50,
	(100, 100): 100
}

funcao_saida = {
	(0, 25): 0,
	(0, 50): 0,
	(0, 100): 1,
	(25, 25): 0,
	(25, 50): 0,
	(25, 100): 1,
	(50, 25): 0,
	(50, 50): 1,
	(50, 100): 1,
	(75, 25): 1,
	(75, 50): 1,
	(75, 100): 1,
	(100, 25): 0,
	(100, 50): 0,
	(100, 100): 1
}

maquinaDeLata = MaquinaMealy(estados, alfabeto, funcao_transicao, estado_inicial, funcao_saida)
