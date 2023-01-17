from utilidades import moeda
from utilidades.dado import leiaDinheiro, leiaFloat, leiaInt
n = leiaDinheiro('Digite um valor: R$')
moeda.resumo(n,10,20)

print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Aumentando a taxa de 10% em {moeda.moeda(n)} da {moeda.aumentar(n,10, True)}')
print(f'Diminuindo a taxa de 10% em {moeda.moeda(n)} da {moeda.diminuir(n,10,True)}')


num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um numero real: ')
print(num1,num2)

