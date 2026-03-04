import sqlite3

print(f"{'Região':<15} {'Estados':>7} {'Mínima':>13} {'Máxima':>13} {'Média':>13} {'Total':>13}")
print(f"{'='*15} {'='*7} {'='*13} {'='*13} {'='*13} {'='*13}")

with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute("""
        select regiao, count(*), min(populacao),
        max(populacao), avg(populacao), sum(populacao) as tpop
        from estados
        group by regiao having count(*) > 5 order by tpop desc"""):
        print("{0:<15} {1:7d} {2:13,} {3:13,} {4:13,.0f} {5:13,}".format(*regiao))
    
    print("-" * 79)
    dados_brasil = conexao.execute("""
        select count(*), min(populacao), max(populacao),
               avg(populacao), sum(populacao) from estados""").fetchone()
    print("{0:<15} {1:7d} {2:13,} {3:13,} {4:13,.0f} {5:13,}".format(
        "Brasil", *dados_brasil))