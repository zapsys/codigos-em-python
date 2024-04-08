# Algoritmo que imprime a soma de todos os números inteiros de
# 1 a 100: 1 + 2 + 3 + 4 + 5 + ... + 99 + 100

cont = 1  # Contador
soma = 0  # Soma inicial
termo = 1  # Primeiro termo igual a 1

while cont <= 100:
    soma = soma + termo
    cont += 1  # Incrementa o contador em 1 unidade a cada repetição
    termo += 1  # Incrementa o termo em 1 unidade a cada repetição
print(soma)
