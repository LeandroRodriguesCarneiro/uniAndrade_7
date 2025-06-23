from abc import abstractmethod
from ..entidade import Entidade

class Jogador(Entidade):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.inventario = []

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self, dano):
        pass

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} obteve {item.nome}.")

    def usar_item(self, item):
        if item in self.inventario:
            item.usar(self)
            self.inventario.remove(item)
        else:
            print(f"{item.nome} não está no inventário.")
