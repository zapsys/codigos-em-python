# Algoritmo que imprime os 10 primeiros termos da sequência de Fibonacci
# Valores a serem impressos: 1 1 2 3 5 8 13 21 34 55

cont = 0  # Variável contadora do laço de repetição
n_atual = 1  # Variável que armazena o termo atual da sequência (inicia com 1)
n_anter = 1  # Variável que armazena o termo anterior da sequência (inicia com 1)
soma = 1  # Variável que armazena a soma do termo atual + anterior

while cont < 10:
    n_anter = n_atual
    n_atual = soma
    soma = n_atual + n_anter
    cont += 1  # Incrementa o contador a cada repetição
    print(n_anter)
