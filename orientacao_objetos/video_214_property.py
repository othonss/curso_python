class Caneta:
    def __init__(self, cor):
        #Convenção para dizer que é privado ou protegido
        self._cor = cor
        self._cor_tampa = None

    def get_cor(self):
        return self._cor

    #Tanto o get_cor quanto o property são equivalente neste caso
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):  
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
   

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor)
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Preta'
print(caneta.cor)
print(caneta.cor_tampa)
