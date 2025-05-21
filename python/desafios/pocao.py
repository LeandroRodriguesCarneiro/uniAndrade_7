class Personagem:
    def __init__(self, nome: str):
        self.nome = nome
        self.saude = 10
        self.vivo = True
    
    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f'{self.nome} já está morto e não pode usar poções.')
            return
        
        if isinstance(pocao, PocaoRoxa):
            self.saude += pocao.potencia
            if self.saude <= 0:
                self.saude = 0
                self.vivo = False
                print(f'{self.nome} foi envenenado e morreu.')
            else:
                print(f'{self.nome} usou a poção: {pocao.tipo}')
                print(f'{self.nome} levou {pocao.potencia} de dano tem: {self.saude} pontos de vida')
        else:
            temp = self.saude + pocao.potencia
            if temp > 100:
                self.saude = 100
                print(f'Personagem {self.nome} já está com {self.saude} pontos de vidav')
                return
            
            self.saude = temp
            print(f'{self.nome} usou a poção: {pocao.tipo}')
            print(f'{self.nome} ganhou {pocao.potencia} de vida tem: {self.saude} pontos de vida')

class PocaoVerde:
    def __init__(self, tipo:str, potencia:int):
        self.tipo = tipo
        self.potencia = potencia

class PocaoRoxa:
    def __init__(self, tipo:str, potencia:int):
        self.tipo = tipo
        self.potencia = potencia * (-1)

p1 = Personagem("Kratos")
pocao_verde = PocaoVerde("cura", 40)
pocao_roxa = PocaoRoxa("veneno", 40)

p1.usar_pocao(pocao_verde)
p1.usar_pocao(pocao_verde)
p1.usar_pocao(pocao_verde)
p1.usar_pocao(pocao_verde)
p1.usar_pocao(pocao_verde)
# p1.usar_pocao(pocao_verde)
# p1.usar_pocao(pocao_verde)
p1.usar_pocao(pocao_roxa)
p1.usar_pocao(pocao_roxa)
p1.usar_pocao(pocao_roxa)
p1.usar_pocao(pocao_roxa)
# p1.usar_pocao(pocao_roxa)
# p1.usar_pocao(pocao_roxa)
# p1.usar_pocao(pocao_roxa)
