import sqlite3

print("Regiao Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexao:
    cursor = conexao.execute("""SELECT regiao, COUNT(*) FROM estados GROUP BY regiao""")
    for regiao in conexao.execute("""
        select regiao, count(*)
        from estados
        group by regiao"""):
        print(f"{0:6} {1:17}".format(*regiao))        

conexao.commit()
conexao.close()