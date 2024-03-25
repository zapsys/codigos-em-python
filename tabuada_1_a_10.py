# Impressão das tabuadas de 1 a 10 usando as classes internas 'list' e 'range'
A = list(range(1, 11))
for i in A:
    print(f' Tabuada do {i}')
    print('----------------')
    for j in A:
        print(f'  {i} x {j} = {i * j}\n')
