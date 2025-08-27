# Armazene o maior número atual aqui.
maior_numero = -999999999

# Insira o primeiro valor.
numero = int(input("Digite um número ou digite 0 para parar: "))

# Se o número não for igual a -1, continue.
while numero != 0:
    # O número é maior que o maior_número?
    if numero > maior_numero:
        # Sim, atualize o maior_número.
        maior_numero = numero
    # Insira o próximo número.
    numero = int(input("Digite um número ou digite 0 para parar: "))

# Imprima o maior número.
print("O maior número é:", maior_numero)
