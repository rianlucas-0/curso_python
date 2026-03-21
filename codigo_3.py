# Inputs
# email = input('Escreva seu email: ')
# nome = input('Escreva seu nome: ')
# print(f'{nome}, verifique o email enviado em: {email}')

# Listas
vendas = [100, 20, 45, 67, 98, 40]

total_vendas = sum(vendas) # Soma todos os elementos da lista
print(total_vendas)

quantidade_vendas = len(vendas)
print(quantidade_vendas)

print(f'O maior valor é: {max(vendas)}') # Maior valor da lista
print(f'O menor valor é: {min(vendas)}') # Menor valor da lista

print(vendas[0])

lista_produtos = ['iphone', 'ipad', 'macbook', 'imac']

# produto_procurado = input('Digite o produto que deseja buscar: ')
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)



# Adicionar um item
lista_produtos.append('apple watch')
print(lista_produtos)

# Remover um item
lista_produtos.remove('apple watch') # .remove você passa o nome do item .pop passa a posição do item na lista
print(lista_produtos)

# Editar um item
precos_produtos = [1000, 2000, 3500]
precos_produtos[0] = precos_produtos[0] * 1.5
print(precos_produtos)

# Contar quantas vezes um item aparece na lista
lista_produtos = ['iphone', 'ipad','iphone','imac', 'macbook', 'imac','iphone']
print(lista_produtos.count('iphone')) # Conta quantas vezes um item aparece

# Ordenar uma lista
lista_produtos.sort(reverse=True)
print(lista_produtos)