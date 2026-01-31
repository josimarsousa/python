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

#funcao para verificar se numero é maior de 2 números
def maior_menor(num1, num2):
    if num1 > num2:
        return f"{num1} é maior que {num2}"
    else:
        return f"{num2} é maior que {num1}"

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print(maior_menor(num1, num2))


#funcao para verificar se numero1 é múltiplo de numero2
def multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num1 = int(input("Digite o primeiro número: "))
num2 = (int(input("Digite o segundo número:")))
        
if multiplo(num1, num2) == True:
    print(f"{num1} é múltiplo de {num2}")
else:
    print(f"{num1} não é múltiplo de {num2}")


#pesquisa em uma lista
def pesquisa(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


L = [10, 20, 25, 30]
print(pesquisa(L, 10))
print(pesquisa(L, 20))
print(pesquisa(L, 30))


#calculando a media de 2 valores de uma lista
def soma(L):
    total = 0
    for n in L:
        total += n
    return total

def media(L):
    return soma(L) / len(L)

print(f"A soma da lista {L}", soma(L))
print(f"A média da lista {L}", media(L))


#calculando o fatorial de um número: 
def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return print(f"O fatorial de {numero} é: {fat}")

numero= int(input(f"Digite um número para calcular o fatorial: "))
fator = fatorial(numero)    

#outra forma calcular fatorial
def fatorial2(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return print(f"O fatorial de {numero} é: {fat}")

numero= int(input(f"Digite um número para calcular o fatorial: "))
fator2 = fatorial2(numero)    

#funcao fatorial mais dinamica
print("Fatorial mais dinamica")
def fatorial3(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n ==1:
        print(f"Fatorial de {n} é 1")
        return 1
    else:
        fat = n * fatorial3(n-1)
        print(f"Fatorial de {n} é {fat}")
    return fat

#exemplo de fatorial3
print(fatorial3(5))

#funcao recursiva de fibonacci
def fibonacci(n):
    print(f"Calculando o fibonacci de {n}")
    if n <= 1:
        print(f"Fibonacci de {n} é {n}")
        return n
    else:
        print(f"Fibonacci de {n} é {fibonacci(n-1) + fibonacci(n-2)}")
        return fibonacci(n-1) + fibonacci(n-2)

#exemplo de fibonacci recursiva
fibonacci(5)

#exemplo de validaçao sem usar a função
while True:
    v = int(input("Digite um valor entre 0 e 5: "))
    if v < 0 or v > 5:
        print("Valor inválido!")
    else:
        print("Valor dentro do aceitável!")
        break
#transformando a validação em funcão
def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print("Valor inválido!")
        else:
            print("Valor dentro do aceitável!")
            break

faixa_int("Digite um valor entre 0 e 5: ", 0, 5)

#funcoes sem parametros
def barra():
    print("*" * 40)

barra()

#funcao barra2 com parametros opcionais
def barra2(n=40, caractere="*"):
    print(caractere * n)

barra2()

#funcão soma com parâmetros obrigatórios e opcionais
def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s

soma(2, 3, True)

#nomeando parâmetros
#funcao retangulo com parametros obrigatórios e opcionais
def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

#teste
retangulo(5, 8)


#funções como parâmetro
def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def imprime(a, b, foper):
    print(foper(a, b))
imprime(5, 4, soma)
imprime(10, 1, subtracao)


#outro exemplo de configurar funções com funções
def imprime_lista(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def imprime_elemento(e):
    print(f"Valor: {e}")

def epar(x):
    return x % 2 == 0

def eimpar(x):
    return not epar(x)

L = [1, 7, 9, 2, 11, 0]
imprime_lista(L, imprime_elemento, epar)
imprime_lista(L, imprime_elemento, eimpar)

#empacotamento e desempacotamento de parâmetros
def soma(a, b):
    print(a + b)
L = [2, 3]
soma(*L)

#outro exemplo
def barra(n=10, c="*"):
    print(c * n)
L = [[5, "-"], [10, "*"], [5], [6, "."]]
for e in L:
    barra(*e)

#funcao soma com numero indeterminado de parâmetros
def soma_args(*args):
    s = 0
    for x in args:
        s += x
    return s

print(soma_args(1,2))
print(soma_args(1,2,3))
print(soma_args(1,2,3,4))

#funcao para imprimir numero maior com numero indeterminado de parâmetros
def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(f"{mensagem} {maior}")

imprime_maior("O maior número é:", 1, 2, 3, 4, 5)

#funções lambda
a = lambda x: x * 2
print(a(3))

#função lambda com mais de um parâmetro
aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))

#exceções
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except IndexError:
        print("Valor inválido, digite entre 0 e 2")

#exceções de tipo raiz Exception, nomeando a função Exception
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except Exception as e:
        print(f"Algo deu errado: {e}")

#utilizando uma declaração try-except-finally
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:            #executado independentemente de ter ocorrido uma exceção ou não
        print("Fim da tentativa")

#utilizando a instrução raise para lançar uma exceção
nomes = ["Ana", "Carlos", "Maria"]
try:
    i = int(input("Digite o índice que quer imprimir: "))
    print(nomes[i])
except ValueError:
  print("Digite um número!")
  raise
finally:            #executado independentemente de ter ocorrido uma exceção ou não
  print("Fim da tentativa")

#outro exemplo com função
def epar(n):
    try:
        return n % 2 == 0
    finally:
        print("Executado antes de retornar")
try:
    print(2, epar(2))
    print(3, epar(3))
except Exception:
    print(f"Algo deu errado")

#exemplo com while
while True:
    try:
        v = int(input("Digite um número inteiro (0 sai):"))
        if v == 0:
            break
    except Exception:
        print("Valor inválido!")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executando sempre, mesmo com break")
"""

#módulos
def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v < minimo or v > maximo:
                return v
            else:
                print(f"Digite um valor entre {minimo} e {maximo}")
        except ValueError:
                print("Você deve digitar um número inteiro!")

#importando e utilizando modulos
#gerando numero aleatorio e colocando em orderm crescente
import random

for x in range(15):
    print(random.randint(1, 25))
#gerando numero sem repetir e em ordem crescente
    print("Gerando números aleatórios sem repetir e em ordem")
    print(sorted(random.sample(range(1, 26), 15)))


#funcao type
def tipo(v):
    print(f"O tipo de {v} é {type(v)}")

tipo(10)
tipo(10.5)
tipo("Olá")
tipo([1, 2, 3])

#funcao isinstance
import types

def diz_o_tipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, int):
        return "Inteiro"
    elif isinstance(a, float):
        return "Ponto Flutuante"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionário"
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Função interna"
    else:
        return str(type(a))
print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Olá"))
print(diz_o_tipo([1, 2, 3]))    
print(diz_o_tipo({"a": 1, "b": 2}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))

#navegando listas a partir do tipo de seus elementos
L = ["a", ["b", "c", "d"], "e"]
for numero in L:
    if isinstance(numero, str):
        print(f"{numero} é uma string")
    else:
        print("Lista: ", end="")
        for e in numero:
            print(f" {e} ", end="")
        print()

#imprimindo uma lista de inteiros com m;ultiplos níveis
def imprime_listas(lista, nivel=0):
    for x in lista:
        if isinstance(x, int):
            print(f"{x:{nivel * 2}}")
        else:
            imprime_listas(x, nivel + 1)
print("Lista em niveis diferentes")
imprime_listas([1, 2, [3, 4, [5, 6, [7,8,9]], 10]])

#list comprehension
print("List comprehension")
L = [x for x in range(10)]
print(L)

#mesmo que utilizar um loop for
print("List com loop for")
L = []
for x in range(10):
    L.append(x)
print(L)

#list comprehension com outras listas
print("List comprehension com outras listas")
L = [(x, x * 2) for x in [0,1,2,3]]
print(L)

#list comprehension com outros tipos de dados
print("list comprehension com outros tipos de dados")
z = [s.upper() for s in "abcdefghij"]
print(z)

print("list comprehension com filtro e if")
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

import math

I = [math.sqrt(z) for z in range(0, 10)]
print(I)

H = [z for z in range(0, 10) if math.sqrt(z) % 1 == 0]
print(H)

#geradores em python
print("Geradores em python")
L = [1,2,3,4,5]
i = iter(L)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#podemos usar o mesmo raciocinio com dicionários
d = {"A": 1, "B": 2, "C": 3}
i = iter(d)
print(i)
print(next(i))
print(next(i))
print(next(i))

#gerador com sequência finita de números
print("Gerador com sequência finita de números")
def gerador_fibonacci():
    p = 0
    s = 1
    while s < 10:
        yield s
        p, s = s, p + s

lista =  [x for x in gerador_fibonacci()]
print(lista)

#outra versao de gerador_fibonacci que receb um valor como parametro fim
print("Versao limitada com um parametro fim")
def gerador_fibonacci(fim):
    p = 0
    s = 1
    while s < fim:
        yield s
        p, s = s, p + s

lista =  [x for x in gerador_fibonacci(30)]
print(lista)

#generator comprehensions, assim como usamos em listas podemos criar geradores apenas
#substituindo por parenteses
print("Generator comprehensions")
lista = [x for x in range(10) if x % 3 == 0]
print(lista)
#ou 
print("com parenteses")
lista1 = (x for x in range(10) if x % 3 == 0)
print(lista1)
print(next(lista1))
print(next(lista1))
print(next(lista1))

#dicionario comprehension
print("Dicionario comprehension")

dicionario = {chave: valor * 2 for chave, valor in {"a": 1, "b": 2}.items()}
print(dicionario)
