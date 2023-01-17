# progressão aritmética com while

prim_termo = int(input ('Digite aqui o primeiro termo da progressão aritmética: ') )
razao = int( input ('Digite aqui a razão: '))
qnt = int(input('Insira aqui quantas casas da razão deseja saber: '))
cont = 1
while cont < qnt:
    cont += 1
    print (prim_termo, end= ' - ') 
    prim_termo = prim_termo + razao
    
print (prim_termo)
resp = str(input('Deseja saber mais numeros? S/N: '))
while resp is 's':
    cont = 1
    resp1 = int(input ('Digite aqui quantas casas a mais: '))
    while cont < resp1:
        cont += 1
        print (prim_termo, end=' - ')
        prim_termo = prim_termo + razao
    print (prim_termo)
if resp == 'n':
    print ('Finalizando...')