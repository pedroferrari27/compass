class Aviao:
    def __init__(self, modelo, velocidade_maxima,capacidade,cor):
        self._modelo = modelo
        self._velocidade_maxima = velocidade_maxima
        self._capacidade = capacidade
        self.cor = "azul"
        
        
#a adicionar: leitura automatica da entrada
        
# regex : modelo [A-Za-z]+[0-9]+: velocidade máxima [0-9]+ km/h: capacidade para [0-9]+ passageiros: Cor [A-Za-z]+ 
# regex : modelo(\s([A-Za-z]+\s)+)[A-Za-z]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?: velocidade máxima de [0-9]+ Km/h: capacidade para [0-9]+ passageiros: Cor [A-Za-z]+


#adicionando dados da entrada em uma lista     
lista = []
lista.append(Aviao("BOIENG456",1500,400,"Azul"))
lista.append(Aviao("Praetor 600",863,14,"Azul"))
lista.append(Aviao("An-2",258,12,"Azul"))

#imprimindo de acordo com a lista
for aviao in lista:
    print("O avião de modelo " + aviao._modelo + " possui uma velocidade máxima de " + str(aviao._velocidade_maxima) + ", capacidade para " + str(aviao._capacidade) + " passageiros e é da cor " + aviao.cor + ".")

