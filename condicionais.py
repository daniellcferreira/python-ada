#ESTRUTURAS CONDICIONAIS

idade = 16
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')



media = float(input('Informe a media do estudante: '))
if media >= 7:
    print('Você foi Aprovado')
elif media >= 5:
    print('Você foi para a Recuperação')
else:
    print('Você foi Reprovado')



media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')