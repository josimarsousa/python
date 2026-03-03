import sqlite3

with sqlite3.connect("brasil.db") as conexao:
        conexao.row_factory = sqlite3.Row
        print(f"{'Id':3s} {'Estado':<20s} {'População':12s} {'Região':15s} {'Sigla':6s}")
        print("=" * 60)
        for estado in conexao.execute("SELECT * FROM estados ORDER BY nome"):
            sigla = estado['sigla'] if estado['sigla'] else "N/A"
            print(f"{estado['id']:3d} {estado['nome']:20s} {estado['populacao']:12d} {estado['regiao']:15s} {sigla:6s}")
