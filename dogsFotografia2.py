# Uso de uma função com input para retornar as informações
def dogsFotografia():
	nome_cliente = input("Nome do cliente: ")
	nome_lugar = input("Nome do lugar: ")
	dia = int(input("Dia da semana: "))
	mes = int(input("Mês: "))
	ano = int(input("Ano: "))
	
	return print(f"\n{nome_cliente}\n{nome_lugar}\n{dia}/{mes}/{ano}\n")
	
dogsFotografia()
