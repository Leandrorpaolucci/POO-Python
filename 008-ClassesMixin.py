""""
Quando Utilizar?

Você pode desejar reutilizar uma determinada feature em varias classes diferentes.
Para melhorar a modularidade

Mixin's é uma forma controlada de adicionar funcionalidades as classes.

Prioridades:
1) Não deve ser extendida
2) nao deve ser instanciada

Em python o conceito de mixins é o implemento utilizando herança multipla

"""

class Livro(object):

    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo

class LivroMixin(object):
    def renderizar(self):
        return 'x'
