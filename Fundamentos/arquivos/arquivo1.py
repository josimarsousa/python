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
                

#arquivos - leitura e escrita
with open("multiplos de 4.txt", "w") as multiplos4:
    with open("pares.txt") as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(linha)
                


#processamento de um arquivo
largura = 79
with open("entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(largura))
        elif linha[0] == "*":
            print(linha[1:].center(largura))
        else:
            print(linha)
"""
#Controle de uma agenda de telefones
agenda = []
def pede_nome():
    return input("Nome: ")
def pede_telefone():
    return input("Telefone: ")
def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")
def pede_nome_arquivo():
    return input("Nome do arquivo: ")
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n.......")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print(".......")

def le():
    #lê o arquivo e carrega a agenda na memória - global
    global agenda
    nome_arquivo = pede_nome_arquivo()
    
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo: 
        agenda = []
        print(f"Carregando arquivo {nome_arquivo}...")
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split("#")
            agenda.append([nome, telefone])
            
def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <=fim:
                return valor
        except ValueError:
            print(f"Valor inválido. Digite um número inteiro entre {inicio} e {fim}.")


def menu():
    print(""""

    1 - Novo
    2 - Apaga
    3 - Altera
    4 - Lista
    5 - Le
    6 - Grava


    0 - Sai
    
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)
while opcao := menu():
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        apaga()
    elif opcao == 3:
        altera()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        le()
    elif opcao == 6:
        grava()

