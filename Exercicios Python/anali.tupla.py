##Analise de dados com Tupla

numeros = int(input('Insira um numero: ')), int(input('Insira mais um numero: ')), int(input('Agora mais um numero: ')), int(input('Ultimo numero: '))
print (numeros)
print (f'{numeros.count(9)}x foram as vezes que o numero 9 apareceu')
if 3 in numeros:
    print (f'O numero 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('Numero 3 não foi encontrado!')
print ('Os numeros pares digitados foram: ')
for n in numeros:
    if n % 2 == 0:
        print (n, end=' ')