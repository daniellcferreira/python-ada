# DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome' : 'Daniel', 'idade' : 35, 'altura' : 1.79}
print(dicionario)
print(dicionario['idade'])


# Adicionando elementos em um dicionario

dicionario['programador'] = True
print(dicionario)


# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])


# Testando a exitencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)