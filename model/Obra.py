from model.Publicacion import Publicacion


class Obra(Publicacion):
    def __init__(self,autor,nrePags,referencia,titol):
        Publicacion.__init__(self,referencia,titol)
        self.autor = autor
        self.nrePags = nrePags

    def get_autor(self):
        return self.autor
    def set_autor(self,autor):
        self.autor = autor

    def get_nrePags(self):
        return self.nrePags
    def set_nrePags(self,nrePags):
        self.nrePags = nrePags

    def visualitzar(self):
        Publicacion.visualitzar(self)
        print("autor: "+self.autor)
        print("nrePags: "+self.nrePags)
