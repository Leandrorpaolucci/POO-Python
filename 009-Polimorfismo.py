"""
Polimorfismo - 
A tecnica do poliformismo, se uma classe herda os metodos de outra classe e modifica esses
métodos, isso é chamado de polimorfismo

"""
import math

class Forma():

    def __init__(self):
        print('Construtor da Forma')

    def area(self):
        print('Area da forma')
    
    def perimetro(self):
        print('Perimetro da forma')

    def descricao(self):
        print('Descrição da forma')

class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def descricao(self):
        #return super().descricao()
        print("Descrição do Circulo na classe Circulo")



quadrado = Quadrado(2)
print(f'Area: {quadrado.area()}')
print(f'Perimetro: {quadrado.perimetro()}')

circulo = Circulo(3)
print(f'Area: {circulo.area():.2f}')
print(f'Perimetro: {circulo.perimetro():.2f}')
circulo.descricao()

forma = Forma()
forma.area()