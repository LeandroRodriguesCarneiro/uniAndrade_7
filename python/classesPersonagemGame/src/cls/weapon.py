import random

from .item import Item

class Weapon(Item):
    def __init__(self, name, weight, effect, description, value, damage_type, damage_value):
        """
        :param name: Nome da arma.
        :param weight: Peso da arma.
        :param effect: Efeito da arma (por exemplo, "corte", "fogo", etc.).
        :param description: Descrição da arma.
        :param value: Valor monetário da arma.
        :param damage_type: Tipo de dano causado pela arma (ex.: "corte", "impacto").
        :param damage_value: Valor do dano que a arma causa.
        """
        super().__init__(name, weight, effect, description, value)
        self._damage_type = damage_type  # Tipo de dano (ex.: "corte", "fogo", etc.)
        self._damage_value = damage_value  # Valor do dano (quantidade de dano causado)

    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value):
        self._damage_type = value

    @property
    def damage_value(self):
        return self._damage_value

    @damage_value.setter
    def damage_value(self, value):
        self._damage_value = value

    def use(self, target):
        # Chance de esquiva baseada na velocidade
        dodge_chance = min(50, target.speed * 2)  # Máximo 50%
        roll = random.randint(1, 100)
        
        print(f"Tentando acertar {target.name} (Chance de esquiva: {dodge_chance}%, Dado: {roll})")

        if roll <= dodge_chance:
            print(f"{target.name} esquivou do ataque!")
        else:
            print(f"{target.name} foi atingido por {self.name} causando {self.damage_value} de dano ({self.damage_type})!")
            target.take_damage(self.damage_value)

    def __str__(self):
        return (f"{super().__str__()} | Tipo de Dano: {self.damage_type} | Dano: {self.damage_value}")

    def __repr__(self):
        return (f"Weapon(name='{self.name}', weight={self.weight}, effect='{self.effect}', "
                f"description='{self.description}', value={self.value}, "
                f"damage_type='{self.damage_type}', damage_value={self.damage_value})")
