class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        print('Get cor')
        return self.cor_tinta

    #Tanto o get_cor quanto o property são equivalente neste caso
    @property
    def cor(self):
        print('Property')
        return self.cor_tinta
   

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor)
