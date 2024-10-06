from automatos import AFD

# Definindo os componentes do autômato do item a da primeira questão
estados = {'q0', 'q1', 'q2'}
alfabeto = {'a', 'b', 'c'}
estado_inicial = 'q0'
estados_finais = {'q0', 'q1', 'q2'}
funcao_transicao = {
	('q0', 'a'): 'q1',
	('q1', 'a'): 'q1',
	('q1', 'b'): 'q1',
	('q1', 'c'): 'q2',
	('q2', 'a'): 'q1',
	('q2', 'c'): 'q2'
}

# Criando o autômato do item a da primeira questão
aut_item_a = AFD(estados, alfabeto, funcao_transicao, estado_inicial, estados_finais)

# Definindo os componentes do autômato do item b da primeira questão
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
alfabeto = {'a', 'b', 'c'}
estado_inicial = 'q0'
estados_finais = {'q3', 'q7'}
funcao_transicao = {
	('q0', 'a'): 'q1',
	('q0', 'b'): 'q4',
	('q0', 'c'): 'q4',
	('q1', 'a'): 'q2',
	('q2', 'a'): 'q3',
	('q3', 'b'): 'q3',
	('q3', 'c'): 'q3',
	('q4', 'a'): 'q5',
	('q4', 'b'): 'q4',
	('q4', 'c'): 'q4',
	('q5', 'a'): 'q6',
	('q6', 'a'): 'q7'
}

# Criando o autômato do item b da primeira questão
aut_item_b = AFD(estados, alfabeto, funcao_transicao, estado_inicial, estados_finais)

# Definindo os componentes do autômato do item c da primeira questão
estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'a', 'b'}
estado_inicial = 'q0'
estados_finais = {'q1', 'q3', 'q4'}
funcao_transicao = {
	('q0', 'a'): 'q1',
	('q0', 'b'): 'q3',
	('q1', 'a'): 'q2',
	('q1', 'b'): 'q4',
	('q2', 'a'): 'q2',
	('q2', 'b'): 'q3',
	('q4', 'b'): 'q4'
}

# Criando o autômato do item c da primeira questão
aut_item_c = AFD(estados, alfabeto, funcao_transicao, estado_inicial, estados_finais)


# Definindo os componentes do autômato do item d da primeira questão
estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'a', 'b', 'c'}
estado_inicial = 'q0'
estados_finais = {'q1', 'q2', 'q4'}
funcao_transicao = {
	('q0', 'a'): 'q1',
	('q0', 'b'): 'q3',
	('q1', 'a'): 'q2',
	('q1', 'b'): 'q3',
	('q1', 'c'): 'q4',
	('q2', 'a'): 'q2',
	('q2', 'b'): 'q3',
	('q2', 'c'): 'q4',
	('q3', 'a'): 'q4',
	('q3', 'b'): 'q3',
	('q4', 'c'): 'q4'
}

# Criando o autômato do item d da primeira questão
aut_item_d = AFD(estados, alfabeto, funcao_transicao, estado_inicial, estados_finais)


# Definindo as cadeias de teste
cadeias_teste_a = [
	#Cadeias Aceitas: 
		"",          # Cadeia vazia
		"a",         # Cadeia que contém apenas 'a'
		"abc",       # Cadeia que contém apenas 'abc'
		"ab",        # Cadeia sem 'c'
		"ac",        # Cadeia sem 'b'
		"abbbbbb",   # Cadeia com 'b' repetido muitas vezes
		"acccccc",   # Cadeia com 'c' repetido muitas vezes 
		"abbbbccc",  # Cadeia com 'b' e 'c' repetidos muitas vezes   

	#Cadeias Rejeitadas:

		"b",         # Cadeia que contém apenas 'b'
		"c",         # Cadeia que contém apenas 'c'
		"ccccccc",   # Cadeia com 'c' repetido muitas vezes
		"bbbbbbb",   # Cadeia com 'b' repetido muitas vezes
		"bbbbccc",   # Cadeia com 'b' e 'c' repetidos muitas vezes
		"bcbcbcb",	 # Cadeia de 'b' e 'c' alternando
		"abcbcbc",	 # Cadeia começando com 'a' de 'b' e 'c' alternando"
]

cadeias_teste_b = [
	#Cadeias Aceitas:
		"aaa", 			 # Cadeia com "aaa"
		"aaabbbb", 	 # Cadeia com "aab"
		"aaacccc", 	 # Cadeia com "aac"
		"aaaccbcbc", # Cadeia com "aaa" e 'b', 'c' alternando
		"bbbbaaa",   # Cadeia começa com "bbb" e termina com "aaa"
		"ccccaaa",   # Cadeia começa com "ccc" e termina com "aaa"
		"bbbcbcaaa", # Cadeia começa com "bbb" e termina com "aaa" e 'b', 'c' alternando

	#Cadeias Rejeitadas:
		"" ,         # Cadeia vazia	
		"a",				 # Cadeia com "a"
		"aa" ,       # Cadeia com "aa"
		"aaaabcbc",  # Cadeia com "aaa" e 'b', 'c' alternando
		"bbbccca",   # Cadeia termina com apenas um 'a'
		"cbbccaa",   # Cadeia começa com apenas dois 'aa'
		"cbaabcc",   # Cadeia apresenta "aa" no meio 
]

cadeias_teste_c = [
	#Cadeias Aceitas:
		"b",    		 # Cadeia com "b"
		"a",    		 # Cadeia com "a"
		"aaaaab",	 	 # Cadeia começa com varios 'a' e termina com 'b'
		"abbbbb",	 	 # Cadeia começa com 'a' e termina com varios 'b'
		"ab",				 # Cadeia simples 'ab'
		"aaab",			 # Cadeia começa com 'a' e termina com 'b'
		"abbb",			 # Cadeia começa com 'a' e termina com três 'b'

	#Cadeias Rejeitadas:
		"",  				 # Cadeia vazia
		"bbbbbbbb",	 # Cadeia com varios "b"
		"aaaaaaaa",	 # Cadeia com varios "a"
		"abababab",	 # Cadeia com varios "ab"
		"bbbaaa",	   # Cadeia começa com 'b' e termina com 'a'"
		"ba",				 # Cadeia simples começando com 'b' e terminando com 'a'
		"bbaaaabb",  # Cadeia começa com 'b' e termina com 'a' e 'b'"
]

cadeias_teste_d = [
	#Cadeias Aceitas:
		"a",          # Cadeia simples
		"aa",         # Cadeia que contém apenas 'a'
		"aaaaa",      # Cadeia com muitas ocorrências de 'a'
		"aac",				# Cadeia com 'a' e 'c'
		"aabba",			# Cadeia com 'a' e 'b' alternando
		"abac",				# Cadeia com 'a', 'b' e 'c' alternando"
		"aaabbbaccc", # Cadeia com 'a', 'b', 'c' alternando e 'a', 'b' e 'c

	# Cadeias Rejeitadas:
		"abc",        # Cadeia que contém 'a', 'b' e 'c'
		"bca",        # Cadeia começando com 'b'
		"cccc",       # Cadeia com repetições de 'c'
		"aabbcc",     # Cadeia com múltiplos 'a', 'b' e 'c'
		"acb",        # Cadeia com 'a', 'c' e 'b' em ordem diferente
		"bc", 				# Cadeia com 'b' e 'c'
		"",						# Cadeia vazia
]

# Função para testar as cadeias em um autômato específico
def testar_automato(aut, cadeias):
		print(f"Testando autômato {aut}")
		for cadeia in cadeias:
				resultado = aut.reconhecer(cadeia)
				print(f"Cadeia '{cadeia}': {'Aceita' if resultado else 'Rejeitada'}")

# Testando todas as cadeias em cada autômato
print("Testes para o item a:")
testar_automato(aut_item_a, cadeias_teste_a)

print("\nTestes para o item b:")
testar_automato(aut_item_b, cadeias_teste_b)

print("\nTestes para o item c:")
testar_automato(aut_item_c, cadeias_teste_c)

print("\nTestes para o item d:")
testar_automato(aut_item_d, cadeias_teste_d)
