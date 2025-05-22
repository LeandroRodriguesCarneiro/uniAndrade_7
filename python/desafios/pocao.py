from abc import ABC, abstractmethod

class Pocao(ABC):
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo
        self.potencia = potencia

    @abstractmethod
    def obter_efeito(self) -> int:
        pass

class PocaoVerde(Pocao):
    def obter_efeito(self):
        return self.potencia  # cura (positivo)

class PocaoRoxa(Pocao):
    def obter_efeito(self):
        return -abs(self.potencia)  # dano (negativo)

class Personagem:
    def __init__(self, nome: str, nome_armadura, protecao):
        self.nome = nome
        self._saude = 10
        self._vivo = True
        self.inventario = Inventario()
        self.armadura = Armadura(nome_armadura, protecao)

    @property
    def saude(self):
        return self._saude

    @property
    def vivo(self):
        return self._vivo

    def usar_pocao(self, pocao: Pocao):
        if not self.vivo:
            print(f'{self.nome} já está morto e não pode usar poções.')
            return

        efeito = pocao.obter_efeito()

        if efeito > 0:
            self._aumentar_vida(efeito)
            print(f'{self.nome} usou a poção: {pocao.tipo}')
            print(f'{self.nome} ganhou {efeito} de vida. Vida atual: {self.saude}')
        elif efeito < 0:
            self._reduzir_vida(-efeito)
            if self.vivo:
                print(f'{self.nome} usou a poção: {pocao.tipo}')
                print(f'{self.nome} levou {-efeito} de dano. Vida atual: {self.saude}')
            else:
                print(f'{self.nome} foi envenenado e morreu.')

    def _aumentar_vida(self, quantidade):
        self._saude = min(self._saude + quantidade, 100)

    def _reduzir_vida(self, quantidade):
        self._saude -= quantidade
        if self._saude <= 0:
            self._saude = 0
            self._vivo = False

class Item:
    def __init__(self, tipo, efeito):
        self.tipo = tipo
        self.efeito = efeito

class Inventario:
    def __init__(self):
        self.itens = []

    def add_item(self, item):
        if not item:
            print('Escolha um item para inserir')
        self.itens.append(item)

    def drop_item(self, item):
        self.itens.remove(item)

class Armadura:
    def __init__(self, nome, protecao):
        self.nome = nome
        self.protecao = protecao

    def blindar(self):
        print('sua protecao aumentou')

p1 = Personagem("Kratos", 'diamante', 75)
pocoes = [
    PocaoVerde("Poção de Cura", 30),
    PocaoVerde("Poção de Cura", 40),
    PocaoRoxa("Poção de Veneno", 20),
    PocaoRoxa("Poção de Veneno", 50)
]

for pocao in pocoes:
    p1.usar_pocao(pocao)
