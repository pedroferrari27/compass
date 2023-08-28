class Ordenadora ():
    def __init__(self,lista):
        self.listaBaguncada = lista
        
        @property 
        def listaBaguncada(self):
            """propiedade lista"""
            #print(self.listaBaguncada)
            return self._listaBaguncada
        
        
        @listaBaguncada.setter
        def listaBaguncada(self,lista):
            self._listaBaguncada = lista
        
        
    def ordenacaoCrescente(self):
        crescente = self.listaBaguncada
        crescente.sort()
        return crescente
    #pq alterar o crescente altera o atributo?
        
        
    def ordenacaoDecrescente(self):
        decrescente = self.listaBaguncada
        decrescente.sort(reverse=True)
        return decrescente

a = [3,4,2,1,5]
b = [9,7,6,8]

crescente = Ordenadora(a)
decrescente = Ordenadora(b)

#print(crescente.listaBaguncada)
print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())  

#print(crescente.listaBaguncada)
#print(decrescente.listaBaguncada)

#