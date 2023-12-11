class Ponto:

    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def resetar(self):
        self.x, self.y = 0,0
        print("Resetamos o numero no eixo X e Y para zero!")

    def mover(self, x, y):
        self.x, self.y = x, y
        

#a variavel recebe a classe criada, porem o init força dois argumentos criados como X e Y
num1 = int(input("Digite o valor de X: "))
num2 = int(input("Digite o valor de Y: "))

#verificando os valores que inicialmente no init X e Y receberam
p = Ponto(num1, num2) 
print(f'Eu recebi no p input o valor {p.x}')
print(f'Eu recebi no p input o valor {p.y}')
#resetando os numeros recebidos de X e Y com o método resetar
#p.resetar() 

# -> chamamos a função resetar á partir da classe, passando como p como argumento self
Ponto.resetar(p)
print(p.x, p.y) 

p.mover(10, 20)
print(p.x, p.y) 
