tabuada
valor = int(input('Insira aqui um numero que deseja saber a tabuada: '))   
uni = 0
for c in range (1,11):
    uni = uni + 1
    print (f'{uni} x {valor} = {valor * c}')