lista_produtos = ['airpod', 'imac', 'ipad', 'iphone']
precos = [2000, 5000, 1000, 7000]

dic_produtos = {'airpod': 2000, 'imac': 5000, 'ipad':1000, 'iphone':7000}

print(dic_produtos['airpod'])

dic_produtos['imac'] = 11000
print(dic_produtos['imac'])

print(len(dic_produtos))

dic_produtos.pop('airpod')
print(dic_produtos)

dic_produtos['apple watch'] = 6000
print(dic_produtos)

if 'iphone' in dic_produtos:
    print('Existe')
else:
    print('Não existe')

if 9000 in dic_produtos.values():
    print('Existe')
else:
    print('Não existe')

nome = input('Nome do produto: ')
nome = nome.lower()

preco_produto = float(input('Preço do produto: '))

dic_produtos[nome] = preco_produto
print(dic_produtos)

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 0.1
    dic_produtos[produto] = novo_preco
    print(novo_preco)