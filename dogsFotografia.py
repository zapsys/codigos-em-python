# Declaração direta das variáveis
"""
nome_cliente = "Pablo Augusto"
nome_lugar = "Lago Azul"
dia = 20
mes = 5
ano = 2019

print(nome_cliente)
print(nome_lugar)
print(f"{dia}/{mes}/{ano}")
"""
# Ou via função
def dogsFotografia():
	nome_cliente = "Pablo Augusto"
	nome_lugar = "Lago Azul"
	dia = 20
	mes = 5
	ano = 2019
	
	return print(f"{nome_cliente}\n{nome_lugar}\n{dia}/{mes}/{ano}")
	
dogsFotografia()
