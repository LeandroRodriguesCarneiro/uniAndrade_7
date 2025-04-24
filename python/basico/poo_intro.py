class Player():
    def __init__(self, nome: str, arma:str):
        self.__nome = nome
        self.__arma = arma

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def arma(self):
        return self.__arma
    
    @arma.setter
    def arma(self, arma):
        self.__arma = arma

    def __repr__(self):
        return f"Player(name = {self.nome}, arma = {self.arma})"

kratos: Player = Player('Kratos', 'Leviata')
print(kratos.__repr__())

print(kratos.nome)
kratos.nome = 'Kratos2'
print(kratos.__repr__())

atreus: Player = Player('Atreus', 'Arco')
print(atreus.__repr__())
