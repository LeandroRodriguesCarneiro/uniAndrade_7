from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = max(0, valor)

    @abstractmethod
    def atacar(self):
        """Método que deve retornar o dano causado."""
        pass

    @abstractmethod
    def defender(self, dano):
        """Método que deve aplicar o dano na entidade."""
        pass

    def esta_vivo(self):
        return self.vida > 0