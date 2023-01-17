#Verificação simples
sexo = str(input('Digite aqui o seu sexo M/F: ')).strip().upper()[0]  #Strips retira os espaços e upper põe tudo em maiusculo
while sexo not in 'MmFf':
    sexo = str(input('Informação incorreta digite seu sexo: '))