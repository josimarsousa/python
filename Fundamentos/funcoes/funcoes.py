"""
def soma(a, b):
    #print(f"A soma de {a} + {b} é: {a+b}")
    return (f"A soma de {a} + {b} é: {a+b}")

print(soma(2, 3))
print(soma(5, 7))
print(soma(10, 20))

#verificar se número é par ou impar
def par_impar(num):
    if num % 2 == 0:
        return f"{num} é par"
    else:
        return f"{num} é impar"

print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(5))
print(par_impar(6))
"""
#funcao para verificar se numero é maior de 2 números
def maior_menor(num1, num2):
    if num1 > num2:
        return f"{num1} é maior que {num2}"
    else:
        return f"{num2} é maior que {num1}"

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print(maior_menor(num1, num2))
