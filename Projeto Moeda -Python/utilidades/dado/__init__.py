def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        dinheiro = str(input(mensagem)).replace(',','.').strip()
        if dinheiro.isalpha() or dinheiro == '':
            print(f'Erro! "{dinheiro}" não é um valor válido')
        else:
            valido = True
    return float(dinheiro)
        
        
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

def leiaFloat(mensagem):
    while True:
        try:
            num = float(input(mensagem))
        except (ValueError, TypeError):
            print('O valor informado não corresponde ao padrão float')
            continue
        except (KeyboardInterrupt):
            print('O usuario decidiu interromper os dados.')
            return 0
        else:
            return num
