class Cancion:
  """ 
  La clase *Cancion* representa una canción con un título y un autor. 
  Que permite obtener y modificar estos valores mediante métodos específicos.
  """
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor


