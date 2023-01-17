lista1 = list()
while True:
    num = (int(input('Digite um numero: ')))
    if num not in lista1:
        lista1.append(num)
        print('Valor adicionado!')
    else: print ('Valor repetido, não vou adicionar!')
    resp = str(input('Deseja continuar? S/N: ')).strip().lower()[0]
    if resp == 'n':
        print (sorted(lista1))
        break

##Solução com sorted
lista = list()
for l in range (1,6):
    resp = int(input('Digite um numero: '))
    lista.append(resp)
print (sorted(lista))