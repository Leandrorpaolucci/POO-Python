class TV:

    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligado = False
        self.tamanho = tamanho
        self.canal = "Menu Home"
        self.volume = 20

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV(tamanho=55)
tv_quarto = TV(48)

print(f'Meu canal atual: atributo padrão definido -> {tv_sala.canal}')

tv_sala.mudar_canal('SBT')
print(f'Parametro da TV intuitivo: {tv_sala.tamanho}')
print(f'Cheguei no Método/Função dentro da classe "Mudar Canal": {tv_sala.canal}')

tv_quarto.mudar_canal('Youtube')
print(f'Atributo declarado pela ordem self da classe: {tv_quarto.tamanho}')
print(f'Cheguei no Método/Função dentro da classe "Mudar Canal": {tv_quarto.canal}')

