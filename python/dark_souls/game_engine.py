from jogadores import Cavaleiro
from inimigos import MortoVivo, Chefe
from itens import (
    EfeitoCura,
    EfeitoBuffDano,
    EfeitoBuffDefesa,
    EfeitoRemoverVeneno,
    Pocao,
    Arma
)
from npcs import Ferreiro


class GameEngine:
    def __init__(self):
        self.jogador = Cavaleiro("Artorias")
        self.boss = Chefe("Gwyn")
        self.undead = MortoVivo("Hollow Soldier")
        self.ferreiro = Ferreiro("Andre")

        # Criando itens
        espada = Arma("Espada Longa", dano=25, resistencia=80)
        pocao_vida = Pocao("Poção de Vida", efeitos=[
            EfeitoCura(50)
        ])
        pocao_furia = Pocao("Poção de Fúria", efeitos=[
            EfeitoBuffDano(10)
        ])
        pocao_pedra = Pocao("Poção de Pedra", efeitos=[
            EfeitoBuffDefesa(15)
        ])
        antidoto = Pocao("Antídoto", efeitos=[
            EfeitoRemoverVeneno()
        ])

        # Adicionando itens ao inventário
        self.jogador.adicionar_item(espada)
        self.jogador.adicionar_item(pocao_vida)
        self.jogador.adicionar_item(pocao_furia)
        self.jogador.adicionar_item(pocao_pedra)
        self.jogador.adicionar_item(antidoto)

        # Equipando arma inicial
        self.jogador.equipar_arma(espada)

    def menu(self):
        while True:
            print("\n=== Dark Souls RPG ===")
            print(f"Vida do jogador: {self.jogador.vida}")
            print("1 - Atacar Undead")
            print("2 - Atacar Boss")
            print("3 - Usar Item")
            print("4 - Falar com Ferreiro")
            print("5 - Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.combate(self.undead)

            elif escolha == '2':
                self.combate(self.boss)

            elif escolha == '3':
                self.usar_item()

            elif escolha == '4':
                self.ferreiro.falar()

            elif escolha == '5':
                print("Saindo do jogo...")
                break

            else:
                print("Escolha inválida!")

    def combate(self, inimigo):
        if not inimigo.esta_vivo():
            print(f"{inimigo.nome} já foi derrotado.")
            return

        dano = self.jogador.atacar()
        inimigo.defender(dano)

        if inimigo.esta_vivo():
            dano_recebido = inimigo.atacar()
            self.jogador.defender(dano_recebido)
        else:
            print(f"{inimigo.nome} foi derrotado!")

    def usar_item(self):
        if not self.jogador.inventario:
            print("Inventário vazio.")
            return

        print("\n=== Inventário ===")
        for idx, item in enumerate(self.jogador.inventario):
            print(f"{idx + 1} - {item.nome} ({item.tipo})")

        escolha = input("Escolha o número do item para usar ou (C)ancelar: ")

        if escolha.lower() == 'c':
            return

        try:
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(self.jogador.inventario):
                item = self.jogador.inventario[escolha_idx]
                self.jogador.usar_item(item)
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida.")
