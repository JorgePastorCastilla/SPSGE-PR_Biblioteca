from Biblioteca import Biblioteca
from model.Obra import Obra
from model.Publicacion import Publicacion
from model.Volum import Volum

input = ""
biblioteca = Biblioteca(10)
publicaciondef = Publicacion("ref1", "titulo")
biblioteca.publicaciones.append(publicaciondef)

def separador():
    print("-------------------------------")

def ask_options():
    print("1. Mostrar la capacitat de la biblioteca.")
    print("2. Mostrar el nombre d'elements que hi ha en la biblioteca")
    print("3. Afegir una publicacio a la biblioteca.")
    print("4. Mostrar una publicacio a partir de la seva referencia.")
    print("5. Visualitzar el contingut de la biblioteca.")
    print("6. Salir de la aplicacion")
    separador()
    global input
    input = str( raw_input("Elige una opcion: \n") )
    separador()
def ask_create_options():
    print("Que quieres Crear?")
    print("1. Publicacion.")
    print("2. Obra")
    print("3. Volum.")
    print("4. Revista.")
    createInput = str( raw_input("Elige una opcion: \n"))
    separador()
def create_Publicacion():


while(not(input.__eq__("6"))):
    # print input
    # print "6"
    ask_options()
    if(input == "1"):
        print ("la capacitat de la biblioteca es: " + str(biblioteca.get_capacitatMax()) )
        separador()
    elif(input == "2"):
        print("la cantidad de publicaciones en la biblioteca es: " + str(biblioteca.get_cantidad()) )
        separador()
    elif(input == "3"):
        #aqui van lo de anadir publicaciones
        publicacion = Volum("20","paco","200","ref2","titulo")
        #pregunta = str( raw_input("Cual es la referencia? ") )
        biblioteca.add_publicacion(publicacion)
    elif(input == "4"):
        pregunta = str( raw_input("Cual es la referencia? \n") )
        biblioteca.find_publicacion(pregunta).visualitzar()
        separador()
    elif(input == "5"):
        #print (biblioteca.get_publicaciones())
        biblioteca.get_publicaciones()
        separador()
    elif(input == "6"):
        break
    elif(input == ""):
        print("Tienes que introducir una opcion")
        separador()
        ask_options()
    else:
        print("Esto no es una opcion correcta")
        separador()
        ask_options()

print("hasta luego champion")


