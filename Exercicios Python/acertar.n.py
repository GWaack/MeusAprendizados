#Acertar numero do computador
from random import randint

pc = randint(1,10)
jogador = int(input('Tente adivinhar o numero de 1 a 10: '))
cont = 1
while jogador != pc:
    if jogador > pc:
        jogador = int(input('Errado! Tente um número menor:'))
        cont += 1
    else: 
        jogador = int(input('Errado! Tente um número maior:'))
        cont += 1
print (f'Você acertou! o número era {pc}! Você precisou de {cont} tentativas até acertar.')