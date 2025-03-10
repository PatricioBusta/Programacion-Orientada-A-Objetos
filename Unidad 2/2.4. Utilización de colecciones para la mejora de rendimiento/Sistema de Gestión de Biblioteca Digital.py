class Libro:
    def __init__(self, titulo, autor, genero, isbn):
        self.detalles = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"{self.detalles[0]} de {self.detalles[1]} (Género: {self.genero}, ISBN: {self.isbn})"


class Lector:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []  # Lista para almacenar libros prestados

    def __str__(self):
        return f"Lector: {self.nombre}, Cédula: {self.cedula}, Libros Prestados: {len(self.libros_prestados)}"


class BibliotecaDigital:
    def __init__(self):
        self.catalogo_libros = {}  # Diccionario {ISBN: Objeto Libro}
        self.lectores_registrados = {}  # Diccionario {Cédula: Objeto Lector}
        self.cedulas_registradas = set()  # Conjunto para cédulas únicas

    def agregar_libro(self, libro):
        if libro.isbn not in self.catalogo_libros:
            self.catalogo_libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya está en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.catalogo_libros:
            del self.catalogo_libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado del catálogo.")
        else:
            print("El libro no se encuentra en el catálogo.")

    def registrar_lector(self, lector):
        if lector.cedula not in self.cedulas_registradas:
            self.lectores_registrados[lector.cedula] = lector
            self.cedulas_registradas.add(lector.cedula)
            print(f"Lector registrado: {lector}")
        else:
            print("El lector ya está registrado.")

    def eliminar_lector(self, cedula):
        if cedula in self.lectores_registrados:
            del self.lectores_registrados[cedula]
            self.cedulas_registradas.remove(cedula)
            print(f"Lector con cédula {cedula} eliminado del registro.")
        else:
            print("El lector no está registrado.")

    def prestar_libro(self, cedula, isbn):
        if cedula in self.lectores_registrados and isbn in self.catalogo_libros:
            lector = self.lectores_registrados[cedula]
            libro = self.catalogo_libros.pop(isbn)
            lector.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {lector.nombre}")
        else:
            print("Préstamo no realizado. Verifique lector y libro disponible.")

    def devolver_libro(self, cedula, isbn):
        if cedula in self.lectores_registrados:
            lector = self.lectores_registrados[cedula]
            for libro in lector.libros_prestados:
                if libro.isbn == isbn:
                    lector.libros_prestados.remove(libro)
                    self.catalogo_libros[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El lector no tiene este libro en préstamo.")
        else:
            print("Lector no registrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.catalogo_libros.values()
                      if getattr(libro, criterio, "") == valor or valor in libro.detalles]
        return resultados if resultados else "No se encontraron libros."

    def listar_libros_prestados(self, cedula):
        if cedula in self.lectores_registrados:
            lector = self.lectores_registrados[cedula]
            return lector.libros_prestados if lector.libros_prestados else "No tiene libros prestados."
        else:
            return "Lector no registrado."


# Menú interactivo
biblioteca = BibliotecaDigital()

while True:
    print("\n--- Biblioteca Digital ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar lector")
    print("4. Eliminar lector")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        isbn = input("ISBN: ")
        biblioteca.agregar_libro(Libro(titulo, autor, genero, isbn))
    elif opcion == "2":
        isbn = input("Ingrese ISBN del libro a eliminar: ")
        biblioteca.eliminar_libro(isbn)
    elif opcion == "3":
        nombre = input("Nombre del lector: ")
        cedula = input("Cédula: ")
        biblioteca.registrar_lector(Lector(nombre, cedula))
    elif opcion == "4":
        cedula = input("Ingrese la cédula del lector a eliminar: ")
        biblioteca.eliminar_lector(cedula)
    elif opcion == "5":
        cedula = input("Cédula del lector: ")
        isbn = input("ISBN del libro a prestar: ")
        biblioteca.prestar_libro(cedula, isbn)
    elif opcion == "6":
        cedula = input("Cédula del lector: ")
        isbn = input("ISBN del libro a devolver: ")
        biblioteca.devolver_libro(cedula, isbn)
    elif opcion == "7":
        criterio = input("Buscar por (titulo/autor/genero): ")
        valor = input("Valor de búsqueda: ")
        resultados = biblioteca.buscar_libro(criterio, valor)
        print(resultados)
    elif opcion == "8":
        cedula = input("Ingrese la cédula del lector: ")
        print(biblioteca.listar_libros_prestados(cedula))
    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
