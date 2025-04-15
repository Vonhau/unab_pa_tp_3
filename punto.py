class Punto():
    """
    Entre el parentesis se puede poner "Object", que es una forma de decir que
    esta clase Punto hereda todo de la super clase antes nombrada que viene con
    Python predefinida.
    NO es necesaria.
    """

    cont = 0 # Atributo de CLASE o Estatico
    def __init__ (self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return f"X: {self.get_x()}\nY: {self.get_y()}"
    
class PuntoIdentidad(Punto):
    """
    Hereda de la clase Punto, es para generar puntos con mismo X e Y.
    """
    def __init__(self, x):
        super().__init__(x, x)

def main():
    p1 = Punto(1, 2)
    p2 = PuntoIdentidad(2)
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()