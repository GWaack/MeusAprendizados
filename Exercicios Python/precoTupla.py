#Lista de preço com Tuplas
produtos = 'Borracha', 1.50, 'Giz' , 2.50, 'Lápis', 1.00, 'Caneta', 3.00
print ('-'*40)
print (f'{"LISTAGEM DE PREÇOS":^40}')
print ('-'*40)
for pos in range (0, len(produtos)):  #cria uma repetição que pega a posição de 0 até a ultima de produtos
    if pos %2 == 0:  # confere se a posição é par, para destinguir qual é produto e qual é preço
        print (f'{produtos[pos]:.<30}', end=' ') #:.<30 faz com que criem-se pontos que preencham até dar 30 caracteres alinhas a esquerda
    else:
        print (f'{produtos[pos]:>.2f}') #:>.2f alinha a direta com 2 casas decimais
print ('-'*40)