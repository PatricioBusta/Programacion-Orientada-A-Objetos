# Clase base
class Vehiculo:
    
    def __init__(self, marca, modelo):
        #Inicializa un vehículo con una marca y un modelo.
        
        self.marca = marca
        self.modelo = modelo

    def detalles(self):
        #Devuelve una descripción básica del vehículo.
        
        return f"{self.marca} {self.modelo}"

# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    #Agrega el atributo 'puertas' para describir un Auto.

    def __init__(self, marca, modelo, puertas):
        #Inicializa un Auto con una marca, modelo y número de puertas.
    
        super().__init__(marca, modelo)
        self.puertas = puertas

    def detalles(self):
        #Devuelve una descripción extendida del Auto, incluyendo el número de puertas.

        return f"{super().detalles()}, {self.puertas} puertas"

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    
    def __init__(self, marca, modelo, cilindraje):
        #Inicializa una moto con una marca, modelo y cilindraje.
        
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def detalles(self):
        #Devuelve una descripción extendida de la moto, incluyendo el cilindraje.

        return f"{super().detalles()}, {self.cilindraje} cc"

# Uso de herencia
Auto = Auto("Toyota", "Corolla", 4)  # Crear un Auto con 4 puertas
moto = Moto("Honda", "CBR", 600)  # Crear una moto con 600 cc

print(Auto.detalles())  # Imprime detalles del Auto
print(moto.detalles())  # Imprime detalles de la moto
