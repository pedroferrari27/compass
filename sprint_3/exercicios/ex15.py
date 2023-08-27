class Lampada:
    def  __init__(self):
        self.ligada = True
    def liga(self):
        self.ligada = True
    def desliga(self):
        self.ligada = False
    def esta_ligada(self):
        if self.ligada == True:
            return True
        else:
            return False

lamp = Lampada()

lamp.liga()

print("A lâmpada está ligada? ",lamp.esta_ligada())

lamp.desliga()

print("A lâmpada está ligada? ",lamp.esta_ligada())