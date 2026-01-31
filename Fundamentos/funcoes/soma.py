import entrada  #chama funcao valida_inteiro do modulo entrada

L = []
for n in range(10):
    L.append(entrada.valida_inteiro(f"Digite o um número: ", 0, 20))
print(f"Soma: {sum(L)}")


