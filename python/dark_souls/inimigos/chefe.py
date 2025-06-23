from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome):
        super().__init__(nome, vida=200, dano=40)

    def atacar(self):
        print(f"{self.nome} ataca causando {self.dano} de dano.")
        return self.dano

    def especial(self):
        print(f"{self.nome} usa ataque especial causando 80 de dano!")
        return 80

    def defender(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")
