# Representação da função do segundo grau y = x^2 (Parábola)

# Uso da biblioteca 'mathplotlib' para gerar e 'PyQt6' para renderizar o gráfico

import matplotlib.pyplot as graph

# Eixo x, lista de valores. Lista vazia
a = []

# Eixo y, lista de valores. Lista vazia
b = []

for x in range(-10, 11, 1):  # varia x de -10 até 10 com passo de 1 unidade
    y = x * x    # Valores de y calculados em função de x
    a.append(x)  # Cria a lista de valores de x
    b.append(y)  # Cria a lista de valores de y

# Plotando os pontos adicionando marcador em forma de círculo
graph.plot(a, b, marker="o")

# Setando a escala dos eixos
graph.xticks(range(-10, 11, 2))  # de -10 até 10 com passo de 2 unidades
graph.yticks(range(0, 111, 10))  # de 0 até 110 com passo de 10 unidades

# Definindo os limites do gráfico
graph.xlim(-11, 11)
graph.ylim(0, 110)

# Mostra o grid no gráfico com o linhas tracejadas
graph.grid(linestyle='-.')

# Nome do eixo x
graph.xlabel('x')

# Nome do eixo y
graph.ylabel('y = f(x)')

# Título para o gráfico
graph.title('Função y = x^2')

# Chamando a função 'show' para mostrar o gráfico
graph.show()
