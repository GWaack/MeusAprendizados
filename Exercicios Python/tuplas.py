#Tuplas

numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = -1
while escolha <0 or escolha > 20:
    escolha = int (input('Insira um número entre 0 e 20: '))
print (f'Você escolheu o número {numeros[escolha]}')