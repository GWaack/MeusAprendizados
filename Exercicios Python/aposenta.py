from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
dados['Idade'] = (datetime.now().year - int(input('Digite seu ano de nascimento: ')))
dados['Carteira'] = int(input('Digite sua carteira de trabalho / Caso não tenha digite 0'))
if dados['Carteira'] != 0:
    dados['AnoContrat'] = int(input('Digite o ano de contratação: '))
    dados['Salario'] = float(input('Digite seu salario: R$'))
    dados['Aposentadoria'] = ((35-(datetime.now().year - dados['AnoContrat'])) + dados['Idade'])
print ('-=' * 30)
for k, v in dados.items():
    print (f'{k} tem o valor {v}')
