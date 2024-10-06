class AFD():
	def __init__(self, estados, alfabeto, funcao_transicao, estado_inicial, estados_finais):
		self.estados = estados
		self.alfabeto = alfabeto
		self.funcao_transicao = funcao_transicao
		self.estado_inicial = estado_inicial
		self.estados_finais = estados_finais
		self.log_transicoes = []

	def reconhecer(self, cadeia):
		estado_atual = self.estado_inicial
		self.log_transicoes = []
		
		for simbolo in cadeia:
			if simbolo not in self.alfabeto:
				raise ValueError(f"Símbolo '{simbolo}' não pertence ao alfabeto.")

			estado_anterior = estado_atual
			estado_atual = self.funcao_transicao.get((estado_atual, simbolo))
			
			if estado_atual is None:
				self.log_transicoes.append((estado_atual, simbolo, "Transição indefinida"))
				return False
			
			self.log_transicoes.append((estado_anterior, simbolo, estado_atual))
		
		return estado_atual in self.estados_finais

	
	def log(self):
		if not self.log_transicoes:
			print("Nenhuma transição registrada.")
		else:
			print("Log de transições:")
			for transicao in self.log_transicoes:
				print(f"Estado atual: {transicao[0]}, Símbolo: '{transicao[1]}', Próximo estado: {transicao[2]}")

	def varrer(self, cadeia):
		estado_atual = self.estado_inicial
		posicoes_aceitas = []
		
		for indice, simbolo in enumerate(cadeia):
			if simbolo not in self.alfabeto:
				raise ValueError(f"Símbolo '{simbolo}' não pertence ao alfabeto.")

			estado_anterior = estado_atual
			estado_atual = self.funcao_transicao.get((estado_atual, simbolo))
			
			if estado_atual is None:
				continue
			
			if estado_atual in self.estados_finais:
				posicoes_aceitas.append(indice-10)

		return posicoes_aceitas





class MaquinaMealy:
	def __init__(self, estados, alfabeto, funcao_transicao, estado_inicial, funcao_saida):
		self.estados = estados
		self.alfabeto = alfabeto
		self.funcao_transicao = funcao_transicao
		self.estado_inicial = estado_inicial
		self.funcao_saida = funcao_saida
		self.estado_atual = estado_inicial

	def processar(self, cadeia):
		saidas = []
		self.estado_atual = self.estado_inicial

		
		for simbolo in cadeia:
			if simbolo not in self.alfabeto:
				raise ValueError(f"Símbolo '{simbolo}' não pertence ao alfabeto.")

			
			saidas.append(self.funcao_saida.get((self.estado_atual, simbolo)))

			
			self.estado_atual = self.funcao_transicao.get((self.estado_atual, simbolo))
			if self.estado_atual is None:
				raise ValueError(f"Transição indefinida para o estado '{self.estado_atual}' com o símbolo '{simbolo}'.")

		return saidas

	def resetar(self):
		self.estado_atual = self.estado_inicial

