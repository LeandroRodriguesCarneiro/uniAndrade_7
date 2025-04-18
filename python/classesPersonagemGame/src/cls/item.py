from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, weight, effect, description, value: float):
        self._name = name
        self._weight = weight
        self._effect = effect
        self._description = description
        self._value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, value):
        self._effect = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @abstractmethod
    def use(self, target):
        """
        Aplica o efeito do item a uma entidade (target).
        As subclasses devem implementar esse método.
        """
        pass

    def __str__(self):
        return (f"{self.name} - {self.description} "
                f"(Peso: {self.weight}, Efeito: {self.effect}, Valor: {self.value} moedas)")

    def __repr__(self):
        return (f"Item(name='{self.name}', weight={self.weight}, "
                f"effect='{self.effect}', description='{self.description}', value={self.value})")
