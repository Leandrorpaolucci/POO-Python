class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def resetar(self):
        self.x, self.y = 0,0
        print("Resetamos o numero no eixo X e Y para zero!")

#a variavel recebe a classe criada, porem o init força dois argumentos criados como X e Y
num1 = int(input("Digite o valor de X: "))
num2 = int(input("Digite o valor de Y: "))

#verificando os valores que inicialmente no init X e Y receberam
p = Ponto(num1, num2) 
print(f'Eu recebi no p input o valor {p.x}')
print(f'Eu recebi no p input o valor {p.y}')
#resetando os numeros recebidos de X e Y com o método resetar
p.resetar() 
print(p.x, p.y) 

