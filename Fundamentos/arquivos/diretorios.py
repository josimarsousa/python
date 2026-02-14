#criando diretório
import os
"""
os.mkdir("d")
os.mkdir("e")
os.mkdir("f")
print(os.getcwd())
os.chdir("d")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("f")
print(os.getcwd())

#criando diretorios intermédiarios de uma vez
os.makedirs("avos/pais/filhos")


#criando um arquivo e o fecha imediatamente
open("moribundo.txt",   "w").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("moribundo.txt")


#listando arquivos e diretorios
print(os.listdir("."))
print(os.listdir("avos"))
print(os.listdir("avos/pais"))

#criando e renomeando um diretorio
os.mkdir("velho")
os.rename("velho", "novo")
print(os.listdir("."))


#a funcao rename tambem pode mover arquivos.
os.makedirs("avo/pai/filho")
os.makedirs("avo/mae/filha")
os.rename("avo/mae/filha", "avo/mae/filho")

#cria um arquivo e o fecha imediatamente
open("moribundo.txt", "w").close()
os.mkdir("vago")
os.rmdir("vago")
#os.rmdir("moribundo.txt") = esta linha remove o arquivo criando anteriormente


#modulo os.path
import os.path
for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)
"""
#verificando se um diretório já existe
import os.path
if os.path.exists("z"):
    print("O diretório z existe")
else:
    print("O diretório z não existe")

#propriedades de um arquivo
import os.path
import time
import sys
nome = sys.argv[0]
if len(sys.argv) > 1:
    nome = sys.argv[1]
else:
    print("Nenhum arquivo passado. Usando o próprio script como exemplo.")

print(f"Nome: {nome}")
print(f"Tamanho: {os.path.getsize(nome)} bytes")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")
print(f"Modificado: {time.ctime(os.path.getmtime(nome))}")
print(f"Acessado: {time.ctime(os.path.getatime(nome))}")

#funcao para manipular o tempo
import time

agora = time.time()
print("Data e hora")
print(agora)
print("função ctime")
print(time.ctime(agora))

#estrutura tempo
print("estruturas de tempo")
agora2 = time.struct_time((2010, 6, 23, 18, 23, 40, 2, 174, 1))
segundos = time.mktime(agora2)
print(time.gmtime(segundos))
