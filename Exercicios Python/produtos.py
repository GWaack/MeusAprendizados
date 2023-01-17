## ler nome e preço de varios produtos
## perguntar se quer registrar mais
## informar total gasto
## quantos custam mais de 1000
## nome do produto mais barato

print ('-*-' *10)
print ('          Registro')
print ('-*-' *10)
total = maismil = maisbara = cont = 0
barato = ' '
while True:
    nome = str(input('Insira aqui o nome do produto: '))
    preco = int(input('Insira aqui o preço desse produto: R$'))
    cont += 1
    if cont == 1 or preco < maisbara:
        maisbara = preco
        barato = nome
    if preco >= 1000:
        maismil += 1
    total = total + preco
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja registrar mais produtos? [S/N]')).strip().lower()[0]
    if resp == 'n':
        break
print (f'Acabou! total a pagar R${total} com {maismil} itens custando mais de R$1.000 e o nome do produto mais barato é {barato}')