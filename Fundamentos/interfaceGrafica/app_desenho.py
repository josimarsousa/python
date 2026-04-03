import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quadro = ttk.Frame(self)
        self.cria_barra()
        self.cria_area_de_desenho()
        self.title("Desenho")
        self.geometry("800x600")
        self.quadro.pack(expand=True, fill="both")
    
    
   