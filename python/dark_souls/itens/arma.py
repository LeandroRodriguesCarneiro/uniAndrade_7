from .item import Item

class Arma(Item):
    def __init__(self, nome, dano, resistencia):
        super().__init__(nome, tipo="arma")
        self.dano = dano
        self.resistencia = resistencia

    def usar(self, alvo):
        print(f"{alvo.nome} usa {self.nome} causando {self.dano} de dano.")
        return self.dano
