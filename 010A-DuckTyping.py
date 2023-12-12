class Pato:

    def quack(self):
        print('Quack, Quack - PATO')

class Pessoa:

    def quack(self):
        print("Eu sou um ser HUMANO e imito um quack")

def fazer_quack(obj):
    # EAFP -Easier to ask for forgiveness than permission
    try:
        obj.quack()
    except AttributeError as e:
        print(e)



'''
def fazer_quack(obj):
    # LBYL - Não pythonico
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            obj.quack()
'''

""" Isso nao é Pythonico

def fazer_quack(obj):

    if isinstance(obj, Pato):
        obj.quack()
    else:
        print("isso tem que ser um PATO")

# pato = Pessoa()
# pato.quack()

# pessoa = Pessoa()
# pessoa.quack()
"""

pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
