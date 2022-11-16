import os

# Definição de variáveis como strings
cpf = '08231675345'
senha = '1234'

# Definição de um vetor de strings com 2 posições
a = ['','']

# O primeiro índice (a[0]) armazena o cpf e o segundo (a[1]) armazena a senha
# Laço de repetição while que solicita as entradas
while (a[0] != cpf or a[1] != senha):
    os.system('clear')                  # Limpa o terminal
    a[0] = input('Digite seu CPF: ')    # Solicita o CPF
    a[1] = input('Senha: ')        # Solicita a senha
else:
    print('Seja bem vindo!')            # Se as condições foram satisfeitas
