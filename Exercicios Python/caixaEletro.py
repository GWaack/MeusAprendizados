## Caixa eletronico
## valor a ser sacado
## cedulas
while True:
    #inicia variaveis
    cinq = vint = dez = um = 0

    #pergunta quanto quer sacar
    saque = int(input('Quanto deseja sacar? R$'))

    #calcula o numero de notas de 50
    cinq = saque // 50
    resto = saque % 50

    #calcula o numero de notas de 20
    vint = resto // 20
    resto = resto % 20

    #calcula o numero de notas de 10
    dez = resto // 10
    resto = resto % 10

    #calcula o numero de notas de 1
    um = resto

    print(f'Você precisará de {cinq} notas de R$50, {vint} notas de R$20, {dez} notas de R$10 e {um} notas de R$1.') 
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja sacar mais? [S/N]')).strip().lower()[0]
    if resp == 'n':
        break

print (f'Você precisara de {cinq} notas de R$50, {vint} notas de R$20, {dez} notas de R$10 e {um} notas de R$1')