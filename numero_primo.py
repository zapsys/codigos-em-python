# Algoritmo para verificar se um número é primo ou não e mostrar seus divisores
# Um número primo é divisível por 1 e ele mesmo, ou seja, 2 divisores

n = int(input('Informe um número inteiro: '))

# Variável para contar o divisores
count = 0

# Variável de controle
i = 1

print('----------------------')
print(f'Divisores de {n}: ')
print('----------------------')
while i <= n:
    if (n % i) == 0:
        count = count + 1
        div = int(n / i)  # Variável para armazenar os divisores
        print(div)
    i = i + 1
print('----------------------')
if count < 2 or count > 2:
    print(f'O número {n} não é primo')
else:
    print(f'O número {n} é primo')
