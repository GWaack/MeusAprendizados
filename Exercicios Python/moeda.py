def aumentar(preço=0, taxa=0, formatado=False):
    resposta = preço + (preço * taxa/100)
    return resposta if formatado is False else moeda(resposta)

def diminuir(preço=0,taxa=0, formatado=False):
    resposta = preço - (preço * taxa/100)
    return resposta if formatado is False else moeda(resposta)

def dobro(preço=0, formatado=False):
    resposta = preço * 2
    return resposta if formatado is False else moeda(resposta)

def metade(preço=0, formatado=False):
    resposta = preço /2
    return resposta if formatado is False else moeda(resposta)

def moeda(valor):
    real = f'R$ {valor}'
    return real

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0, taxa_aumento=0, taxa_diminui=0):
    print('-'*30)
    print('RESUMO DE VALORES'.center(30))
    print('-'*30)
    taxa_aum = aumentar(preço,taxa_aumento)
    taxa_dim = diminuir(preço,taxa_diminui)
    dobr = dobro(preço)
    metad = metade(preço)
    return f'Dobrando o valor {moeda(preço)} temos {moeda(dobr)} \nMetade de {moeda(preço)} temos {moeda(metad)} \nCom a taxa de {taxa_aumento}% em cima de {moeda(preço)} temos o valor de {moeda(taxa_aum)} \nCom a taxa diminuindo em {taxa_diminui}% em cima de {moeda(preço)} temos o valor de {moeda(taxa_dim)}' 

result = resumo(10,1,0)
print(result)
