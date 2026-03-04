import sqlite3

feriados = [["2026-01-01", "Confraternizacao Universal"], ["2026-04-21", "Tiradentes"], 
["2026-05-01", "Dia do Trabalhador"], ["2026-09-07", "Dia da Independencia"], ["2026-11-02", "Dia de finados"], 
["2026-11-15", "Dia de Proclamacao da Republica"], ["2026-12-25", "Natal"]]

with sqlite3.connect("brasil.db") as conexao:
    conexao.execute("create table feriados(id integer primary key autoincrement, data date, descricao text)")
    conexao.executemany("insert into feriados(data, descricao) values(?, ?)", feriados)
    
conexao.commit()
conexao.close()
    