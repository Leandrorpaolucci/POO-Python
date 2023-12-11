class Funcionario:

    def __init__(self, nome, idade, cpf, salario):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario
        #self.__x = x #privado com dois underscore _ _ = __

    def bonificacao(self):
        return self.salario * 0.20
    
    def salario_total(self):
        return self.salario + self.bonificacao() 


class Gerente(Funcionario):
    
    def __init__(self, nome, idade, salario , cpf, senha):
        super().__init__(nome, idade, salario, cpf)
        self.senha = senha

    def bonificacao_gerente(self):
        self.beneficio_gerente =  1000
        return super().bonificacao()  + self.beneficio_gerente


g = Gerente('Leandro', 28, '470-111-111-11', 2200, 'minha_senha')
print(g.nome)
print(g.idade)
print(g.cpf)
print(g.salario)
print(g.senha)
