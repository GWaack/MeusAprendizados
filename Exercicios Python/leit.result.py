## ler varios numeros inteiros
## só parar quando digitar 999
##quantos numeros foram digitados
##soma entre eles

soma = qnt = 0
while True:
   num = int(input('Insira aqui um numero: '))
   if num == 999:
       break
   qnt += 1
   soma += num
print(f'Você digitou {qnt} números e a soma entre eles é de {soma}')