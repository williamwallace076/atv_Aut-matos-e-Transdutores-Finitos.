from primeiraQuestao import aut_item_a, aut_item_b, aut_item_c, aut_item_d, testar_automato,cadeias_teste_a,cadeias_teste_b,cadeias_teste_c,cadeias_teste_d
from segundaQuestao import automato_computador
from terceiraQuestao import maquinaDeLata

def questao1():
	print("\nExecutando a questão 1...")
	print("\n--- automatos ---")
	print("a - (ab*c*)*")
	print("b - aaa(b | c)* | (b | c)* aaa")
	print("c - a*b | ab*")
	print("d - a*b* (a| ac*)")
	print("s - Sair")
	print("\n-----------------")
	
	while True:
		opcao = input("\nEscolha um automato para ser testado : ")
		if opcao == 'a':
			print("\nTestes para o automato (ab*c*)* :\n")
			testar_automato(aut_item_a, cadeias_teste_a)
		elif opcao == 'b':
			print("\nTestes para o automato aaa(b | c)* | (b | c)* aaa:\n")
			testar_automato(aut_item_b, cadeias_teste_b)
		elif opcao == 'c':
			print("\nTestes para o automato a*b | ab*:\n")
			testar_automato(aut_item_c, cadeias_teste_c)
		elif opcao == 'd':
			print("\nTestes para o automato a*b* (a| ac*):\n")
			testar_automato(aut_item_d, cadeias_teste_d)
		elif opcao == 's':
				print("Saindo do programa...")
				break
		else:
				print("Opção inválida! Por favor, escolha uma opção válida.")
	pass




def questao2():
	print("\nExecutando a questão 2...")
	# Texto fornecido
	texto = ("O computador é uma máquina capaz de variados tipos de tratamento automático de "
					 "informações ou processamento de dados. Entende-se por computador um sistema físico que "
					 "realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são "
					 "ícones da era da informação. O primeiro computador eletromecânico foi construído por "
					 "Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado "
					 "computador pessoal ou ainda computador doméstico.")

	# Executa o autômato
	resultado = automato_computador(texto)

	# Exibe as posições encontradas
	print("\nTexto: O computador é uma máquina capaz de variados tipos de tratamento automático de "
				"informações ou processamento de dados. Entende-se por computador um sistema físico que "
				"realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são "
				"ícones da era da informação. O primeiro computador eletromecânico foi construído por "
				"Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado "
				"computador pessoal ou ainda computador doméstico.")
	print(f"\nA palavra 'computador' ocorre nas posições: {resultado['posicoes']}")
	print(f"\nOs casamentos exatos ocorrem nas posições: {resultado['casamentos_exatos']}")
	pass




def questao3():
	print("\nExecutando a questão 3...")
	moedas = [25, 25, 25, 25, 100, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
	saida = maquinaDeLata.processar(moedas)

	print("\n------------------Resultado---------------")

	print(f"\ntotal: {sum(moedas)} moedas ")
	print(f"\nnumero de latas esperadas: {sum(moedas) // 100}\n")

	for index, moeda in enumerate(moedas):
		print(f"{moeda}: {saida[index]}")
	print(f"\nnumero de latas obtidas: {sum(saida)}")
	pass





def exibir_menu():
	print("\n--- Menu de Usuário ---")
	print("1. Executar Questão 1")
	print("2. Executar Questão 2")
	print("3. Executar Questão 3")
	print("0. Sair")





def main():
	while True:
			exibir_menu()
			opcao = input("\nEscolha uma opção: ")

			if opcao == '1':
					questao1()
			elif opcao == '2':
					questao2()
			elif opcao == '3':
					questao3()
			elif opcao == '0':
					print("Saindo do programa...")
					break
			else:
					print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
	main()
