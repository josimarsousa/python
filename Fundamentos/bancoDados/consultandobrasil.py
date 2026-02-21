import sqlite3

with sqlite3.connect("brasil.db") as conexao:
        conexao.row_factory = sqlite3.Row
        print(f"{'Id':3s} {'Estado':<20s} {'População':12s}")
        print("=" * 37)
        for estado in conexao.execute("SELECT * FROM estados ORDER BY nome"):
           print(f"{estado['id']:3d} {estado['nome']:20s} {estado['populacao']:12d}")
