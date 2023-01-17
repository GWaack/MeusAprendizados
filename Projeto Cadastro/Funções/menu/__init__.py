def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'O valor informado não é válido')
            continue
        except (KeyboardInterrupt):
            print('O usuario decidiu interromper os dados.')
            return 0
        else:
            return num

def linha(tamanho=42):
    return '-'* tamanho

def cabecalho(titulo):
    print(linha())
    print(f'{titulo.center(42)}')
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[1;33m{cont}\033[m - \033[1;36m{item}\033[m')
        cont += 1
    print(linha())
    resposta_opcao = leiaInt('Digite sua opção: ')
    return resposta_opcao

# cores final  \033[m  
'''
Preto	\033[1;30mS
Vermelho	\033[1;31m
Verde	\033[1;32m
Amarelo	\033[1;33m
Azul	\033[1;34m
Magenta	\033[1;35m
Cyan	\033[1;36m
Cinza Claro	\033[1;37m
Cinza Escuro	\033[1;90m
Vermelho Claro	\033[1;91m
Verde Claro	\033[1;92m
Amarelo Claro	\033[1;93m
Azul Claro	\033[1;94m
Magenta Claro	\033[1;95m
Cyan Claro	\033[1;96m
Branco	\033[1;97m
Negrito	\033[;1m
Inverte	\033[;7m
'''



    





'''def cadastrar(nome=0, idade=0):
    while True:
        try:
            name = str(input(nome))
        except (ValueError, TypeError):
            print('Algo deu errado, insira seu nome novamente: ')
            continue
        else:
            print(f'Nome {name} adicionado com sucesso!')
            return name
           '''   

