class ContaCorrente():
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.saldo_anterior = saldo  # Nova variável para armazenar o saldo anterior

    def consultar_saldo(self):
        return f'Olá {self.nome}, o seu saldo atual é: R$ {self.saldo:.2f}.'

    def depositar(self, valor):
        self.saldo += valor
        return f'Olá {self.nome}, você recebeu um depósito de R$ {self.saldo:.2f} reais.'

    def sacar_dinheiro(self, valor):
        self.saldo_anterior = self.saldo  # Armazena o saldo antes do saque
        if self.saldo - valor < 0:
            print(f"Você não possui saldo suficiente para sacar o valor desejado.")
            print(f"Seu saldo atual é de R$ {self.saldo:.2f}.")
        else:
            self.saldo -= valor
            return f'Olá {self.nome}, você tinha o valor de {self.saldo_anterior:.2f} R$, você sacou o valor de {valor:.2f} R$. Saldo Atual Após o saque: {self.saldo:.2f} R$'


pessoa_1 = ContaCorrente('Leandro', '123.456.789-11')
print(f'Nome do Correntista: {pessoa_1.nome}')
print(f'CPF do Correntista: {pessoa_1.cpf}')
print(f'Saldo atual do correntista: {pessoa_1.saldo}')
print(f'Você está consultando o seu saldo. Saldo atual: {pessoa_1.consultar_saldo()}')
pessoa_1.depositar(2300)
print(f'SALDO: {pessoa_1.saldo}')
pessoa_1.depositar(8300)
print(f'SALDO: {pessoa_1.saldo}')
pessoa_1.sacar_dinheiro(2400)
print(f'Saldo Atual: {pessoa_1.saldo}')
print(f'Saldo Anterior: {pessoa_1.saldo_anterior}')

