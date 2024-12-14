# Clase base
class Animal:

    def hacer_sonido(self):
        #Método para emitir sonidos específicos.

        pass

# Clase Perro implementa el método 'hacer_sonido'
class Perro(Animal):

    def hacer_sonido(self):
        return "Guau"

# Clase Gato implementa el método 'hacer_sonido'
class Gato(Animal):

    def hacer_sonido(self):
        return "Miau"

# Clase Vaca implementa el método 'hacer_sonido'
class Vaca(Animal):

    def hacer_sonido(self):
        return "Muu"

# Función que usa polimorfismo
def imprimir_sonido(animal):
    #Imprime el sonido dependiendo del animal

    print(animal.hacer_sonido())

# Uso de polimorfismo
animales = [Perro(), Gato(), Vaca()]  # Lista de diferentes animales
for animal in animales:
    imprimir_sonido(animal)  # Llama al método 'hacer_sonido' según el tipo de animal
