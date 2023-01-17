## Progressão Aritmética 

prim_termo = int(input ('Digite aqui o primeiro termo da progressão aritmética: ') )
razao = int( input ('Digite aqui a razão: '))
cont = 0
for c in range (prim_termo, 150 ,razao):
    cont = cont + 1
    if cont <= 10:
        print (c, end=' ')
    else: break