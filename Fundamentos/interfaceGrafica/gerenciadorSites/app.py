import tkinter as tk
import tkinter.ttk as ttk
from gerente import GerenteSites

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
        self.minimize(self.MIN_X, self.MIN_Y)
        
