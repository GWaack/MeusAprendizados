#par impar em lista
listageral = list()
listapar = list()
listaimpar = list()
while True:
    num = int(input('Digite um numero: '))
    listageral.append(num)
    if num %2 == 0:
        listapar.append(num)
    elif num %2 >= 1:
        listaimpar.append(num)
    resp = str(input('Quer continuar? S/N: ')).strip().lower()[0]
    if resp == 'n':
        break
print(listaimpar)
print(listapar)
print(listageral)