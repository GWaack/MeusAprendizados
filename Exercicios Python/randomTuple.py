## numeros aleatórios Tuplas
from random import randint
numeros = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
for n in numeros:
    print (n, end=' ')
print (f'\nO maior numero foi {max(numeros)}')
print (f'O menor numero foi {min(numeros)}')