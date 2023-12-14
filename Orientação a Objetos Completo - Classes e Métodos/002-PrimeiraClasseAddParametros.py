class TV:

    def __init__(self):
        self.cor = 'preta'
        self.ligado = False
        self.tamanho = 55
        self.canal = "Menu Home"
        self.volume = 20

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV()
tv_quarto = TV()

print(f'Meu canal atual: atributo padrão definido -> {tv_sala.canal}')

tv_sala.mudar_canal('SBT')
print(f'Cheguei no Método/Função dentro da classe "Mudar Canal": {tv_sala.canal}')

tv_quarto.mudar_canal('Youtube')
print(f'Cheguei no Método/Função dentro da classe "Mudar Canal": {tv_quarto.canal}')