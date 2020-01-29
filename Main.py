from Biblioteca import Biblioteca
from model.Publicacion import Publicacion
input = ""
biblioteca = Biblioteca(10)
publicaciondef = Publicacion("ref1", "titulo")
biblioteca.publicaciones.append(publicaciondef)

def ask_options():
    print("1. Mostrar la capacitat de la biblioteca.")
    print("2. Mostrar el nombre d'elements que hi ha en la biblioteca")
    print("3. Afegir una publicacio a la biblioteca.")
    print("4. Mostrar una publicacio a partir de la seva referencia.")
    print("5. Visualitzar el contingut de la biblioteca.")
    print("6. Salir de la aplicacion")
    global input
    input = str( raw_input("Elige una opcion ") )
    if(input == ""):
        print("Tienes que introducir una opcion")
        #ask_options()

while(not(input.__eq__("6"))):
    # print input
    # print "6"
    ask_options()
    if(input == "1"):
        print ("la capacitat de la biblioteca es: " + str(biblioteca.get_capacitatMax()) )
    if(input == "2"):
        print("la cantidad de publicaciones en la biblioteca es: " + str(biblioteca.get_cantidad()) )
    if(input == "3"):
        #aqui van lo de anadir publicaciones
        publicacion = Publicacion("ref2","titulo")
        #pregunta = str( raw_input("Cual es la referencia? ") )
        biblioteca.add_publicacion(publicacion)
    if(input == "4"):
        pregunta = str( raw_input("Cual es la referencia? ") )
        biblioteca.find_publicacion(pregunta).visualitzar()
    if(input == "5"):
        #print (biblioteca.get_publicaciones())
        biblioteca.get_publicaciones()

print("hasta luego champion")


