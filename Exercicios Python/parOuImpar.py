## valor pra pessoa e computador
## perguntar se a pessoa quer impar ou par
## comparar resultado
## informar quem ganhou
## se a pessoa ganhar o jogo continua

from random import randint
cont = 0
while True:
    pess = int(input('Escolha um numero: '))
    comp = randint (1,100)
    pi = str(input('Você deseja par ou impar? [P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Você deseja par ou impar? [P/I] ')).strip().upper()[0]
    if pi == 'P':
        resul = pess + comp
        if resul %2 == 0:
            cont += 1
            print(f'Deu par, você venceu! Você jogou {pess} e o computador jogou {comp} num total de {resul}')
        elif resul %2 >=1: 
            print(f'Você perdeu! Você jogou {pess} e o computador jogou {comp} num total de {resul}. Você acertou {cont} vezes')
            break  
    if pi == 'I':
        resul = pess + comp
        if resul %2 >=1:
            cont += 1
            print(f'Deu Ímpar, você venceu! Você jogou {pess} e o computador jogou {comp} num total de {resul}')
        elif resul %2 == 0: 
            print(f'Você perdeu! Você jogou {pess} e o computador jogou {comp} num total de {resul}. Você acertou {cont} vezes')
            break
        else: print(f'Você perdeu! Você jogou {pess} e o computador jogou {comp} Você acertou {cont} vezes')
        break
    if pi == 'i':
        resul = pess + comp
        if resul %2 >= 1:
            cont += 1
            print(f'Deu Ímpar, você venceu! Você jogou {pess} e o computador jogou {comp}')         
        else: print(f'Você perdeu! Você jogou {pess} e o computador jogou {comp}. Você acertou {cont} vezes')
        break
