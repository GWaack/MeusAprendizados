#Vogais com Tuplas
itens = ('Carne', 'Salada', 'Frango', 'Feijoada', 'Arroz', 'Mandioca', 'Mingau')
for palavras in itens:
    print (f'\nNa palavra {palavras} temos as vogais: ', end=' ')
    for vogais in palavras:
        if vogais.lower() in 'aeiou':
            print (vogais.lower(), end=' ')