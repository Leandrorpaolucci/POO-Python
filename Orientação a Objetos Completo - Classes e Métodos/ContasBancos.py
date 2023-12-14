class ContaCorrente():

    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def consultar_saldo(self):
        return f'Olá {self.nome}, o seu saldo atual é: R$ {self.saldo:.2f}.'
    
    def depositar(self, valor):
        self.saldo += valor
        return f'Olá {self.nome}, você recebeu um deposito de R$ {self.saldo:.2f} reais.'


    def sacar_dinheiro(self, valor):
        self.saldo -= valor
        return f'Olá {self.nome}, você sacou o valor de R$ {self.saldo:.2f} reais.'
    
   

############################################################################
pessoa_1 = ContaCorrente('Camila', '123.456.789-11')
print(f'Nome do Correntista: {pessoa_1.nome}')
print(f'CPF do Correntista: {pessoa_1.cpf}')
print(f'Saldo atual do correntista: {pessoa_1.saldo}')

###################################-MÉTODOS-#################################
print(pessoa_1.consultar_saldo())

print(pessoa_1.depositar(2300))
print(pessoa_1.saldo)

print(pessoa_1.sacar_dinheiro(500000))
print(pessoa_1.saldo)
