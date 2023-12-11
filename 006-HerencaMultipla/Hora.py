class Relogio:

    def __init__(self, hora=0, minuto=0, segundos=0):
        self.hora = hora
        self.minuto = minuto
        self.segundos = segundos

    def ajustar_hora(self, hora, minuto, segundos=0):
        self.hora = hora
        self.minuto = minuto
        self.segundos = segundos

    def __str__(self):
        return f"A hora atual: {self.hora:02}:{self.minuto:02}:{self.segundos:02}"

    def ticktok(self):
        if self.segundos == 59:
            self.segundos = 0
            if self.minuto == 59:
                self.minuto = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.minuto += 1
        else:
            self.segundos += 1

relogio = Relogio(12, 30, 59)
print(relogio)

relogio.ticktok()
print(relogio)
