#Dicionarios
alunomed  = dict()
alunomed['nome'] = str(input('Nome: '))
alunomed['media'] = int(input('Média: '))
if alunomed["media"] >= 5:
    alunomed['Situação'] = 'Aprovado'
else: alunomed['Situação'] = 'Reprovado'
print (f'O aluno {alunomed["nome"]} teve uma média {alunomed["media"]} e sua situação é {alunomed["Situação"]}')
