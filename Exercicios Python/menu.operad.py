from time import sleep

v1 = int(input("Insira aqui um valor: "))
v2 = int(input("Insira aqui outro valor: "))
operador = 0
while operador != 5:
    print('''[1]Somar 
    [2] Maior 
    [3] Multiplicar 
    [4] Inserir novos números
    [5] Sair ''')
    operador = int(input('Informe qual sua opção: '))

    if operador == 1:
        soma = v1+v2
        print(f'{v1} + {v2} é igual a {soma}')
    elif operador == 2:
        if v1 > v2:
            print(f'{v1} é maior que {v2}')
        elif v1 == v2:
            print (f'Os valores {v1} e {v2} são iguais')
        else: 
            print(f'{v2} é maior que {v1}')           
    elif operador == 3:
        mult = v1*v2
        print(f'{v1} x {v2} é igual a {mult}')
    elif operador == 4:
        print('Insira os novos números')
        v1 = int(input("Insira aqui um valor: "))
        v2 = int(input("Insira aqui outro valor: ")) 
    elif operador == 5:
        print ('Finalizando...')
        sleep(2)
    else: print('Opção Inválida')
    print ('=-=' * 10)
print('Finalizado com sucesso!')