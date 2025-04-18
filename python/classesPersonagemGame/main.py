from src import PersonagemGame, Monster, Potion, Weapon 

def main():
    # Criando o personagem jogável
    player = PersonagemGame(name="Herói", hp=80, strenght=15, speed=10, magic=5)
    player2 = PersonagemGame(name="Ajudante", hp=80, strenght=15, speed=10, magic=5)
    print(f"{player.name} foi criado com HP: {player.hp}")
    print(player.__repr__())
    print(player2.__repr__())

    # Criando um monstro
    goblin = Monster(name="Goblin", hp=50, strenght=8, speed=6, magic=2, monster_type="goblin")

    # Criando arma
    sword = Weapon(
        name="Espada Longa",
        weight=5,
        effect="corte",
        description="Uma espada afiada e resistente.",
        value=150,
        damage_type="corte",
        damage_value=25
    )
    player.add_item(sword)

    # Criando poções
    healing_potion = Potion(
        name="Poção de Cura",
        weight=1,
        effect="cura",
        description="Restaura 30 de HP.",
        value=50,
        effect_amount=30
    )

    speed_potion = Potion(
        name="Poção de Velocidade",
        weight=1,
        effect="velocidade",
        description="Aumenta a velocidade temporariamente.",
        value=75,
        effect_amount=10,
    )

    # Adicionando poções ao inventário
    player.add_item(healing_potion)
    player.add_item(speed_potion)

    print(f"\nInventário de {player.name}:\n{player.show_inventory()}")

    # Usando arma
    sword.use(goblin)
    print(f"\nHP do {goblin.name} após ataque: {goblin.hp}")

    # Usando poção de cura
    print(f"\nHP de {player.name} antes da cura: {player.hp}")
    healing_potion.use(player)
    print(f"HP de {player.name} depois da cura: {player.hp}")

    # Usando poção de velocidade
    speed_potion.use(player)
    print(player.show_effects())

    # Usando poção de velocidade
    speed_potion.use(player)
    print(player.show_effects())

    # Combate até o goblin ser derrotado
    print(f"\nComeçando o combate entre {player.name} e {goblin.name}!")

    while goblin.is_alive():
        sword.use(goblin)
        print(f"{goblin.name} agora tem {goblin.hp} de HP.")
    
    print(f"\n{goblin.name} foi derrotado por {player.name}!")

if __name__ == "__main__":
    main()
