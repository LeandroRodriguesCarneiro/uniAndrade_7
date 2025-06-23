from .jogador import Jogador

class Cavaleiro(Jogador):
    def __init__(self, nome):
        super().__init__(nome, vida=150)
        self.armadura = 50
        self.arma_equipada = None  # Arma inicialmente não equipada

    def atacar(self):
        if self.arma_equipada:
            dano = self.arma_equipada.dano
            print(f"{self.nome} ataca com {self.arma_equipada.nome} causando {dano} de dano.")
            return dano
        else:
            dano = 5  # Dano básico sem arma
            print(f"{self.nome} soca o inimigo causando {dano} de dano.")
            return dano

    def defender(self, dano):
        dano_reduzido = max(0, dano - (self.armadura * 0.3))
        self.vida -= dano_reduzido
        print(f"{self.nome} defendeu! Dano recebido: {dano_reduzido}. Vida atual: {self.vida}")

    def equipar_arma(self, arma):
        self.arma_equipada = arma
        print(f"{self.nome} equipou {arma.nome}.")
