#lista
Z = [1,2,3,4,5,6,7,8,9,10]
print(Z)

#buscando elemento pelo indice
print(Z[0])

#atribuindo valor ao elemento pelo indice
Z[0] = 100
print(Z)


#calculo de media
notas = [6,7,4,9, 3]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:.2f}")