# Exemplo de definição de um vetor usando laço 'for'
# Um vetor é um conjunto de valores, do mesmo tipo (número, caractere, objeto)
# Pode-se se ter vetores do tipo linha ou coluna

A = [None] * 10  # Vetor A com 10 posiçõs sem elementos definidos

"""
Vetor linha com 10 elementos (0 a 9)
Necessidade de usar a classe 'range' (intervalo) e
a função 'len' para obter o tamanho do vetor
"""
for col in range(len(A)):  # A classe range inicia em 0 e o passo padrão é igual a 1
    A[col] = col
print(A)
