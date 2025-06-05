from .jogador import Jogador

class Cavaleiro(Jogador):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)

    def atacar(self):
        pass
    
    def defender(self):
        pass

if __name__ == '__main__':
    p1 = Cavaleiro('jhon Doe', 50)

    print(p1.saude)