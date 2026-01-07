#exemplo 
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