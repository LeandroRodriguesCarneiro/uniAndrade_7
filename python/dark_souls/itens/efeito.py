from abc import ABC, abstractmethod

class Efeito(ABC):
    @abstractmethod
    def aplicar(self, alvo):
        pass


class EfeitoCura(Efeito):
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def aplicar(self, alvo):
        alvo.vida += self.quantidade
        print(f"{alvo.nome} recuperou {self.quantidade} de vida. Vida atual: {alvo.vida}")


class EfeitoBuffDano(Efeito):
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def aplicar(self, alvo):
        alvo.buff_dano = getattr(alvo, 'buff_dano', 0) + self.quantidade
        print(f"{alvo.nome} aumentou o dano em +{self.quantidade} temporariamente.")


class EfeitoBuffDefesa(Efeito):
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def aplicar(self, alvo):
        alvo.buff_defesa = getattr(alvo, 'buff_defesa', 0) + self.quantidade
        print(f"{alvo.nome} aumentou a defesa em +{self.quantidade} temporariamente.")


class EfeitoRemoverVeneno(Efeito):
    def aplicar(self, alvo):
        if getattr(alvo, 'envenenado', False):
            alvo.envenenado = False
            print(f"{alvo.nome} foi curado do veneno.")
        else:
            print(f"{alvo.nome} não estava envenenado.")
