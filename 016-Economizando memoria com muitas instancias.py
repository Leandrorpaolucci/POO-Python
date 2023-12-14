"""
__slots__ é restrito para adicionar mais de um atributo após ser instanciado, ou seja
você precisa definir muito bem os parametros para que mais tarde não sejam alterados.

A memoria utilizada nos slot, variam da quantidade de instancias

ferramenta de otimização

"""

class Pessoa:

    __slots__ = ['Nome', 'Idade', 'Peso']

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    