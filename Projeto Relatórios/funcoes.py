def ler_arquivo(nome_arquivo):
    """Lê o arquivo de entrada e armazena os dados em uma lista de dicionários.

    Args:
    nome_arquivo (str): O nome do arquivo a ser lido.

    Retorna:
    list: A lista de dicionários com os dados dos usuários.
    """
    usuarios = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            login, espaco_utilizado = linha.split()
            usuario = {"login": login, "espaco_utilizado": int(espaco_utilizado)}
            usuarios.append(usuario)
    return usuarios

def converter_para_megabytes(espaco_em_bytes):
    """Converte o espaço ocupado em disco, em bytes, para megabytes.

    Args:
    espaco_em_bytes (int): O espaço ocupado em bytes.

    Returna:
    float: O valor do espaço ocupado em megabytes.
    """
    return espaco_em_bytes / 1024 / 1024

def calcular_porcentagem_uso(espaco_utilizado, espaco_total):
    """Calcula o percentual de uso de um usuário.

    Args:
    espaco_utilizado (float): O espaço ocupado pelo usuário em megabytes.
    espaco_total (float): O espaço total da organização em megabytes.

    Retorna:
    float: O percentual de uso do usuário.
    """
    return espaco_utilizado / espaco_total * 100

def pedir_quantidade_usuarios():
    """Solicita ao usuário a quantidade de usuários a serem mostrados.

    Retorna:
    int: A quantidade de usuários a serem mostrados.
    """
    while True:
        quantidade = input("Insira a quantidade de usuários a serem mostrados (digite 'todos' para mostrar todos): ")
        if quantidade.lower() == "todos":
            return -1
        else:
            try:
                quantidade = int(quantidade)
                if quantidade > 0:
                    return quantidade
                else:
                    print("Quantidade inválida. Por favor, insira um valor positivo ou 'todos'.")
            except ValueError:
                print("Quantidade inválida. Por favor, insira um valor numérico positivo ou 'todos'.")