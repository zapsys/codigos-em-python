# Exemplo função área (quadrado ou retângulo) com dois parâmetros
def area(x, y):
    if x == y:
        area = x * x
        return print('A aŕea é igual a %.2f u.a. A figura é um quadrado.' % area)
    else:
        area = x * y
        return print('A aŕea é igual a %.2f u.a. A figura é um retângulo.' % area)


# Chamada da função para mostrar o resultado. Passar os lados como parâmetros
area(1, 1)
