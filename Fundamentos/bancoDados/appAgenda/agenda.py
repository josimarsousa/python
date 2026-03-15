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
        consulta = self.conexao.execute("select * from nomes where id = ?", (id,))
        return self.carrega(consulta.fetchone())

    def carrega_por_nome(self, nome):
        consulta = self.conexao.execute(
            "select * from nomes where nome = ?", (nome.nome,))
        return self.carrega(consulta.fetchone())

    def carrega(self, consulta):
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta["nome"], consulta["id"]))
        for telefone in self.conexao.execute(
                    "select * from telefones where id_nome = ?", (novo.nome.id,)):
            ntel = DBTelefone(telefone["numero"], None,
                            telefone["id"], telefone["id_nome"])
            for tipo in self.tiposTelefone: 
                if tipo.id == telefone["id_tipo"]:
                    ntel.tipo = tipo
                    break
            novo.telefones.adiciona(ntel)
        return novo

    def lista(self):
        consulta = self.conexao.execute("select * from nomes order by nome")
        for registro in consulta:
            yield self.carrega(registro)
    
    def novo(self, registro):
        try:
            cur -= self.conexao.cursor()
            cur.execute("insert into nomes(nome) values (?)",
                        (str(registro.nome,)))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute("""insert into telefones(numero, 
                            id_tipo, id_nome) values (?,?,?)""",
                        (telefone.numero, telefone.tipo.id,
                         registro.nome.id))
                telefone.id = cur.lastrowid
            self.conexao.commit()
        except Exception:
            self.conexao.rollback()
            raise
        finally:
            cur.close()
