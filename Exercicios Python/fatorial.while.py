##fatorial com while
c = 1
valor = int(input('Informe um número que deseja saber o fatorial: '))
while valor != 0:
    print (valor, end=' ')
    print ('x' if valor > 1 else '=', end=' ')
    c = c * valor
    valor -= 1

print (c) 