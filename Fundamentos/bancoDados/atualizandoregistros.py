import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""UPDATE contatos
                        set telefone = '35987653434'
                        where nome = 'João'""")
        conexao.commit()