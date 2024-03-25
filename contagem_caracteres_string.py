# Contagem de palavras e caracteres em um texto
texto = input('Informe uma palavra ou texto: ')

# O método split() remove o delimitador definido, no caso o espaço ''
# O método join retorna um novo texto é 'juntado' (.join) com o restante da string

n_texto = ''.join(texto.split())
count = 0
count_c = 0
# A variável 't' percorre todos os caracteres do texto (espaços inclusive)
for t in texto:
    count = count + 1
# A variável 'c' percorre todos os caracteres do texto (sem espaços)
for c in n_texto:
    count_c = count_c + 1
print('Quantidade de palavras: ', count - (count_c - 1))
print('Quantidade de caracteres: ', count_c)
