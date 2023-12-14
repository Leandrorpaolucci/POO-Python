class A:

    def fazer_algo(self):
        ...

    def outro_metodo(self):
        ...

    def algum_metodo(self, nome):
        print(nome)

class B:

    def __init__(self):
        self.a = A()

    def fazer_algo(self):
        # delega para self.a instancia interna da classe B
        return self.a.fazer_algo()
    
    def outro_metodo(self):
        # delega para self.a instancia da classe B
        return self.a.outro_metodo()
    
    def __getattr__(self, nome):  #pega tudo para leitura de atributos
        return getattr(self.a, nome)
    
b = B()
print(b.fazer_algo()) # chama B.fazer_algo() (existe em B)
print(b.algum_metodo('python')) # chama B.__getattr__('algum metodo') e delega para A.algum_metodo
    
