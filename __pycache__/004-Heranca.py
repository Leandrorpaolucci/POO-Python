class MinhaClasse(object):
    pass

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF

class PessoaJuridica(Pessoa):
    
    def __init__(self, CNPJ, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ


p1 = Pessoa('Leandro', 28)
print(p1.nome)
print(p1.idade)

p2 = PessoaFisica('470.111.111-11', 'Leandro', 28)
print(p2.CPF, p2.nome, p2.idade)