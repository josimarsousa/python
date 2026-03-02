import sqlite3

print("Regiao Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute("""
        SELECT regiao, count(*)
        FROM estados
        GROUP BY regiao"""):
        nome_regiao = regiao[0] if regiao[0] else "Indefinido"
        print(f"{nome_regiao:6} {regiao[1]:17}")
           

