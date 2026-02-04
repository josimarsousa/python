#gerando e granvando um arquivo
"""
arquivo = open("números.txt", "w")
for linha in range(1, 101):
    arquivo.write(f"{linha}\n")
arquivo.close()


#lendo e abrindo um arquivo e imprimir suas linhas na tela
arquivo = open("números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#uso do with para abrir e fechar o arquivo automaticamente
print("uso do WITH")
with open("números.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

#geração de arquivos
with open("impares.txt", "w") as impares:
    with open("pares.txt", "w") as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")
                
"""
#arquivos - leitura e escrita
with open("multiplos de 4.txt", "w") as multiplos4:
    with open("pares.txt") as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(linha)