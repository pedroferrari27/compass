class Calculo():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    @property 
    def x(self):
        """propiedade x"""
        return self._x
    
    
    @x.setter
    def x(self,x):
        #print("gravndo x ")
        self._x = x
   
    @x.getter
    def x(self):
        #print("recebendo x ")
        return self._x
    
    
    
    @property 
    def y(self):
        """propiedade y"""
        return self._y
    
    @y.setter
    def y(self,y):
        #print("gravndo y ")
        self._y = y
  
    @y.getter
    def y(self):
        #print("recebendo y ")
        return self._y
    
    def soma(self):
        print("Somando: "+str(self.x)+"+"+str(self.y)+" = " +str(self.x + self.y))
    def subtracao(self):
        print("Somando: "+str(self.x)+"-"+str(self.y)+" = " +str((self.x - self.y )))

#testasndo classe

x = 4
y = 5

        
calc = Calculo(x, y)

calc.soma()

calc.subtracao()








    
        