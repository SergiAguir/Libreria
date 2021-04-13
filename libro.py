class Libro:
    def __init__(self,isbn,titulo,autor,paginas):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.valoracion=-1

    def getISBN(self):
        return self.isbn

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getPaginas(self):
        return self.paginas

    def getValoracion(self):
        return self.valoracion

    def setISBN(self,isbn):
        self.isbn = isbn

    def setTitulo(self,titulo):
        self.titulo = titulo

    def setAutor(self,autor):
        self.autor = autor

    def setPaginas(self,paginas):
        self.paginas = paginas

    def setValoracion(self,valoracion):
        self.valoracion = valoracion