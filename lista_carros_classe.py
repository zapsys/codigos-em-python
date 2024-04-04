# Exemplo de definição de uma classe (POO)
class Carro:
    # Inicialização (definição dos atributos)
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


# Gerando vários objetos da classe
# laço WHILE com três objetos do tipo carro, incremento i iniciando em 1
i = 1
while i < 4:
    marca = input('Informe a marca do carro: ')
    modelo = input('Informe o modelo do carro: ')
    cor = input('Informe a cor do carro: ')
    ano = input('Informe o ano do carro: ')
    carro = Carro(marca, modelo, cor, ano)
    print()
    print('---------')
    print('Carro ', i)
    print('---------')
    print(f'{carro.marca}\n{carro.modelo}\n{carro.cor}\n{carro.ano}')
    print()
    i += 1  # Notação para incrementar i em 1 unidade a cada repetição
