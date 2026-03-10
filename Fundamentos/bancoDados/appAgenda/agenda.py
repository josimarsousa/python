import sqlite3

banco = """"
    create table tipos(id integer primary key autoincrement, descricao text);
    create table nome(id integer primary key autoincrement, nome text);
    create table telefones(id integer primary key autoincrement, id_nome integer, numero text, id_tipo integer);
    insert into tipos(descricao) values ("Celular");
    insert into tipos(descricao) values ("Residencial");
    insert into tipos(descricao) values ("Comercial");
    insert into tipos(descricao) values ("Trabalho");
    """

class DBAgenda:
    def __init__(self, banco):
        self.tiposTelefone = DBTiposTelefone()
        self.banco = banco
        novo = not os.path.isfile(banco)
        self.conexao = sqlite3.connect(banco)
     