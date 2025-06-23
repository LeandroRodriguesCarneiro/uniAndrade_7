from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome):
        super().__init__(nome, vida=60, dano=15)

    def atacar(self):
        print(f"{self.nome} morde causando {self.dano} de dano.")
        return self.dano

    def especial(self):
        print(f"{self.nome} cospe veneno causando 25 de dano.")
        return 25

    def defender(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")
