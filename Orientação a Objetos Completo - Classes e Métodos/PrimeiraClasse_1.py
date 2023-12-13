class TV:

    def __init__(self):
        self.cor = 'preta'
        self.ligado = False
        self.tamanho = 55
        self.canal = "Menu Home"
        self.volume = 20

    def ligar_tv(self):
        ...



tv_sala = TV()
print(tv_sala.cor)

tv_quarto = TV()
print(tv_quarto.canal)