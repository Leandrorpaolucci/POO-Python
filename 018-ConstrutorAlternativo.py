class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    #contrutor alternativo
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)
    
p = Pessoa('Leandro')
print(p.nome)

s = Pessoa.outro_construtor('Leandro classmethod')
print(s.nome)
