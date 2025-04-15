from punto import Punto

class Linea(Punto):
    def __init__(self, PuntoA, PuntoB):
        self._punto_a = PuntoA
        self._punto_b = PuntoB
    
    def mueve_derecha(self, distancia):
        self._punto_a += distancia
        self._punto_b += distancia

    def get_punto_a(self):
        return self._punto_a
    
    def get_punto_b(self):
        return self._punto_b
    
    #def set_x(self, x):
    #    self._x = x

    #def set_y(self, y):
    #    self._y = y

    def __str__(self):
        return f"Punto A: {self.get_punto_a()}\nPunto B: {self.get_punto_b()}"

# Prueba

p1 = Punto(1, 2)
p2 = Punto(2, 1)
linea1 = Linea(p1, p2)

print(linea1)