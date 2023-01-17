## Numeros primos

num = int(input ('Digite aqui um numero para saber se é primo: '))
cont = 0
for c in range (1, num + 1):
    if num % c == 0:
        cont += 1
        
if cont >= 3:
    print ('Este não é um numero primo')
else:
    print (f'Este é um numero primo pois é divisivel {cont} vezes.')