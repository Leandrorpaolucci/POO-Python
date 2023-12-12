from abc import ABCMeta, abstractmethod

class MinhaClasseAbstrata(metaclass=ABCMeta):

    @abstractmethod
    def fazer_algo(self):
        pass

    @abstractmethod
    def fazer_algo_novamente(self, o_que_fazer):
        pass


obj = MinhaClasseAbstrata()