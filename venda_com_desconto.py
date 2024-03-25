# Cálculo de desconto e valor a pagar de um produto

nome = input("Favor digite o nome da mercadoria: ")
preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valorDesconto = preco * desconto / 100
valorPagar = preco - valorDesconto

print("O percentual de desconto é de: ", desconto)
print("O valor do desconto é de: ", valorDesconto)
print(
    "O valor a ser pago pela mercadoria é de: %.2f" % valorPagar
)  # valor formatado com 2 casas decimais
