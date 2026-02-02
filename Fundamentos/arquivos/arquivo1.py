#gerando e granvando um arquivo
"""
arquivo = open("números.txt", "w")
for linha in range(1, 101):
    arquivo.write(f"{linha}\n")
arquivo.close()
"""

#lendo e abrindo um arquivo e imprimir suas linhas na tela
arquivo = open("números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()