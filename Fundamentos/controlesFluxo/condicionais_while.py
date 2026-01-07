#exemplo 
"""
x = 1
while x <=10:
    print(x)
    x += 2


#while e contadores
fim = int(input("Digite o valor final: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1

#while e tabuada
tabuada = int(input("Digite o valor da tabuada: "))
x = 1
while x <= 10:
    print(f"{tabuada} x {x} = {tabuada * x}")
    x += 1

#acumuladores e contadores
n = 1
soma = 0
while n <= 10:
    x = int(input(f"Digite o {n} número:"))
    soma = soma + x
    n = n + 1
print(f"Soma: {soma}")
"""
#calculo de media com acumuladores que nada mais é do que uma variavel registrando os dados recebidos.
x = 1
soma = 0

while x <= 5:
    n = int(input(f"{x} Digite o número: "))
    soma = soma + n
    x = x + 1
print(f"Média: {soma / 5}")