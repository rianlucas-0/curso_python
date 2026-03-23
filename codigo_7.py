lista_precos = [1000, 2000, 3000, 4000, 5000]

def calcula_imposto_total(preco):
    if preco <- 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(preco, ' ', imposto_total)