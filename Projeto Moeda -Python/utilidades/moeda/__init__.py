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

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0,taxaa=10,taxar=15):
    print('-'*30)
    print('RESUMO DE VALORES'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço,taxar,True)}')