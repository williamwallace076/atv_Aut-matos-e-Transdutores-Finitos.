import re

def automato_computador(texto):
		estado = 0
		posicoes = []
		casamentosExatos = []
		# Função de transição (delta) que descreve o autômato
		transicoes = [
				{'c': 1},          # q0 -> q1 com 'c'
				{'o': 2},          # q1 -> q2 com 'o'
				{'m': 3},          # q2 -> q3 com 'm'
				{'p': 4},          # q3 -> q4 com 'p'
				{'u': 5},          # q4 -> q5 com 'u'
				{'t': 6},          # q5 -> q6 com 't'
				{'a': 7},          # q6 -> q7 com 'a'
				{'d': 8},          # q7 -> q8 com 'd'
				{'o': 9},          # q8 -> q9 com 'o'
				{'r': 0}           # q9 -> q0 com 'r' (volta ao estado inicial para continuar buscando)
		] 
		# Percorrendo cada caractere do texto
		for i in range(len(texto)):
				char = texto[i]
				# Verificando se existe uma transição no estado atual para o caractere
				if char in transicoes[estado]:
						estado = transicoes[estado][char]
				else:
						estado = 0  # Reinicia se não houver correspondência
				# Se chegamos ao estado final (q9), encontramos uma ocorrência da palavra
				if estado == 9:
						posicoes.append(i + 1)  # Marca um casamento da palavra "computador"
						estado = 0  # Reinicia o estado para continuar buscando
						# Verifica se o próximo caractere está disponível
						if i + 2 < len(texto):
								# Verifica se o próximo caractere não é uma letra
								if not re.match(r'[a-zA-Z]', texto[i + 2]):
										# Verifica se o caractere anterior não é uma letra
										if not re.match(r'[a-zA-Z]', texto[(i - len("computador"))+1]):
												casamentosExatos.append(i + 1)  # Marca casamento exato da palavra computador

		return {'posicoes': posicoes, 'casamentos_exatos': casamentosExatos}
