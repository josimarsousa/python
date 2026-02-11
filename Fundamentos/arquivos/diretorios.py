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
"""

#listando arquivos e diretorios
print(os.listdir("."))
print(os.listdir("avos"))
print(os.listdir("avos/pais"))
