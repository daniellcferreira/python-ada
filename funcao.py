# FUNÇÕES

# 1. O que são funções e por que utiliza-las?

# Funçôes ja vistas anteriormente..

# print()  - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
# input()  - Retorna um dado informado pelo usuario (entrada padrão) e pode receber uma string
# len ()  - Recebe uma lista e retorna o tamanho dessa lista
# max ()  - Retorna o maior valor da lista

# 2. Criação de Funções

# Função Inicial

def saudacao():
    print('Seja bem vindo!')
    print('Olá! é prazer ter você conosco! ')

saudacao()

# Função com parâmentros

def saudacao(nome, curso):
    print(f'Seja bem vindo, {nome}!')
    print(f'Olá! é prazer ter você conosco no curso de {curso}! ')

saudacao('Daniel', 'Ptyhon')

# Função com parâmentros defauf

def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo, {nome}!')
    print(f'Olá! é prazer ter você conosco no curso de {curso}! ')

saudacao('Daniel')

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é ', resultado)



def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    

resultado = calculadora(10, 20, '*')
print(resultado)


    