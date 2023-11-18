# METODOS DE LISTAS

lista = [1, 3, 12, 8, 12]

# append

lista.append(3)
print(lista)

# insert

lista.insert(2, 10)
print(lista)

# extend

lista2 = [1, 2, 3]
lista.extend(lista2)
print(lista)

# pop - indice

lista.pop()
print(lista)

lista.pop(1)
print(lista)

# remove - elemento

lista.remove(3)
print(lista)

# count

print('Quantidade de numeros 2 na lista: ', lista.count(2))

# index

print('Indice do elemento 12: ', lista.index(12))

# sort

lista.sort()
lista.sort(reverse=True)
print(lista)


# FUNÇÕES PARA LISTAS

# len

print(len(lista))

# sum

print(sum(lista))

# max 

print(max(lista))

# min

print(min(lista))


