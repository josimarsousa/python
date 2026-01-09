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

#calculo de media com acumuladores que nada mais é do que uma variavel registrando os dados recebidos.
x = 1
soma = 0

while x <= 5:
    n = int(input(f"{x} Digite o número: "))
    soma = soma + n
    x = x + 1
print(f"Média: {soma / 5}")

#interrompendo um laço while
s = 0 
while True:
    v = int(input("Digite um número a soma ou 0 para sair: "))
    if v == 0:
        break
    s += v
print(f"Soma: {s}")

"""

#Contagem de cédulas
valor = int(input("Digite o valor a pagar: "))
cédulas = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
       print(f"{cédulas} cédula(s) de R${atual}")
       if apagar == 0:
        break
       if atual == 50:
        atual = 20
       if atual == 20:
        atual = 10
       elif atual == 10:
        atual = 5
       elif atual == 5:
        atual = 1
       cédulas = 0 


#instruçoes aninhadas
#tabuada com instruçoes aninhadas
tabuada = 1
while tabuada <=10:
    número = 1
    while número <= 10:
        print(f"{tabuada} x {número} = {tabuada * número}")
        número += 1
    tabuada += 1

#F-Strings
a = "mundo"
print(f"olá {a}")

numero = 10
print(f"o número é: {numero :.2f}")
