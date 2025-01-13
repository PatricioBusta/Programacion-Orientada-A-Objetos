# Juego de Piedra, Papel o Tijera
# Este programa permite jugar Piedra, Papel o Tijera contra la computadora.
# Utiliza diferentes tipos de datos, identificadores descriptivos y comentarios explicativos.

import random

def obtener_opcion_usuario():
    # Solicita al usuario que elija entre piedra, papel o tijera.
    # Devuelve la opción elegida como una cadena.

    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    while True:
        try:
            opcion = int(input("Ingresa el número correspondiente a tu elección: "))
            if opcion in [1, 2, 3]:
                opciones = {1: "piedra", 2: "papel", 3: "tijera"}
                return opciones[opcion]
            else:
                print("Por favor, elige un número entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 1 y 3.")

def obtener_opcion_computadora():

    # Genera aleatoriamente la elección de la computadora entre piedra, papel y tijera.
    # Devuelve la opción elegida como una cadena.

    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):

    # Determina el ganador del juego según las opciones del usuario y de la computadora.
    # Devuelve una cadena indicando el resultado.

    if opcion_usuario == opcion_computadora:
        return "Empate. Ambos eligieron " + opcion_usuario + "."

    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }

    if reglas[opcion_usuario] == opcion_computadora:
        return f"Ganaste. {opcion_usuario.capitalize()} vence a {opcion_computadora}."
    else:
        return f"Perdiste. {opcion_computadora.capitalize()} vence a {opcion_usuario}."

def main():
    # Función principal que ejecuta el juego de Piedra, Papel o Tijera.

    print("Bienvenido al juego de Piedra, Papel o Tijera.")

    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()

        print(f"\nTu elección: {opcion_usuario.capitalize()}")
        print(f"Elección de la computadora: {opcion_computadora.capitalize()}")

        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(resultado)

        jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if jugar_de_nuevo != "s":
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
