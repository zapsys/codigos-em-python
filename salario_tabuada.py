# Cálculo reajuste salário e impressão tabuada de 1 a 10
salario = float(input('Digite o salário: '))

if (salario < 500.00):
    print(f'O valor do salário reajustado será de 15%: R$ {salario*1.15}')
elif (salario <= 1000.00):
    print(f'O valor do salário reajustado será de 10%: R$ {salario*1.10}')
else:
    print(f'O valor do salário reajustado será de 5%: R$ {salario*1.05}')
    
print('------------------------------------------------------')
#A = [1,2,3,4,5,6,7,8,9,10]
A = list(range(1,11))
for i in A:
    print(f' Tabuada do {i}')
    print('----------------')
    for j in A:
        print(f'  {i} x {j} = {i * j}\n')