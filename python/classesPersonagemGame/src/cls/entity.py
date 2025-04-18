from abc import ABC, abstractmethod
from .item import Item

class Entity(ABC):
    def __init__(self, name: str, hp: int, strenght: int, speed: int, magic: int):
        self._name = name
        self._hp = hp
        self._strenght = strenght
        self._speed = speed
        self._magic = magic
        self._inventory = []  
        self._effects = []

    # Getters e setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def strenght(self):
        return self._strenght

    @strenght.setter
    def strenght(self, value):
        self._strenght = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def magic(self):
        return self._magic

    @magic.setter
    def magic(self, value):
        self._magic = value

    @property
    def effects(self):
        return self._effects

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    # Métodos de inventário
    def total_weight(self):
        return sum(item.weight for item in self._inventory)

    def add_item(self, item: Item):
        """Adiciona um item ao inventário, se o peso total não exceder a força."""
        if self.total_weight() + item.weight > self._strenght:
            print(f"{self.name} não consegue carregar {item.name}, peso excede o limite de força.")
        else:
            self._inventory.append(item)
            print(f"{item.name} foi adicionado ao inventário de {self.name}.")

    def drop_item(self, item: Item):
        """Remove um item do inventário."""
        if item in self._inventory:
            self._inventory.remove(item)
            print(f"{item.name} foi removido do inventário de {self.name}.")
        else:
            print(f"{item.name} não está no inventário.")

    def show_inventory(self):
        """Mostra todos os itens no inventário."""
        if not self._inventory:
            return "Inventário vazio."
        return "\n".join([f"- {item}" for item in self._inventory])

    def show_effects(self):
        """Mostra todos os efeitos ativos."""
        if not self._effects:
            return "Nenhum efeito ativo."
        return "\n".join([f"* {effect}" for effect in self._effects])

    def add_effect(self, effect: str):
        """Adiciona um efeito à lista de efeitos ativos."""
        self._effects.append(effect)
        print(f"{self.name} agora está sob o efeito de: {effect}")

    def remove_effect(self, effect: str):
        """Remove um efeito da lista de efeitos ativos."""
        if effect in self._effects:
            self._effects.remove(effect)
            print(f"{self.name} não está mais sob o efeito de: {effect}")
        else:
            print(f"Efeito {effect} não encontrado nos efeitos ativos.")

    # Métodos de dano
    def take_damage(self, amount: int):
        """Reduz o HP da entidade. Se HP chegar a 0 ou menos, a entidade morre."""
        self._hp -= amount
        if self._hp <= 0:
            self._hp = 0
            print(f"{self.name} morreu.")
        else:
            print(f"{self.name} recebeu {amount} de dano. HP restante: {self._hp}.")

    def is_alive(self):
        """Retorna se a entidade está viva ou não."""
        return self._hp > 0

    # Método de pilhagem
    def pilhar(self, other_entity: "Entity"):
        """Permite pilhar itens de uma outra entidade derrotada."""
        if not other_entity.is_alive():
            if other_entity._inventory:
                self._inventory.extend(other_entity._inventory)  # Transfere todos os itens
                other_entity._inventory.clear()  # Limpa o inventário da entidade derrotada
                print(f"{self.name} pilhou os itens de {other_entity.name}.")
            else:
                print(f"{other_entity.name} não tem itens para pilhar.")
        else:
            print(f"{other_entity.name} ainda está viva. Não é possível pilhar.")

    # Métodos de exibição
    def __str__(self):
        return (f"{self.name} | HP: {self.hp} | Força: {self.strenght}, "
                f"Velocidade: {self.speed}, Magia: {self.magic}\n"
                f"Efeitos Ativos: {', '.join(self._effects) if self._effects else 'Nenhum efeito ativo.'}")

    def __repr__(self):
        return (f"Entity(name='{self.name}', hp={self.hp}, strenght={self.strenght}, "
                f"speed={self.speed}, magic={self.magic}, "
                f"inventory={self._inventory}, effects={self._effects})")
