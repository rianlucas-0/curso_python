lista_vendas = [1000, 3000, 50, 3000, 4000, 7000]

meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0
    print('R$ ', bonus)