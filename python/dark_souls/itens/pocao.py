from .item import Item

class Pocao(Item):
    def __init__(self, nome, efeitos: list):
        """
        efeitos: lista de objetos do tipo Efeito
        """
        super().__init__(nome, tipo="pocao")
        self.efeitos = efeitos

    def usar(self, alvo):
        print(f"{alvo.nome} usa {self.nome}.")
        for efeito in self.efeitos:
            efeito.aplicar(alvo)
