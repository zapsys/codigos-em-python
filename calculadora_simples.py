# importação de módulos
import operator
import os

# definição das operações (ações)
acao = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}
# atribui o valor inicial da variável 'opcao'
opcao = 'S'

# laço de repetição enquanto opcao = 'S' ou 's'
while opcao == 'S' or opcao == 's':
    os.system("clear")  # limpa o terminal (no Windows use cls)
    n1 = float(input("Entre com o primeiro número: "))  # recebe o primeiro número
    n2 = float(input("Entre com o segundo número: "))  # recebe o segundo número
    sinal = str(input("Informe a operação: "))  # recebe o sinal da operação
    while n2 == 0 and sinal == '/':  # enquanto n2 = 0 e a operação for divisão
        print("\nDivisão por zero não é possível")  # informa que a divisão por zero não é possível
        print("Tente outro número!\n")
        n2 = float(
            input("Entre com o segundo número: ")
        )  # solicita para informar n2 novamente
        os.system("clear")
    resposta = acao[sinal](n1, n2)  # define a resposta na função
    print("Resposta: ", n1, sinal, n2, " = ", resposta)  # imprime a resposta da operação
    opcao = input("\nDeseja continuar (S/N)? ")  # recebe a opcao para continuar ou não
else:  # se 's' ou 'S' não for digitado na 'opcao'
    print("Operação finalizada")  # finaliza a operação (quebra o laço)
