import tkinter as tk
from tkinter import ttk

class Aplicacao:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_1 = 0
        self.contador_2 = 0
        self.title("Contadores")
        self.geometry("250x100")
        self.cria_quadro()
        