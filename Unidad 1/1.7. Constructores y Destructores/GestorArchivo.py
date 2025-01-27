class GestorDeArchivo:
    #  Esta clase permite manejar operaciones con archivos.

    def __init__(self, nombre_archivo, modo):
        # Constructor que abre un archivo y lo inicializa.

        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
        try:
            self.archivo = open(nombre_archivo, modo)
            print(f"El archivo '{self.nombre_archivo}' ha sido abierto en modo '{self.modo}'.")
        except Exception as e:
            print(f"No se pudo abrir el archivo: {e}")

    def escribir_linea(self, contenido):
        # Escribe una línea de texto en el archivo.

        if self.archivo and ('w' in self.modo or 'a' in self.modo):
            self.archivo.write(contenido + '\n')
            print(f"Se escribió en '{self.nombre_archivo}': {contenido}")
        else:
            print("El archivo no está en un modo que permita escribir.")

    def __del__(self):
        # Destructor que cierra el archivo si está abierto.

        if self.archivo:
            try:
                self.archivo.close()
                print(f"El archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")
            except Exception as e:
                print(f"Error al intentar cerrar el archivo: {e}")


# Demostración del programa
if __name__ == "__main__":
    # Crear una instancia de GestorDeArchivo
    gestor = GestorDeArchivo("archivo_prueba.txt", "w")

    # Escribir en el archivo
    gestor.escribir_linea(
        "Este es un ejemplo de implementación personalizada de constructores y destructores en Python.")

    # Forzar la eliminación
    del gestor
    print("Fin del programa. El archivo ha sido manejado correctamente.")
