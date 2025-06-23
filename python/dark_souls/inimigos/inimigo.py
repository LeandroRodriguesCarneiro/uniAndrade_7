from abc import abstractmethod
from ..entidade import Entidade

class Inimigo(Entidade):
    def __init__(self, nome, vida, dano):
        super().__init__(nome, vida)
        self.dano = dano

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def especial(self):
        pass

    @abstractmethod
    def defender(self, dano):
        pass
