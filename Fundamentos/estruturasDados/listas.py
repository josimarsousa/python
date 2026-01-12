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
"""
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