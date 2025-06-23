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


# 🔥 Criar jogador e inimigos
jogador = Cavaleiro("Artorias")
boss = Chefe("Gwyn")
undead = MortoVivo("Hollow Soldier")

# 🔥 Criar arma e poções
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

# 🔥 Equipar arma e adicionar itens
jogador.equipar_arma(espada)
jogador.adicionar_item(pocao_vida)
jogador.adicionar_item(pocao_furia)
jogador.adicionar_item(pocao_pedra)
jogador.adicionar_item(antidoto)


print("\n=== TESTE DE COMBATE CONTRA UNDEAD ===")
dano = jogador.atacar()
undead.defender(dano)

if undead.esta_vivo():
    dano_inimigo = undead.atacar()
    jogador.defender(dano_inimigo)
else:
    print(f"{undead.nome} foi derrotado!")

print("\n=== TESTE USANDO POÇÃO DE VIDA ===")
jogador.usar_item(pocao_vida)

print("\n=== TESTE USANDO POÇÃO DE FÚRIA (Buff de Dano) ===")
jogador.usar_item(pocao_furia)

print("\n=== TESTE USANDO POÇÃO DE PEDRA (Buff de Defesa) ===")
jogador.usar_item(pocao_pedra)

print("\n=== TESTE DE COMBATE CONTRA BOSS COM BUFFS ===")
dano = jogador.atacar()
boss.defender(dano)

if boss.esta_vivo():
    dano_inimigo = boss.atacar()
    jogador.defender(dano_inimigo)
else:
    print(f"{boss.nome} foi derrotado!")

print("\n=== TESTE USANDO ANTÍDOTO (Sem estar envenenado) ===")
jogador.usar_item(antidoto)

print("\n=== STATUS FINAL ===")
print(f"Vida do Jogador: {jogador.vida}")
print(f"Buff de Dano: {getattr(jogador, 'buff_dano', 0)}")
print(f"Buff de Defesa: {getattr(jogador, 'buff_defesa', 0)}")
