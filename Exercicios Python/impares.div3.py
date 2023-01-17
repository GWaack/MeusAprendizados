# Numeros impares divisores por 3
soma= 0
for c in range (1,500):
    if c %3 == 0 and c %2 >=1:
       print (c)
       soma = soma + c
print (soma)