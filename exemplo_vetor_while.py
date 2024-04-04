# Exemplo de definição de um vetor usando laço 'while'
# Um vetor é um conjunto de valores, do mesmo tipo.
# Pode-se se ter vetores do tipo linha ou coluna

A = [None] * 10  # vetor A vazio com 10 elementos.

i = 0  # contador

# Vetor linha com 10 elementos (0 a 9)
while i < 10:
    A[i] = i
    i += 1  # Incrementa 1 ao valor de i
print(A)
