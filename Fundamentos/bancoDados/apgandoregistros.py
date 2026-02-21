import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""DELETE FROM contatos
                                 WHERE nome = 'teste'""")
        print("Registros apagados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
            print("Alteração realizada com sucesso")
        else:
            conexao.rollback()
            print("Alteração não realizada")
