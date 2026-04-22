import tkinter as tk
import tkinter.ttk as ttk
from gerente import GerenteSites
from janela import Janela

class App(tk.Tk):
    MIN_X = 800
    MIN_Y = 200
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Controle de sites interessantes")
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.cria_controles()
        self.gerente = GerenteSites()
        self.gerente.carrega("dados.json")
        self.mostra_dados()
        self.minsize(self.MIN_X, self.MIN_Y)

    def cria_controles(self):
        self.quadro = ttk.Frame(self)
        self.quadro.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.grid_rowconfigure(0, weight=1)
        self.tabela = ttk.Treeview(self.quadro, columns=["url", "categoria", "data", "notas"], show="headings")
        self.tabela.heading("url", text="URL")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("categoria", anchor=tk.CENTER)
        self.tabela.heading("data", text="Data")
        self.tabela.heading("data", anchor=tk.CENTER)
        self.tabela.heading("notas", text="Notas")
        self.tabela.grid(
            row=0,
            column=0,
            sticky=tk.NSEW,
        )
        self.tabela.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(self.quadro ,orient=tk.VERTICAL, command=self.tabela.yview)
        self.tabela.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NSEW)
        self.quadro.grid_columnconfigure(0, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.quadro.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.tabela.bind("<Double-Button-1>", self.abre_janela)
        
    def adiciona_site_a_tabela(self, site):
        self.tabela.insert("", tk.END, values=(site.url, site.categoria, site.data, site.notas), iid=site.id)

    def mostra_dados(self):
        for site in self.gerente.sites.values():
            self.adiciona_site_a_tabela(site)

    def pega_selecionado(self):
        if item_selecionado := self.tabela.selection():
            id_selecionado = item_selecionado[0]
            return id_selecionado
        return None

    def abre_janela(self, event):
        if id_selecionado := self.pega_selecionado():
            site = self.gerente.sites[id_selecionado]
        else:
            site = None
        self.mostra_site(site)

    def mostra_site(self, site):
        self.janela = Janela(self, site, on_change=self.atualiza)
        self.janela.grab_set()

App().mainloop()   
