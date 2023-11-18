# LISTAS

# antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com listas

notas = [7.9, 9.7, 8.2]

# criando lista

lista = []
lista = list()
lista = ['Daniel', 35, 1.78, True]
listas_de_lista = [10, [1, 2, 3]]


# INDEXAÇÃO E SLICES (FATIAMENTO)

lista = ['Daniel', 35, 1.78, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])


# INTERAÇÃO COM FOR

# 1. Utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os indices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(i)

    