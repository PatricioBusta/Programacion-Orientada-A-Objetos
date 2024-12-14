# Programación Tradicional

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():

    temperaturas = []
    # Recorre los días de la semana
    for i in range(7):
        # Ingresa de la temperatura diaria
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        # Agrega la temperatura ingresada a la lista
        temperaturas.append(temp)
    # Devuelve la lista de temperaturas
    return temperaturas

# Función para calcular el promedio semanal.
def calcular_promedio(temperaturas):

    # Promedio de temperatura
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main_tradicional():

    # Se muestra el título del programa
    print("Programación Tradicional: Promedio Semanal del Clima")
    # Llama a la función para obtener las temperaturas diarias
    temperaturas = ingresar_temperaturas()
    # Calcula el promedio semanal
    promedio = calcular_promedio(temperaturas)
    # Muestra el promedio con dos decimales y el símbolo de grados Celsius
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar la función principal
if __name__ == "__main__":
    main_tradicional()