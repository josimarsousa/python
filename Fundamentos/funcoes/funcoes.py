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
