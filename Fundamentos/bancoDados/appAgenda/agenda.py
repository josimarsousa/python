import sqlite3

banco = """"
    create table tipos(id integer primary key autoincrement, descricao text);
    create table nome(id integer primary key autoincrement, nome text);
    create table telefones(id integer primary key autoincrement, id_nome integer, numero text, id_tipo integer);
    
    """
