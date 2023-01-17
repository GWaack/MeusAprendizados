lista = list()
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    resp = str(input('Quer continuar? S/N: ')).strip().lower()[0]
    if resp == 'n':
        break

print (f'existem {len(lista)} elementos em sua lista')
lista.sort(reverse = True)
print (lista)
if 5 in lista:
    print (f'Tem o valor 5 na lista na posição {lista.index(5)}º')
else: print('O valor 5 não foi encontrado na lista!')
