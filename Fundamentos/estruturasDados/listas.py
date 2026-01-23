#lista
"""
Z = [1,2,3,4,5,6,7,8,9,10]
print(Z)

#buscando elemento pelo indice
print(Z[0])

#atribuindo valor ao elemento pelo indice
Z[0] = 100
print(Z)


#calculo de media
notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
    print(f"soma = {soma}")
    print(f"x = {x}")
print(f"Média: {soma / x:5.2f}")

#Calculo da média com notas digitadas pelo usuário
notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Digite a nota {x+1}: "))
    soma += notas[x]
    x +=  1
x = 0
while x < 5: 
    print(f"nota {x+1} = {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")

#apresentaçao de números
numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Digite o número {x+1}: "))
    x += 1
while True:
    escolhido = int(input(f"Que posiçao você quer imprimir? (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o númro: {numeros[escolhido-1]}")

#fatiamento de listas e copia
L = [1,2,3]
x = 0
while x < 3:
    print(L[x])
    x += 1
print(L[0:3])

#usando a funcao Len()
L = [1, 2, 3]
x = 0
while x < len(L):
    print(L[x])
    x += 1
print(L[0:len(L)])

#adicionando elementos na lista
L = []
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        print("Voce sair do sistema")
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1

#exercicios de listas
nomes = []
sobrenomes = []
nome_completos = []
while True: 
    nome = input("Digite um nome (s para sair): ")
    if nome == "s":
        print("Você saiu do sistema com segurança.")
        break
    nomes.append(nome)
    sobrenome = input("Digite agora o sobrenome: ")
    sobrenomes.append(sobrenome)
    nome_completos.append(nome + " " + sobrenome)
x = 0
while x < len(nomes):
    print(nomes[x])
    print(sobrenomes[x])
    print(nome_completos[x])
    x += 1
print(nomes, sobrenomes, nome_completos)        

#removendo elementos da lista
L = ["a", "b", "c"]
del L[0]
print(L)

#apagando fatias inteiras
L = list(range(101))
print(L)
del L[0:99]
print(L)

#usando lista como fila
#simulando uma fila de banco
ultimo = 0
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"fila atual: {fila}")
    print(f"Digite C para adicionar um cliente á fila, ")
    print(f"ou A para realizar o atendimento. S para sair.")
    operacao = input("Qual a operação desejada? (C, A ou S)")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia! Ninguém para ser atendido.")
    elif operacao == "C":
        ultimo += 1 #incrementa o ticket de novo cliente
        fila.append(ultimo) #adicionando o novo cliente á fila
    
    elif operacao == "S":
        print("Saindo do sistema...")
        break
    else: 
        print("Operação inválida! Digite apenas A, C ou S.")

#usando lista como pilha
#simulando uma pilha de pratos
prato = 5
pilha = list(range(1, prato + 1))
print(range(1, prato + 1))
while True:
    print(f"nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print(f"Digite E para empilhar um novo prato,")
    print(f"ou D para desempilhar um prato. S para sair.")
    operacao = input("Operaçao (E, D ou S):")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado.")
        else:
            print("Pilha vazia! Nenhum prato para ser lavado.")
    elif operacao == "E":
        prato +=1 #novo prato
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operaçao inválida! Digite apenas E, D ou S.")

#pesquisa sequencial
L = [1,2,3,4,5]
p = int(input("Digite o valor a procurar:"))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x +=1
if achou:
    print(f"{p} achado na posiçao {x}")
else:
    print(f"{p} não encontrado.")
       
#usando o for
L = [8,9,15]
for e in L:
    print(e)

#usando break para interromper for
L = [7,9,10,12]
p = int(input("Digite um número a pesquisar"))
for e in L: #percorrendo a lista
    if e == p: #se o elemento for igual ao número pesquisado
        print(f"{p} achado na posição {L.index(e)}") #imprime a posição do elemento
        break #interrompe o for
    else:
        print(f"{p} não encontrado.")

#usando o range para gerar listas simples
for v in range(10):
    print(v)

#usando o range a partir de um valor
for v in range(5, 8):
    print(v)


#acrescentando um parametro a funcao range
for t in range(3, 33, 3):
    print(t, end="")
print()

#transformando range em lista
import enum


L = list(range(100, 1100, 50))
print(L)

#comparando com funcao enumerate
print("For normal:")
L = [5, 9, 13]
x = 0
for e in L:
    print(f"[{x}] {e}")
    x += 1

#mesmo programa acima com a enumerate
print("Funcao enumerate:")
L = [5, 9, 13]
for x, e in enumerate(L):
    print(f"[{x}] {e}")

#Listas, tuplas, dicionarios e conjuntos
print("Outros exemplos:")
L = [5, 9, 13]
for z in enumerate(L):
    x, e = z
    print(f"[{x}] {e}")
    print(z)

#Operações com listas
#verificanco o maior valor:
L = [1, 7, 2, 4, 879, -1]
print(f"Lista: {L}")
maximo = L[0]
minimo = L[0]
for e in L:
    if e > maximo:
        maximo = e
    elif e < minimo:
        minimo = e
print(f"O maior valor até agora é: {maximo}")
#achando o menor valor:
print(f"O menor valor até agora é: {minimo}")

#copia de elementos para outras listas
print("Copia de elementos para outras listas, separando pares e ímpares:")
valores = [1,4,65,667,4,3,5,7,8,9]
pares = []
impares = []
print("Lista: ", valores)
for e in valores:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)
print(f"Pares: ", pares)
print(f"Impares: ", impares)

#controle de utilizacao de salas de cinema
lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0: 
        print("Saindo do sistema...")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida!")
    elif lugares_vagos[sala - 1] == 0:
        print("Sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse n;umero de lugares não está disponível.")
        elif lugares < 0:
            print("Digite um número válido.")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares reservados na sala {sala}.")
        print("Utilizaçao das salas")
        for sala, vagos in enumerate(lugares_vagos):
            print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
 
#listas com strings
print("listas com strings")
L = ["maça", "pera", "banana", "abacaxi", "uva"]
print(f"Quantidade de palavras na lista: {len(L)}")
print(f"Palavras na lista: {L}")
print(f"Posiçao de cada palavra na lista: {[L.index(e) for e in L]}")

#listas de compras - lendo e imprimindo
compras = []
while True:
    produto = input("Digite um produto para a lista de compras: ")
    if produto == "fim":
        break
    compras.append(produto)
print("lista de compras\n")
for p, compras in enumerate(compras):
    p = p + 1
    print(f"{p} - {compras}")
#for p in compras:
#    print(f"lista de compras: {p}")

#listas dentro de listas - acessando strings letra a letra - buscando palavra na lista
palavras = ["maças", "peras", "abacaxi"]
#print(palavras[0][0])
#print(palavras[0][1])
#print(palavras[1][3])
#print(palavras[2][4])
busca = input("Digite uma palavra para buscar:")
if busca in palavras:
    print(f"A palavra {busca} foi encontrada na posição {palavras.index(busca)} da lista")
else:
    print(f"A palavra {busca} não foi encontrada na lista.")
   
#listas com elementos diferentes
produto1 = ["detergente", 2, 2.79]
produto2 = ["arroz", 1, 18.99]
produto3 = ["sabao em po", 1, 27.99]
compras = [produto1, produto2, produto3]
print(compras)

#imprimindo elementos diferentes de uma lista 
for p in compras:
    print(f"Produto: {p[0]}")
    print(f"Quantidade: {p[1]}")
    print(f"Preço: {p[2]:5.2f}")
    print("------------------")

#calculando o valor total da compra e imprimindo
total = 0
for p in compras:
    total += p[1] * p[2]
print(f"Total da compra: {total:5.2f}")

#criando o programa completo para gerar a lista de compra com o devido total
compras = []
while True:
    produto = input("Digite um produto para a lista de compras: ")
    if produto == "fim":
        break
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for p in compras:
    print(f"{p[0]} - {p[1]:5d} - {p[2]:5.2f} {p[1] * p[2]:5.2f}")
    soma += p[1] * p[2]
print(f"Total da compra: {soma:5.2f}")
 
#vizualizando em tempo real o valor da compra
compras = []
while True:
    produto = input("Digite um produto para a lista de compras: ")
    if produto == "fim":
        break
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    compras.append([produto, quantidade, preco])
    soma = 0.0
    for p in compras:
        print(f"{p[0]} - {p[1]:5d}x{p[2]:5.2f} {p[1] * p[2]:5.2f}")
        soma += p[1] * p[2]
    print(f"Total da compra: {soma:5.2f}")
for p in compras: 
    print(f"{p[0]} - {p[1]:3d} x {p[2]:5.2f} {p[1] * p[2]:5.2f}")
print(f"Total da compra: {soma:5.2f}")

#ordenaçao de elementos em uma lista utilizando o buble sort
L = [1,28,3,3,709,24,2,5,4,4,5]
fim = len(L)
print(f"Lista antes da ordenação: {L}")
while fim > 1:
    trocou = False
    x = 0
    while x < (fim -1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
print(f"Lista depois da ordenação: {L}")
#for e in L: 
 #   print(e)

#ordenação de elementos em uma lista utilizando o buble sort em ordem decrescente
L = [1,28,3,3,709,24,2,5,4,4,5]
fim = len(L)
print(f"Lista antes da ordenação: {L}")
while fim > 1:
    trocou = False
    x = 0
    while x < (fim -1):
        if L[x] < L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
print(f"Lista depois da ordenação: {L}")

#metodo sort() - ordena a lista em ordem crescente
L = [1,28,3,3,709,24,2,5,4,4,5]
print(f"Lista antes da ordenação: {L}")
L.sort()
print(f"Lista depois da ordenação: {L}")

#funcao sorted() - sem alterar a lista original
L = [1,28,3,3,709,24,2,5,4,4,5]
print(f"Lista antes da ordenação: {L}")
sorted(L)
print(f"Lista depois da ordenação: {L}")


#dicionarios
tabela = {
    "Alface": 2.50,
    "Mandioca": 60.00,
    "Couve": 5.00,
    "Feijão": 10.00
}

print(tabela["Alface"])
print(tabela)

#dicionario - obtençao do preço com um dicionário
tabela = {
    "Alface": 2.50,
    "Mandioca": 60.00,
    "Couve": 5.00,
    "Feijão": 10.00
}
while True:
    produto = input("Digite um produto ou digite 'fim' para terminar. ")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado.")


#exemplo de dicionário com operacoes de vendas
estoque = {
    "maças": [100, 12.30],
    "alface": [500, 0.45],
    "abacaxi": [2001, 1.20],
    "feijao": [100, 1.50]
}
venda = [["maças", 2], ["alface", 3], ["abacaxi", 1]]
total = 0
print("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao
    if produto in estoque:
       preco = estoque[produto][1]
       custo = preco * quantidade
       print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
       estoque[produto][0] -= quantidade
       total += custo
    print(f"Custo total: {total:21.2f}\n")
    print(f"Estoque: \n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
        
        print("")


#exemplo de dicionario sem valor padrao, calculando a ocorrencia de uma letra em uma palavra
d = {}
for letra in "abracadabra":
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1
print(d)

#exemplo de dicionário com valor padrao usando o método get do dicionário.
d = {}
for letra in "abracadabra":
    d[letra] = d.get(letra, 0) + 1
print(d)

#tuplas em python
tupla = ("a", "b", "c", "d", "e")
print(tupla)

#o parenteses sao opcionais
tupla = "a", "b", "c", "d", "e"
print(tupla)

#tuplas soportam a maior parte das operaçoes de listas
print("tuplas suportam a maior parte das operaçoes de listas")
print(tupla[0])
print(tupla[2])
print(tupla[1:])
print(len(tupla))
"""
#conjuntos set
a = set()
a.add(11)
a.add(12)
a.add(13)
a.add(14)
a.add(15)
print(a)

if 9 in a:
    print("1 está em a")
else:
    print("1 não está em a")

#conjuntos set - podemos criar listas com estruturas de dados
print("conjuntos set - podemos criar listas com estruturas de dados")
b = set([1,2,3,4,5,7,8,9,10])
print(b)

#mostrando o tamanho da estrutura conjunto com propriedades de set
print("tamanho do conjunto b:", len(b))

#uniao de conjuntos com o operador |


#uniao de conjuntos com o operador |
print("uniao de conjuntos com o operador |")
print(a | b)

#outros métodos 
print("intersecção de conjuntos com o operador &")
print(a & b)

print("Uniao com metodo union")
print(a.union(b))

#diferença simétrica de conjuntos com o operador ^
print("diferença simétrica de conjuntos com o operador ^")
print(a.symmetric_difference(b))
print("ou")
print(a ^ b)

#programa jogo da forca
palavra = input("Digite uma palavra: ")
for x in range(100):
    print()
digitada = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra:
            print("Você acertou a palavra!")
            break
        tentativa = input("\nDigite uma letra: ")
        if tentativa in digitada:
            print("Você ja tentou esta letra")
            continue
        else:
            digitada += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
            print("X==:==\nX  :  ")
            print("X 0 " if erros >= 1 else "X")
            linha2 = ""
            if erros >= 2:
                linha2 = " | "
            if erros == 3:
                linha2 = " \| "
            if erros == 4:
                linha2 = " \|/ "
            print(f"X{linha2}")
            linha3 = ""
            if erros == 5:
                linha3 += " / "
            elif erros >= 6:
                linha3 += " /\ "
            print("X\n==========")
            if erros == 6:
                print("Você foi enforcado!")
                break