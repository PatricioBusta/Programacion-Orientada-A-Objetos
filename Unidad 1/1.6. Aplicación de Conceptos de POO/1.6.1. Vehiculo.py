# Clase base (Demostración de herencia y encapsulación)
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca  # Atributo privado (encapsulación)
        self.modelo = modelo
        self.anio = anio

    # Método para obtener la marca (getter para atributo privado)
    def obtener_marca(self):
        return self.__marca

    # Método para establecer la marca (setter para atributo privado)
    def establecer_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def mostrar_informacion(self):
        return f"Vehículo: {self.__marca} {self.modelo} ({self.anio})"

# Clase derivada (Herencia)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)  # Llamada al constructor de la clase base
        self.puertas = puertas

    # Método sobrescrito (Polimorfismo)
    def mostrar_informacion(self):
        return f"Coche: {self.obtener_marca()} {self.modelo} ({self.anio}), {self.puertas} puertas"

# Otra clase para demostrar polimorfismo con diferentes argumentos
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"Motocicleta: {self.obtener_marca()} {self.modelo} ({self.anio}), Tipo: {self.tipo}"

# Programa principal
if __name__ == "__main__":
    # Instancias
    vehiculo_generico = Vehiculo("Genérico", "ModeloX", 2020)
    coche = Coche("Toyota", "Corolla", 2021, 4)
    motocicleta = Motocicleta("Honda", "CBR", 2019, "Deportiva")

    print(vehiculo_generico.mostrar_informacion())
    print(coche.mostrar_informacion())
    print(motocicleta.mostrar_informacion())

    # Modificación de atributo privado usando setter y getter
    vehiculo_generico.establecer_marca("Actualizado")
    print(vehiculo_generico.mostrar_informacion())
