from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def dizer_algo(self):
        return 'Eu sou um animal'


class Cachorro(Animal):

    def dizer_algo(self):
        s = super(Cachorro, self).dizer_algo()
        return '%s %s' % (s, 'AU AU')

c = Cachorro()
print(c.dizer_algo())
