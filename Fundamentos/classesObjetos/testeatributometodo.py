from atributosemetodos import Contador

c1 = Contador()
c2 = Contador()

print(Contador.instancias)
print(c1.contador)
print(c2.contador)

c2.contador += 1
print(c2.contador)