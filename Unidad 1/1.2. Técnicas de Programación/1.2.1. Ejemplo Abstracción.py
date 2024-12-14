from abc import ABC, abstractmethod

# Clase abstracta
class Figura(ABC):

    def calcular_area(self):
        #Calcula el área de la figura
        pass

    def calcular_perimetro(self):
         #Calcula el perímetro de la figura
        pass

# Subclase
class Rectangulo(Figura):
    #Clase 'Rectangulo' que hereda de 'Forma'.

    def __init__(self, ancho, alto):
        #Inicializa un rectángulo con las dimensiones especificadas.

        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        # Calcula el área del rectángulo
        return self.ancho * self.alto

    def calcular_perimetro(self):
        # Calcula el perímetro del rectángulo
        return 2 * (self.ancho + self.alto)

# Uso de abstracción
rectangulo = Rectangulo(5, 3)  # Crear un rectángulo con ancho 5 y alto 3
print("Área del rectángulo:", rectangulo.calcular_area())  # Muestra el área
print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())  # Muestra el perímetro
