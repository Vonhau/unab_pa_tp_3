# Ejercicio 5:
# Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre 
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar 
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes 
# servicios: getters y setters, método para leer la información y método para mostrar la 
# información. 

# Este último método mostrará la información del libro con este formato: 
# Título: Introduction to Java Programming 3a. edición 
# Autor: Liang, Y. Daniel 
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA)
# viernes 16 de noviembre de 2001 
# 784 páginas

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre_completo(self):
        return f"{self.nombre},{self.apellido}"
    
class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion
    

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_autor(self):
        return self.autor
    
    def set_autor(self,nuevo_autor):
        self.autor = nuevo_autor

    def get_ISBN(self):
        return self.ISBN
    
    def set_ISBN(self, nuevo_ISBN):
        self.ISBN = nuevo_ISBN

    def get_paginas(self):
        return self.paginas
    
    def set_paginas(self,cantidad_pag):
        self.paginas = cantidad_pag

    def get_edicion(self):
        return self.edicion
    
    def set_edicion(self,nueva_edicion):
        self.edicion = nueva_edicion
        
    def get_editorial(self):
        return self.editorial
    
    def set_editorial(self,nueva_editorial):
        self.editorial = nueva_editorial

    def get_lugar(self):
        return self.lugar
    
    def set_lugar(self,nuevo_lugar):
        self.lugar = nuevo_lugar

    def get_fecha(self):
        return self.fecha_edicion
    
    def set_fecha(self,nueva_fecha):
        self.fecha_edicion = nueva_fecha
    
    def __str__(self):
        return f"Titulo: {self.titulo}\n Autor: {self.autor.get_nombre_completo()}\n ISBN: {self.ISBN}\n {self.editorial} {self.lugar}\n {self.fecha_edicion}\n {self.paginas} Paginas"

autor1 = Persona("Carlos", "Allende")

libro1 = Libro(
    titulo="La casa de los espíritus",
    autor=autor1,
    ISBN="978-84-376-0494-7",
    edicion="1a. edición",
    editorial="Plaza & Janés",
    lugar="Barcelona",
    fecha_edicion="1982",
    paginas=490
)

print(libro1)