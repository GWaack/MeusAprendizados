## ler sexo e idade de varias pessoas
## a cada pessoa cadastrada, perguntar se deseja continuar
## quantas pessoas tem mais de 18 anos?
## quantos homens foram cadastrados?
## quantas mulheres tem menos de 20 anos?
print ('-*-' *10)
print ('          Cadastro')
print ('-*-' *10)
maiordezo = homens = mulhemenvint = 0
while True:
    idade = int(input('Insira aqui sua idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Insira aqui seu sexo: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        maiordezo += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f': 
        if idade < 20:
            mulhemenvint += 1   
    resp = ' '
    while resp not in 'sn':
        print ('-*-' *10)
        resp = input('Deseja continuar? [S/N]').strip().lower()[0]
        print ('-*-' *10)
    if resp == 'n':
        break
print (f'Acabou! Você tem cadastrado {maiordezo} pessoas com mais de 18 anos, {homens} homens cadastrados e {mulhemenvint} mulheres com menos de 20 anos')
