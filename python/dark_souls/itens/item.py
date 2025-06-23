from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def usar(self, alvo):
        pass
