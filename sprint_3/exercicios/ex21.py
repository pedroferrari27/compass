class Passaro:
    def __init__(self):
        self.voando = True
    def voar(self):
        if self.voando == True:
            print("Voando...")
    def emitir_som(self):
        print("Passaro emitindo som...")
        print("brr,brr")
    def nomear(self):
        print("Passaro")
        


class Pato(Passaro):
    def nomear(self):
        print("Pato")
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")
  
        
class Pardal(Passaro):
    def nomear(self):
        print("Pardal")
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")


#criando instancias dos objetos

a = Pato()
b = Pardal()



a.nomear()
a.voar()
a.emitir_som()

b.nomear()
b.voar()
b.emitir_som()