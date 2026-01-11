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
"""
#fatiamento de listas e copia
L = [1,2,3]
x = 0
while x < 3:
    print(L[x])
    x += 1
print(L[0:3])

#usando a funcal Len()
L = [1, 2, 3]
x = 0
while x < len(L):
    print(L[x])
    x += 1
print(L[0:len(L)])