from Funções.menu import * 
from time import sleep
def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
       return False
    else:
        return True

def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        for linhas in arquivo:
            dados = linhas.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
        sleep(2)
    finally:
        arquivo.close()

def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao inserir os dados no arquivo!')
        else:
            print('Pessoa cadastrada com sucesso!')
            arq.close()