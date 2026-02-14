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
"""
#exibindo componentes de data e hora

import time

agora = time.localtime()
print(f"Ano: {agora.tm_year}")
print(f"Mês: {agora.tm_mon}")
print(f"Dia: {agora.tm_mday}")
print(f"Hora: {agora.tm_hour}")
print(f"Minuto: {agora.tm_min}")
print(f"Segundo: {agora.tm_sec}")
print(f"Dia da semana: {agora.tm_wday}")
print(f"Dia do ano: {agora.tm_yday}")
print(f"Fuso horário: {agora.tm_isdst}\n")

#tabela de formatação de strftime
print("Tabela com códigos de formatação de strftime\n")
print(f"%a - dia da semana abreviado")
print(f"%A - dia da semana completo")
print(f"%b - mês abreviado")
print(f"%B - mês completo")
print(f"%c - data e hora local")
print(f"%d - dia do mês com zero à esquerda")
print(f"%H - hora no formato 24h(00-23)")
print(f"%m - mês com zero à esquerda")
print(f"%y - ano com dois dígitos")
print(f"%Y - ano com quatro dígitos")
print(f"%H - hora com zero à esquerda")
print(f"%I - hora com zero à esquerda")
print(f"%M - minuto com zero à esquerda")
print(f"%S - segundo com zero à esquerda")
print(f"%p - AM ou PM")

#exemplo
print(time.strftime("%a, %d %b %Y %H:%M:%S\n", agora))
print(time.strftime("Hoje é o dia %j dia do ano de %Y\n", agora))
print(time.strftime("A hora atual é %H:%M:%S\n", agora))
print(time.strftime("%b %d/%m/%y %H:%M\n", agora))
