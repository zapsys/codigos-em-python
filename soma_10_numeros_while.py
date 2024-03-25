# Soma de 10 números usando o laço 'while'

i = 0  # Inicialização do contador
soma = 0  # Inicialização da variável soma


while i < 10:
    num = int(input('Informe um número inteiro: '))  # Entrada dos números inteiros
    soma = soma + num
    i = i + 1
print('Soma dos números informados: ', soma)
