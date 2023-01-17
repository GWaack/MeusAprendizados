##Soma de somente numeros pares
valor = 0
for c in range (1,7):
   num = int(input('Insira aqui um numero: '))
   if num %2 == 0:
       valor = valor + num
print (valor)