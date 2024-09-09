# Algoritmo para conversão de um número decimal inteiro em binário

num = int(input('Informe um número decimal inteiro: '))


# Função para converter um número decimal para binário
# Uso da função interna bin()
def decimalToBinary(num):
    return bin(num).replace('0b', '')


print(f'A representação binária do número {num} é:', decimalToBinary(num))
