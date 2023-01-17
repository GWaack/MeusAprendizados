import funcoes

def main():
    usuarios = funcoes.ler_arquivo("usuarios.txt")
    espaco_total = funcoes.converter_para_megabytes(sum(u["espaco_utilizado"] for u in usuarios))
    espaco_medio = espaco_total / len(usuarios)

    quantidade = funcoes.pedir_quantidade_usuarios()
    usuarios_a_mostrar = usuarios[:quantidade] if quantidade != -1 else usuarios
    
    for usuario in usuarios_a_mostrar:
        usuario["espaco_utilizado"] = funcoes.converter_para_megabytes(usuario["espaco_utilizado"])
        usuario["porcentagem_uso"] = funcoes.calcular_porcentagem_uso(usuario["espaco_utilizado"], espaco_total)

    usuarios_a_mostrar.sort(key=lambda u: u["porcentagem_uso"], reverse=True)
    
        
    with open("relatorio.txt", "w") as arquivo:
        arquivo.truncate(0)
        arquivo.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
        arquivo.write("------------------------------------------------------------------------\n")
        arquivo.write("{:^5} {:<15} {:^25} {:^20}\n".format("#", "Usuário", "Espaço utilizado", "% do uso"))
        arquivo.write("------------------------------------------------------------------------\n")

        for i,usuario in enumerate(usuarios_a_mostrar):
            arquivo.write("{:^5} {:<15} {:^25} {:^20}\n".format(i+1, usuario['login'].capitalize(), f"{usuario['espaco_utilizado']:.2f} MB", f"{usuario['porcentagem_uso']:.2f}%"))
            arquivo.write("\n")
        arquivo.write(f"Espaço total ocupado: {espaco_total:.2f} MB\n")
        arquivo.write(f"Espaço médio ocupado: {espaco_medio:.2f} MB\n")

        print("Relatório gerado com sucesso!")
    return

main()

with open("relatorio.txt", "r") as arquivo:
  conteudo = arquivo.read()

html = f'<html>\n<head>\n<title>Relatório de uso de disco</title>\n</head>\n<body>\n<pre>\n{conteudo}\n</pre>\n</body>\n</html>'

with open("relatorio.html", "w") as arquivo:
    arquivo.write(html)

