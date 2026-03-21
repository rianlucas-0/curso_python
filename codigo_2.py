email = 'rianlucas@gmail.com'

faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f'Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}')

email_cliente = 'teste@gmail.com'
email_cliente = email_cliente.upper() # Upper Case - Deixa tudo maiusculo

email_cliente = email_cliente.lower() # Lower Case - Deixa tudo minusculo
print(email_cliente)

print(email_cliente.find('@')) # Procura algo especifico na string

print(len(email_cliente)) # Armazena o tamanho da string

print(email_cliente[0]) # Pega o valor que estiver na posição dos []
print(email_cliente[:4]) # Pega o valor da posição 0 até a posição passada nos []

novo_email = email_cliente.replace('gmail.com', 'hotmail.com') # Substitui partes da string
print(novo_email)

nome = 'rian lucas'

print(nome.capitalize()) # Deixa a primeira letra da primeira palavra maiuscula
print(nome.title()) # Deixa a primeira letra de todas as palavras em maiusculo

