import json
from cadastro_site import Site

class GerenteSites:
    def __init__(self):
        self.sites = {}

    def carrega(self, nome_do_arquivo):
        with open(nome_do_arquivo) as arquivo:
            dados = json.load(arquivo)
        self.sites.clear()
        for dado in dados: 
            site = Site(
                id=dado.get("id"),
                categoria = dado.get("categoria"),
                data =  dado["data"],
                url = dado["url"],
                notas = dado.get("notas"))
            self.sites[site.id] = site
        
    def grava(self, nome_do_arquivo):
        with open(nome_do_arquivo, "w") as arquivo:
            dados = []
            for site in self .sites. values():
                dados.append({"id": site.id, "uri": site.uri, "notas": site.notas,
                "data": site.data,"categoria": site.categoria})
            json.dump(dados, arquivo, indent=2, sort_keys=True) 
