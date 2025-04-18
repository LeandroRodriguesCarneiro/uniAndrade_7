from .entity import Entity

class Monster(Entity):
    def __init__(self, name: str, hp: int, strenght: int, speed: int, magic: int, monster_type: str):
        super().__init__(name, hp, strenght, speed, magic)  # Chama o construtor da classe base Entity
        self._monster_type = monster_type  # Tipo do monstro, por exemplo: Goblin, Dragão, etc.

    # Getter e Setter para monster_type
    @property
    def monster_type(self):
        return self._monster_type

    @monster_type.setter
    def monster_type(self, value):
        self._monster_type = value

    # Método para atacar outra entidade
    def attack(self, target: Entity):
        if target.is_alive():
            # O dano é baseado na força do monstro
            damage = self._strenght
            target.take_damage(damage)  # O monstro ataca a entidade-alvo
            print(f"{self.name} atacou {target.name} causando {damage} de dano!")
        else:
            print(f"{target.name} já está derrotado!")

    # Método de rotação de comportamento - monstro ataca de acordo com uma escolha aleatória de alvo
    def choose_target(self, entities: list):
        """Escolhe um alvo aleatoriamente de uma lista de entidades."""
        import random
        target = random.choice(entities)
        print(f"{self.name} escolheu atacar {target.name}!")
        return target

    # Exibição do tipo de monstro
    def __str__(self):
        return (f"{self.name} ({self.monster_type}) | HP: {self.hp} | Força: {self.strenght}, "
                f"Velocidade: {self.speed}, Magia: {self.magic}\n"
                f"Efeitos Ativos: {', '.join(self._effects) if self._effects else 'Nenhum efeito ativo.'}")

    def __repr__(self):
        return (f"Monster(name='{self.name}', monster_type='{self.monster_type}', hp={self.hp}, "
                f"strenght={self.strenght}, speed={self.speed}, magic={self.magic}, "
                f"effects={self._effects})")
