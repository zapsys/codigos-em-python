# Algoritmo para conversão de um número decimal inteiro em binário
# Método das divisões sucessivas. Leitura dos restos

num = int(input('Informe um número inteiro: '))


def decimalToBinary(num) -> str:
    if num >= 1:
        decimalToBinary(num // 2)
    return print(num % 2, end='')


print(f'A representação binária do número {num} é: ', end='')
decimalToBinary(num)
print('')
