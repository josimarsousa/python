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
""" 
#listas com strings
print("listas com strings")
L = ["maça", "pera", "banana", "abacaxi", "uva"]
print(f"Quantidade de palavras na lista: {len(L)}")
print(f"Palavras na lista: {L}")
print(f"Posiçao de cada palavra na lista: {[L.index(e) for e in L]}")