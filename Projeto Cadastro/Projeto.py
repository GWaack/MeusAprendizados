from Funções.menu import *
from Funções.arquivo import *
from time import sleep

arquivo = 'cadastro.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)  
while True:
    resposta = menu( ['Cadastrar Pessoas' , 'Ler Arquivos', 'Sair do Programa'])
    if resposta == 1:
        cabecalho('Cadastrando Nova Pessoa')
        quantidade = leiaInt('Quantas pessoas vai cadastrar? ')
        for cadastro in range(0,quantidade):
            nome = str(input('Digite seu nome: '))
            idade = leiaInt('Digite sua idade: ')
            cadastrar(arquivo, nome, idade)
    elif resposta == 2:
        cabecalho('Lendo Arquivo')
        sleep(2)
        lerArquivo(arquivo)
    elif resposta == 3:
        cabecalho('Finalizando...')
        break
    else:
        print('\033[1;31m Ocorreu um erro! Informe um valor válido\033[m')




