'''for var in range(5):
    print(var)

for var in range(1, 5):
    print(var)

for var in range(1, 12, 3):
    print(var)'''


soma = 0
for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota
print(soma/3)