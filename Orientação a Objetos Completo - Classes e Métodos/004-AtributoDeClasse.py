class TV:

    #FORA DO METODO INIT, modificaões fora do init, modificamos a classe inteira
    cor = 'preta'
    #TV.cor = 'branca'
    def __init__(self, tamanho):

        self.ligado = False
        self.tamanho = tamanho
        self.canal = "Menu Home"
        self.volume = 20

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        

tv_sala = TV(55)
tv_quarto = TV(tamanho=48)

print(tv_sala.cor)