from .item import Item

class Potion(Item):
    def __init__(self, name, weight, effect, description, value, effect_amount):
        """
        :param name: Nome da poção.
        :param weight: Peso da poção.
        :param effect: Tipo de efeito da poção (ex.: "cura", "força", "velocidade").
        :param description: Descrição da poção.
        :param value: Valor monetário da poção.
        :param effect_amount: Quantidade do efeito (ex.: quantidade de cura ou aumento de atributos).
        """
        super().__init__(name, weight, effect, description, value)
        self._effect_amount = effect_amount  # Quantidade do efeito (como a quantidade de cura, etc.)

    @property
    def effect_amount(self):
        return self._effect_amount

    @effect_amount.setter
    def effect_amount(self, value):
        self._effect_amount = value

    def use(self, target):
        """
        Aplica o efeito da poção a uma entidade (target).
        Dependendo do tipo de efeito, a poção pode curar, aumentar força, etc.
        """
        if self.effect == "cura":
            target.hp += self.effect_amount
            print(f"{target.name} foi curado em {self.effect_amount} pontos de HP.")
        elif self.effect == "força":
            target.strenght += self.effect_amount
            print(f"A força de {target.name} aumentou em {self.effect_amount}.")
        elif self.effect == "velocidade":
            target.speed += self.effect_amount
            print(f"A velocidade de {target.name} aumentou em {self.effect_amount}.")
        elif self.effect == "magia":
            target.magic += self.effect_amount
            print(f"A magia de {target.name} aumentou em {self.effect_amount}.")
        else:
            print(f"A poção {self.name} não tem um efeito conhecido.")

    def __str__(self):
        return (f"{super().__str__()} Efeito: {self.effect} ({self.effect_amount})")

    def __repr__(self):
        return (f"Potion(name='{self.name}', weight={self.weight}, effect='{self.effect}', "
                f"description='{self.description}', value={self.value}, "
                f"effect_amount={self.effect_amount})")
