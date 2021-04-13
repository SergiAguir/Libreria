from libro import Libro

class Controlador:
    def __init__(self):
        self.listaLibros = {}

    def getNumLibros(self):
        return len(self.listaLibros)

    def anyadirLibro(self,libro):
        if libro.getISBN() in self.listaLibros.keys():
            return False
        self.listaLibros[libro.getISBN()] = libro
        return True

    def eliminarLibro(self,isbn):
        if isbn not in self.listaLibros:
            return False
        else:
            del self.listaLibros[isbn]
            return True

    def listarLibros(self):
        result= ""
        for i in self.listaLibros.values():
            result +=  str(i.getISBN()) +" "+i.getTitulo()+" "+i.getAutor()+" "+str(i.getPaginas())+" "+str(i.getValoracion()) +"\n"
        return result

    def maximaValoracion(self):
        max=-1
        libro = None
        for i in self.listaLibros.values():
            if i.getValoracion() > max:
                max = i.getValoracion()
                libro = i
        return libro

    def minimaValoracion(self):
        min = 11
        libro = None
        for i in self.listaLibros.values():
            if i.getValoracion() < min:
                min = i.getValoracion()
                libro = i
        return libro
