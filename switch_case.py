# Exemplo de uso do switch case em Python (somente Python 3.10+)
lang = input('Qual linguagem de programação deseja aprender? ')

match lang:
    case 'Javascript':
        print('Você pode ser um desenvolvedor web.')
    case 'PHP':
        print('Você pode ser um desenvolvedor web backend.')
    case 'Python':
        print('Você pode ser um cientista de dados.')
    case 'Java':
        print('Você pode ser um desenvolvedor mobile.')
