class SomentePares(list):

    def append(self, inteiro):

        if not isinstance(inteiro, int):
            raise TypeError('Somente Inteiros podem ser adicionados')

        if inteiro % 2:
            raise ValueError('Somente Pares')
        
        super().append(inteiro)


# nome = 'Leandro'
# inteiro_par = 10
# inteiro_impar = 5


# sp = SomentePares()
# #sp.append(nome)
# print(sp.append(inteiro_par))
# #sp.append(inteiro_impar)

###################################################################
def algo():
    print('POO Python')

    raise Exception('Lançando exceção')

    print('Depois da Exceção')

    return 'Sucesso'

algo()


