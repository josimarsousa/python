import sqlite3

with sqlite3.connect("brasil.db") as conexao:
    conexao.execute("""alter table estados add sigla text""")

    conexao.execute("""alter table estados add regiao text""")

conexao.commit()
conexao.close()