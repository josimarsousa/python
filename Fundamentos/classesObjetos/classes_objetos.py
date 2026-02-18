class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisao()
print(tv_quarto.ligada)
print(tv_quarto.canal)

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 5
print("Tv sala está ligada?", tv_sala.ligada)
print("Qual canal está na tv sala?",tv_sala.canal)