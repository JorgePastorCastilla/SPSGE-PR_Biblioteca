from model.Obra import Obra


class Volum(Obra):
    def __init__(self,nro,autor,nrePags,referencia,titol):
        Obra.__init__(self,autor,nrePags,referencia,titol)
        self.nro = nro

    def get_nro(self):
        return self.nro
    def set_nro(self,nro):
        self.nro = nro

    def visualitzar(self):
        Obra.visualitzar(self)
        print("nro: "+self.nro)