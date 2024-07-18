# Importação da função 'date'
from datetime import date

# Data atual
hoje = date.today()

# Entrada do nome
nome = input('Informe o seu nome: ')

# Entrada da data de nascimento usando a classe 'date'
print('Informe os dados de seu nascimento ')
nascimento = date(int(input('Ano: ')), int(input('Mês: ')), int(input('Dia: ')))

# Variável aniversário do tipo 'date' em relação ao ano atual
aniversario = date(hoje.year, nascimento.month, nascimento.day)

# Variável dias_aniver
dias_aniver = (aniversario - hoje).days

if (dias_aniver < 0):
    print(f'{nome}, seu aniversário foi a {-dias_aniver} atrás!')
elif (dias_aniver == 0):
    print(f'{nome}, hoje é o seu dia! Feliz aniversário!!!')
else:
    print(f'{nome}! Faltam {dias_aniver} dias para o seu aniversário!')
