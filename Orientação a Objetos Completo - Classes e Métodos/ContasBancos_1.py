class ContaCorrente():
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.saldo_anterior = saldo  # Armazena o saldo anterior
        self.lis = -1000
        
    def notificar_limite_lis(self):
        if self.saldo < 0 <= self.saldo_anterior:
            mensagem = "Você entrou no cheque especial. Seu saldo está abaixo do limite LIS."
            mensagem += f"\nSeu saldo atual é de R$ {self.saldo:.2f}."
            # Adicione aqui a lógica para enviar notificações, se desejado
            return mensagem  # Retorna a mensagem de notificação
        else:
            return "Seu saldo não está no cheque especial."
        
    def calcular_porcentagem_uso_lis(self):
        if self.saldo < 0:
            uso_lis = abs(self.saldo)  # Calcula o valor do LIS usado
            porcentagem = (uso_lis / abs(self.lis)) * 100  # Calcula a porcentagem usada do LIS
            return f"Você utilizou {porcentagem:.2f}% do seu limite do LIS."
        else:
            return "Seu saldo está positivo, sem uso do cheque especial."
            
    def consultar_saldo(self):
        return f'Olá {self.nome}, o seu saldo atual é: R$ {self.saldo:.2f}'
    

    def depositar(self, valor):
        self.saldo_anterior = self.saldo  # Atualiza o saldo anterior antes do depósito
        self.saldo += valor
        return f'Olá {self.nome}, você depositou R$ {valor:.2f} R$.\nSaldo atual: R$ {self.saldo:.2f} R$.'

    def sacar_dinheiro(self, valor):
        self.saldo_anterior = self.saldo  # Armazena o saldo antes do saque
        if self.saldo - valor < self.lis:
            return f"Você não possui saldo suficiente para sacar o valor desejado.\nSeu saldo atual é de R$ {self.saldo:.2f}."
        else:
            self.saldo -= valor
            return f'Olá {self.nome}, VOCÊ UTILIZOU A FUNÇÃO SAQUE NO VALOR DE: R$ {valor:.2f} R$\nSaldo atual: R$ {self.saldo:.2f} R$.'

    def verificar_saldo_negativo(self):
        if self.saldo_anterior < 0:
            print("Estamos verificando se você utilizou o LIS")
            print(f"Seu saldo anterior é {self.saldo_anterior}, você entrou no cheque especial no seu último saque.")
            print(f"Saldo atual: {self.consultar_saldo()}")
        else:
            print("Seu saldo anterior não estava negativo.")


#Dados do cliente
pessoa_1 = ContaCorrente('Leandro', '123.456.789-11')
print(f"Olá {pessoa_1.nome}, bom dia! ")
print(f'Nome do Correntista: {pessoa_1.nome}')
print(f'CPF do Correntista: {pessoa_1.cpf}')

# Consultas de saldo
print("----------------------CONSULTA EXTRATO----------------------------")
print(f'Saldo atual do correntista: {pessoa_1.saldo}')
print(f'Você está consultando o seu saldo. {pessoa_1.consultar_saldo()}')

# Depósito
print("-----------------------DEPÓSITO---------------------------")
print(pessoa_1.depositar(1500))

# Consulta após o depósito
print("-----------------------CONSULTA APÓS O DEPÓSITO---------------------------")
print(f'SALDO: {pessoa_1.saldo}')

# Extrato final
print("=======================EXTRATO FINAL===================================")
print(f'Saldo Atual: {pessoa_1.saldo}')
print(f'Saldo Anterior: {pessoa_1.saldo_anterior}')
print(pessoa_1.sacar_dinheiro(1700))
print(pessoa_1.sacar_dinheiro(5))
print(pessoa_1.notificar_limite_lis())
print(pessoa_1.calcular_porcentagem_uso_lis())