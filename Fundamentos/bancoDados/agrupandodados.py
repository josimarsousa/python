import sqlite3

print("Regiao Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute("""
        SELECT regiao, count(*)
        FROM estados
        GROUP BY regiao"""):
        # regiao é uma tupla (nome_regiao, contagem)
        # Se nome_regiao for None (não existir no banco), usamos "Indefinido"
        nome_regiao = regiao[0] if regiao[0] else "Indefinido"
        contagem = regiao[1]
        print(f"{nome_regiao:6} {contagem:17}")        

conexao.commit()
conexao.close()