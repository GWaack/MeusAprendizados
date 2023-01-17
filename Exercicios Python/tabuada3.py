##tabuada de 10 numeros (o comando for dentro de um while)
##perguntar se quer saber de mais numeros (condição de parada)
## se valor for negativo parar o programa (parada executada)

while True:
    num = int(input('Insira aqui um numero para saber a tabuada: '))
    if num < 0: break
    for c in range (1 ,11):
        mult = c * num
        print (f'{num} x {c} é igual a {mult}')
   


print ('Finalizado.')