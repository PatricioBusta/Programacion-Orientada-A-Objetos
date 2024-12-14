import Ejemplo_Programación_Tradicional

# Programación Orientada a Objetos

class ClimaSemanal:
    #Clase para manejar el clima semanal.
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        #Método para ingresar temperaturas diarias.
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        #Método para calcular el promedio semanal
        if not self.temperaturas:
            raise ValueError("No hay temperaturas ingresadas.")
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    #Programa principal: Programación Orientada a Objetos.
    print("Programación Orientada a Objetos: Promedio Semanal del Clima")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Menú para elegir cuál programa ejecutar
if __name__ == "__main__":
    print("Seleccione la implementación a ejecutar:")
    print("1. Programación Tradicional")
    print("2. Programación Orientada a Objetos")
    opcion = input("Ingrese el número de su opción: ")

    if opcion == "1":
       Ejemplo_Programación_Tradicional.main_tradicional()
    elif opcion == "2":
        main_poo()
    else:
        print("Opción no válida. Intente de nuevo.")
