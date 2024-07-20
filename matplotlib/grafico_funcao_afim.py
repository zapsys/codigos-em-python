# Representação da função da reta y = x (Função Afim)

# Uso da biblioteca 'mathplotlib' para gerar e 'PyQt6' para renderizar o gráfico

import matplotlib.pyplot as graph

# Eixo x, lista de valores
x = [0, 1, 2, 3, 4, 5, 6]

# Eixo y, lista de valores, no caso igual a x
y = x

# Definindo os limites do gráfico
graph.xlim(0, 6)
graph.ylim(0, 6)

# Plotando os pontos
graph.plot(x, y)

# Mostra o grid no gráfico com o linhas tracejadas
graph.grid(linestyle='--')

# Nome do eixo x
graph.xlabel('x')

# Nome do eixo y
graph.ylabel('y = f(x)')

# Título para o gráfico
graph.title('Função y = x')

# Chamando a função 'show' para mostrar o gráfico
graph.show()
