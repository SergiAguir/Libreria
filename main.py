from libro import Libro
from controlador import Controlador

con = Controlador()

while True:
    print("---------- COLECCION DE LIBROS ------------")
    print("El numero de libros registrados es ",con.getNumLibros())
    print("1.- Anyadir libros")
    print("2.- Eliminar libros")
    print("3.- Listar libros")
    print("4.- Libro con menor valoracion")
    print("5.- Libro con mayor valoracion")
    print("6.- Salir")

    op = int(input("Selecciona una opcion: "))

    if op == 1:
        while True:
            try:
                isbn = int(input("Introduce el ISBN: "))
                if isbn == 0:
                    print("----------------------")
                    print("El ISBN no puede ser 0")
                    print("----------------------")
                else:
                    break
            except ValueError:
                print("--------------------")
                print("El ISBN no es valido")
                print("--------------------")
        
        while True:
            try:
                titulo = str(input("Introduce el titulo: "))
                if titulo == "":
                    print("----------------------------------")
                    print("El titulo no puede estar en blanco")
                    print("----------------------------------")
                else:
                    break
            except ValueError:
                print("----------------------")
                print("El titulo no es valido")
                print("----------------------")

        while True:
            try:
                autor = str(input("Introduce el autor: "))
                if autor == "":
                    print("---------------------------------")
                    print("El autor no puede estar en blanco")
                    print("---------------------------------")
                else:
                    break
            except ValueError:
                print("---------------------")
                print("El autor no es valido")
                print("---------------------")

        while True:
            try:
                paginas = int(input("Introduce el numero de paginas: "))
                if paginas <= 0:
                    print("---------------------------------------------")
                    print("El numero de paginas no puede ser menor que 0")
                    print("---------------------------------------------")
                else:
                    break
            except ValueError:
                print("---------------------------------")
                print("El numero de paginas no es valido")
                print("---------------------------------")

        while True:
            try:
                valoracion = int(input("Introduce la valoracion: "))
                if valoracion <0 or valoracion >10:
                    print("------------------------------------------")
                    print("La valoracion tiene que estar entre 0 y 10")
                    print("------------------------------------------")
                else:
                    break
            except ValueError:
                print("--------------------------")
                print("La valoracion no es valida")
                print("--------------------------")

        libro = Libro(isbn,titulo,autor,paginas)
        libro.setValoracion(valoracion)
        if con.anyadirLibro(libro):
            print("El libro ",libro.getISBN()," ha sido anyadido correctamente")
        else:
            print("El libro ya exsiste!!")

    if op == 2:
        while True:
            try:
                isbn = int(input("Introduce el ISBN: "))
                if isbn == 0:
                    print("----------------------")
                    print("El ISBN no puede ser 0")
                    print("----------------------")
                else:
                    break
            except ValueError:
                print("--------------------")
                print("El ISBN no es valido")
                print("--------------------")
        if con.eliminarLibro(isbn):
            print("El libro ",isbn," a sido eliminado correctamente")
        else:
            print("El libro no exisite!!")


    if op == 3:
        print("Listado de libros: \n",con.listarLibros())

    if op == 4:
        print("El libro con menor valoracion es: ")
        libro = con.minimaValoracion()
        print("ISBN: "+str(libro.getISBN()))
        print("Titulo: "+libro.getTitulo())
        print("Autor: "+libro.getAutor())
        print("Paginas: "+str(libro.getPaginas()))
        print("Valoracion: "+str(libro.getValoracion()))

    if op == 5:
        print("El libro con mayor valoracion es: ")
        libro = con.maximaValoracion()
        print("ISBN: "+str(libro.getISBN()))
        print("Titulo: "+libro.getTitulo())
        print("Autor: "+libro.getAutor())
        print("Paginas: "+str(libro.getPaginas()))
        print("Valoracion: "+str(libro.getValoracion()))


    if op == 6:
        print("Adios!!")
        break