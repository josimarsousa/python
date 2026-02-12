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
"""

#modulo os.path
import os.path
for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)

