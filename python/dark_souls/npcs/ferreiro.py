from .npc import NPC

class Ferreiro(NPC):
    def __init__(self, nome):
        super().__init__(nome, dialogo="Posso forjar algo para você.")
        self.inventario = []
        self.metal = 100

    def vender_item(self, item):
        self.inventario.append(item)
        print(f"Ferreiro vendeu {item.nome}.")
