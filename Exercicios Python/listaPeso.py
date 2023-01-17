lista = list()
dados = list()
maior = menor = 0
while True:
    dados.append (str(input('Digite seu nome: ')))
    dados.append (float(input('Informe sua peso: ')))
    if len(lista) == 0:                 #Estrutura de maior e menor
        maior = menor = dados[1]        # Caso a lista esteja vazia, o maior e o menor numero vão ser o primeiro digitado
    else: 
        if dados[1] > maior:            #Caso não, se o dados[1] que é o peso for maior que o maior setado anteriormente ele se torna o novo maior
            maior = dados[1]
        if dados[1] < menor:            #O mesmo acontece no caso do menor
            menor = dados[1]
    lista.append(dados[:]) #Colchetes com dois pontos dentro informa ao python que será feita uma cópia dos dados
    dados.clear()   #Após o valor ser passado para lista principal, o comando clear vem para limpar para não ter valores duplicados
    resp = str(input('Quer continuar? S/N: ')).strip().lower()[0]
    if resp == 'n':
        break
print (f'Foram inseridos {len(lista)} na lista') # Contabiliza quantos itens tem dentro da lista, não precisando de um contador
print (f'O maior peso foi de {maior}KG', end='')
for p in lista:                 #Estrutura de repetição para percorrer toda a lista conferindo se o peso é igual ao maior
    if p[1] == maior:
        print (f' e pertence a {p[0]}') # Caso seja, ele printa o nome associado ao valor maior
print (f'O menor peso foi de {menor}KG', end='')
for p in lista:                 # O mesmo é feito para o menor valor
    if p[1] == menor: 
        print (f' e pertece a {p[0]}')