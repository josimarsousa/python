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
        self.conexao.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()
    
    def carregaTipos(self):
        for tipo in self.conexao.execute("SELECT * FROM tipos"):
            id_ = tipo["id"]
            descricao = tipo["descricao"]
            self.tiposTelefone.adiciona(DBTipoTelefone(id_, descricao))

    def cria_banco(self):
        self.conexao.executescript(BANCO)

    def pesquisaNome(self):
        if not isinstance(nome, DBNome):
            raise TypeError("nome deve ser do tipo DBNome") 
        achado = self.conexao.execute(""" select count(*) from nomes where nome = ?""", (nome.nome,)).fetchone()
        
        if achado[0] > 0:
            return self.carrega_por_nome(nome)
        else:
            return None
    def carrega_por_id(self, nome):
        consulta = self.conexao.execute("select * from nomes where nome = ?", (nome.nome,))
        return self.carrega(consulta.fetchone())