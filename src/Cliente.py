import Ordem

class Cliente:
    def __init__(self, CPF, ordens):
        self.CPF = CPF
        self.ordens = ordens

    def getOrdens(self):
        return self.ordens
