# Cálculo do MDC (máximo divisor comum) entre dois números inteiros positivos

# Entrada dos valores para verificar
n1 = int(input('Informe o primeiro número inteiro positivo: '))
n2 = int(input('Informe o segundo número inteiro positivo: '))


# Definição da função
def MDC():
    mdc = 1  # Definindo a variável mdc como 1 (mínimo)

    if n1 > n2:  # se n1 é maior que n2 define n = n1
        n = n1
    else:  # senão define n = n2
        n = n2
    for i in range(1, n):  # itera valores de i de 1 até n (maior número)
        resto_1 = n1 % i  # resto da divisão de n1 por i
        resto_2 = n2 % i  # resto da divisão de n2 por i

        if resto_1 == 0 and resto_2 == 0:  # se os restos forem maior que 0
            if i > mdc:  # se i for maior que o mdc definido (= 1)
                mdc = i  # mdc assume o valor de i
    return print(f'O MDC entre {n1} e {n2} é: {mdc}')


# Chamada da função
MDC()
