from .entity import Entity

class PersonagemGame(Entity):
    def __init__(self, name: str, hp: int, strenght: int, speed: int, magic: int, level: int = 1, experience: int = 0):
        super().__init__(name, hp, strenght, speed, magic)
        self._level = level  # Nível inicial do personagem
        self._experience = experience  # Experiência inicial do personagem
        self._max_hp = hp  # HP máximo do personagem, útil para cálculo de regeneração
        self._effects = []  # Lista de efeitos ativos, como 'lento'
        self._inventory = []  # Inventário do personagem

    # Getters e setters para level e experience
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    def add_item(self, item):
        """Adiciona um item ao inventário. Se exceder a força, aplica penalidade de lentidão."""
        total = self.total_weight() + item.weight

        self._inventory.append(item)
        print(f"{item.name} foi adicionado ao inventário de {self.name}.")

        if total > self.strenght:
            if "lento" not in self._effects:
                self._effects.append("lento")
                self._speed = max(1, self._speed - 2)  # Reduz a velocidade, mínimo de 1
                print(f"{self.name} está sobrecarregado! Velocidade reduzida para {self._speed}. Efeito 'lento' aplicado.")

    def drop_item(self, item):
        """Remove um item do inventário. Se o item removido resultar em o personagem deixar de estar sobrecarregado, remove o efeito 'lento'."""
        if item in self._inventory:
            self._inventory.remove(item)
            print(f"{item.name} foi removido do inventário de {self.name}.")

            # Verifica se o peso total após a remoção ainda excede a força
            total_weight = self.total_weight()

            if total_weight <= self.strenght:
                # Se o peso total ficou abaixo ou igual à força, remove o efeito 'lento' e restaura a velocidade
                if "lento" in self._effects:
                    self._effects.remove("lento")
                    self._speed += 2  # Restaura a velocidade
                    print(f"{self.name} não está mais sobrecarregado. Velocidade restaurada para {self._speed}.")
            else:
                print(f"{self.name} continua sobrecarregado, efeito 'lento' permanece.")
        else:
            print(f"{item.name} não está no inventário.")

    def total_weight(self):
        """Calcula o peso total dos itens no inventário."""
        return sum(item.weight for item in self._inventory)

    # Método para ganhar experiência e evoluir de nível
    def gain_experience(self, amount: int):
        """Aumenta a experiência e verifica se o personagem evolui de nível."""
        self._experience += amount
        print(f"{self.name} ganhou {amount} de experiência!")

        # Evolução: a cada 100 pontos de experiência, o personagem sobe de nível
        while self._experience >= 100:
            self._experience -= 100
            self.level_up()

    def level_up(self):
        """Aumenta o nível do personagem e melhora suas características."""
        self._level += 1
        self._strenght += 2  # Aumento de força por nível
        self._speed += 1  # Aumento de velocidade por nível
        self._magic += 1  # Aumento de magia por nível
        self._max_hp += 10  # Aumento de HP máximo por nível
        self._hp = self._max_hp  # Recupera o HP após a evolução

        print(f"{self.name} subiu para o nível {self._level}!")
        print(f"Novos atributos: Força: {self._strenght}, Velocidade: {self._speed}, Magia: {self._magic}, HP: {self._hp}")

    # Método de cura do personagem
    def heal(self, amount: int):
        """Cura o personagem, mas não ultrapassa o HP máximo."""
        self._hp = min(self._hp + amount, self._max_hp)
        print(f"{self.name} foi curado em {amount}. HP atual: {self._hp}/{self._max_hp}.")

    # Método de ataque especial (magia)
    def cast_spell(self, target: Entity, spell_name: str, damage: int):
        """O personagem pode lançar um feitiço em um alvo."""
        if self._magic >= 5:  # Verifica se o personagem tem mana suficiente
            self._magic -= 5  # Consome mana
            target.take_damage(damage)  # Aplica o dano no alvo
            print(f"{self.name} lançou {spell_name} causando {damage} de dano em {target.name}. Mana restante: {self._magic}.")
        else:
            print(f"{self.name} não tem mana suficiente para lançar {spell_name}. Mana atual: {self._magic}.")

    # Exibição personalizada do personagem
    def __str__(self):
        return (f"{self.name} | Nível: {self.level} | HP: {self.hp}/{self._max_hp} | Força: {self.strenght}, "
                f"Velocidade: {self.speed}, Magia: {self.magic}\n"
                f"Efeitos Ativos: {', '.join(self._effects) if self._effects else 'Nenhum efeito ativo.'}")

    def __repr__(self):
        return (f"PersonagemGame(name='{self.name}', level={self.level}, experience={self.experience}, "
                f"hp={self.hp}, max_hp={self._max_hp}, strenght={self.strenght}, speed={self.speed}, "
                f"magic={self.magic}, effects={self._effects})")
