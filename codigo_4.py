vendas = 2100
meta1 = 1300
meta2 = 2000

if vendas > meta2:
    print('Vendedor ganha bônus')
    bonus = vendas * 0.13
    print(f'O bônus do vendedor é de R${bonus:.0f}')
elif vendas > meta1:
    print(f'Vendedor ganha bônus maior')
    bonus = vendas * 0.1
    print(f'O bônus do vendedor é de R${bonus:.0f}')
else:
    print('Vendedor não ganha bônus')

lista_produtos = ['iphone', 'imac', 'macbook', 'airpod']
produto_procurado = input('Procure por um produto: ')
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print('existe')
else:
    print('Não existe')