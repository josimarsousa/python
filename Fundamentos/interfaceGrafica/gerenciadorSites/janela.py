import tkinter as tk
import tkinter.ttk as ttk
from cadastraSite import CadastraSite
from data import Data

class Janela(tk.Toplevel):
    min_x = 300
    min_y = 300
    padxy = 10
    def __init__(self, parent, site, on_change=None):
        super().__init__(parent)
        self.geometry(f"{self.min_x}x{self.min_y}")
        self.title("Site")
        self.padding = {"padx": self.padxy, "pady": self.padxy}
        self.on_change = on_change
        self.cria_controles()
        self.minizable(self.min_x, self.min_y)
        self.captura_site(site)

    def captura_site(self, site):
        self.site = site or Site()
        self.url.set(self.site.url or "")
        self.data.set(self.site.data)
        self.categoria.set(self.site.categoria or "")
        self.t_notas.delete("1.0", tk.END)
        self.t_notas.insert(tk.END, self.site.notas or "")
    
    def cria_controles(self):
        self.f_url = ttk.Frame(self)
        self.f_url.grid(row=0, column=0, columnspan=3, sticky=tk.EW, **self.padding)
        self.l_url = ttk.Label(self.f_url, text="URL")
        self.l_url.pack(anchor=tk.W)
        

