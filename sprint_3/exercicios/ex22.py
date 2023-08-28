class Pessoa():
    
    def __init__(self,id):
        self.id = id
        self.__nome = None
        
    @property
    def nome(self):
        """propiedade nome"""
        return self.__nome
    
    @nome.setter
    def nome(self,completo):
        self.__nome = completo
    @nome.deleter
    def nome(self):
        del self.__nome
        
        
pes = Pessoa(0)
pes.nome = 'Fulano De Tal'
print(pes.nome)
#print(vars(pes))
