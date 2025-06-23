class NPC:
    def __init__(self, nome, dialogo):
        self.nome = nome
        self.dialogo = dialogo
        self.amizade = 0

    def falar(self):
        print(f"{self.nome} diz: {self.dialogo}")
