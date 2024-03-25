# Soma de 10 números usando o laço 'for'

i = 0  # Inicialização do contador
soma = 0  # Inicialização da variável soma


for i in range(0, 10):
    num = int(input('Informe um número inteiro: '))  # Entrada dos números inteiros
    soma = soma + num
    i = i + 1
print('Soma dos números informados: ', soma)
