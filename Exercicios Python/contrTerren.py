def area(larg,comp):
    a = larg*comp  
    print (f'A largura {l}m e o comprimento {c}m tem uma area de {a}m')

print('-=' *30)
print('Controle de Terrenos')
print('-=' *30)
l = float(input('Digite aqui a LARGURA: (m)'))
c = float(input('Digite aqui a COMPRIMENTO: (m)'))
area(l,c)