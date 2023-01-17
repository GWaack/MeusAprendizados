#maior e menor em uma lista
from operator import index

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um número: ')))
print (valores)
print (f'O maior valor foi {max(valores)} na posição {valores.index(max(valores))}º e o menor foi {min(valores)} na posição {valores.index(min(valores))}º')
