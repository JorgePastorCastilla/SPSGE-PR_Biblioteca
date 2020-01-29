from model import *

class Biblioteca():

    #cantidad = 0
    publicaciones = []
    def __init__(self, capacitatMax):
        self.capacitatMax = capacitatMax

    def get_capacitatMax(self):
        return self.capacitatMax
    def get_cantidad(self):
        return self.cantidad

    def get_publicaciones(self):
        for publicacion in self.publicaciones:
            print(publicacion.titol)

    def add_publicacion(self,publicacion):
        if( ( publicacion in self.publicaciones ) and (self.publicaciones < self.capacitatMax)):
            print("Esta publicacion ya esta en la biblioteca")
        else:
            self.publicaciones.append(publicacion)

    def find_publicacion(self,referencia):
        for publicacion in self.publicaciones:
            if(publicacion.referencia == referencia):
                return publicacion
            else:
                print("No se ha encontrado ninguna publicacion con esta referencia({})".format(referencia))
    def get_cantidad(self):
        return len(self.publicaciones)
