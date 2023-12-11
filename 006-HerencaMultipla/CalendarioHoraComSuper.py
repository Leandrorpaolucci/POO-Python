from Hora import *
from Calendario import *

# MRO 


class CalendarioRelogio(Relogio, Calendario):
    # MRO - >> Method Resolution Order -> é quem define a ordem da execução dos Métodos
    
    def __init__(self, hora, minuto, segundos, dia, mes, ano):
        #Exemplo, chamando os "Construtores das duas classes criadas" #Relogio MRO
        Relogio.__init__(self, hora, minuto, segundos)

        #Exemplo, chamando os "Construtores das duas classes criadas" #Calendario Respeitando o MRO
        Calendario.__init__(self, dia, mes, ano)

    #Sobreescrevendo o str
    def __str__(self):
        return Relogio.__str__(self) + ',' + Calendario.__str__(self)
    
    def ticktok(self):
        hora_anterior = self.hora 
        Relogio.ticktok(self)
        if (self.hora < hora_anterior):
            self.avancar_mes()

    
"""
HERANÇA MULTIPLA: COM ESSE EXEMPLO, UTILIZAMOS DUAS CLASSES ISOLADAS PARA CRIAR UM NOVO SOFTWARE
UTILIZAMOS A CLASSE HORA + A CLASSE CALENDARIO, ASSIM PUDEMOS FAZER A HERANÇA MULTIPLA E UNIFICAMOS 
AS FUNCIONALIDADES DE AMBAS AS CLASSES PARA FORMAR UMA FERRAMENTA MELHOR.
"""

calendario_relogio = CalendarioRelogio(23, 59, 59, 31, 12, 2023)
print(f'Utilizando a classe CalendarioRelogio: {calendario_relogio}')

calendario_relogio.ticktok()
print(f'Utilizando a classe CalendarioRelogio: {calendario_relogio}')

print(CalendarioRelogio.mro())

