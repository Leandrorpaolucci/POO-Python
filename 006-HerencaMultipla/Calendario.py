class Calendario:
    
    meses = (31, 28, 31,30,31,30,31,31,30,31,30,31)

    def __init__(self, dia=1, mes=1, ano=2000, *args, **kwargs):
        super(Calendario, self).__init__(*args, **kwargs)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def ajustar_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f" A data atual é: {self.dia}/{self.mes}/{self.ano}." 
    
    def avancar_mes(self):
        dia_max = Calendario.meses[self.mes - 1]

        if self.dia == dia_max:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1

calendario = Calendario(31, 12 , 2023)
print(calendario)

calendario.avancar_mes()
print(calendario)