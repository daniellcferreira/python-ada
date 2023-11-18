numero_sorteado = 15
numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou! Digite outro numero: ')
    numero_escolhido = int(input('Informe um numero entre 1 e 20: '))
print('Você acertou!')


#ESTRUTURA COM CONTADOR

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
