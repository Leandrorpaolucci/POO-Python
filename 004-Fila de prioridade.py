import heapq

class FilaPrioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]
    
class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome
    

fila = FilaPrioridade()
fila.inserir(Item('Leandro'), 28)
fila.inserir(Item('Camila'), 22)
fila.inserir(Item('Arthur'), 1)

print(fila.remover())
print(fila.remover())
