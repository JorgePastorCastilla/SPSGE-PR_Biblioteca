
class Publicacion():
    def __init__(self,referencia,titol):
        self.referencia = referencia
        self.titol = titol

    def get_referencia(self):
        return self.referencia
    def set_referencia(self,referencia):
        self.referencia = referencia
    def get_titol(self):
        return self.titol
    def set_titol(self,titol):
        self.titol = titol

    def visualitzar(self):
        print("referencia: "+self.referencia)
        print("titol: "+self.titol)

    def __str__(self):
        return self.referencia
    def __eq__(self, other):
        return self.__str__() == other.__str__()