from Biblioteca import Biblioteca
from model.Obra import Obra
from model.Publicacion import Publicacion
from model.Revista import Revista
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
    if(createInput == "1"):
        create_Publicacion()
    elif(createInput == "2"):
        create_Obra()
    elif(createInput == "3"):
        create_Volum()
    elif(createInput == "4"):
        create_Revista()
    elif(input == ""):
        print("Tienes que introducir una opcion")
        separador()
        ask_create_options()
    else:
        print("Esto no es una opcion correcta")
        separador()
        ask_create_options()
def create_Publicacion():
    referencia = str(raw_input("Introduce la referencia: \n"))
    separador()
    titol = str(raw_input("Introduce el titulo: \n"))
    separador()
    biblioteca.add_publicacion(Publicacion(referencia=referencia,titol=titol))
def create_Obra():
    referencia = str(raw_input("Introduce la referencia: \n"))
    separador()
    titol = str(raw_input("Introduce el titulo: \n"))
    separador()
    autor = str(raw_input("Introduce el autor: \n"))
    separador()
    nrePags = str(raw_input("Introduce el numero de paginas: \n"))
    separador()
    biblioteca.add_publicacion(Obra(referencia=referencia,titol=titol,autor=autor,nrePags=nrePags))
def create_Volum():
    referencia = str(raw_input("Introduce la referencia: \n"))
    separador()
    titol = str(raw_input("Introduce el titulo: \n"))
    separador()
    autor = str(raw_input("Introduce el autor: \n"))
    separador()
    nrePags = str(raw_input("Introduce el numero de paginas: \n"))
    separador()
    nro = str(raw_input("Introduce el numero de publicaciones: \n"))
    separador()
    biblioteca.add_publicacion(Volum(referencia=referencia,titol=titol,autor=autor,nrePags=nrePags,nro=nro))
def create_Revista():
    referencia = str(raw_input("Introduce la referencia: \n"))
    separador()
    titol = str(raw_input("Introduce el titulo: \n"))
    separador()
    nro = str(raw_input("Introduce el numero de publicaciones: \n"))
    separador()
    any = str(raw_input("Introduce el anyo: \n"))
    separador()
    biblioteca.add_publicacion(Revista(referencia=referencia,titol=titol,any=any,nro=nro))


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
        # publicacion = Volum("20","paco","200","ref2","titulo")
        #pregunta = str( raw_input("Cual es la referencia? ") )
        # biblioteca.add_publicacion(publicacion)
        ask_create_options()
    elif(input == "4"):
        pregunta = str( raw_input("Cual es la referencia? \n") )
        separador()
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


