# Exemplo de definição de uma classe (POO)
class Carro:
    # Inicialização (definição dos atributos)
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


# Objeto 1 da classe
carro = Carro('Audi', 'A5', 'vermelho', '2015')

print('Carro 1')
print('-------')
print(f'{carro.marca}\n{carro.modelo}\n{carro.cor}\n{carro.ano}')
print()

# Objeto 2 da classe
carro = Carro('Wolkswagem', 'Gol', 'branco', '2008')

print('Carro 2')
print('-------')
print(f'{carro.marca}\n{carro.modelo}\n{carro.cor}\n{carro.ano}')
