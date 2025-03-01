import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("ID ya existente. No se puede agregar el producto.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [prod for prod in self.productos.values() if prod.nombre.lower() == nombre.lower()]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(
                f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, archivo)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id_p: Producto(**p) for id_p, p in datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for prod in productos:
                    print(
                        f"ID: {prod.id_producto}, Nombre: {prod.nombre}, Cantidad: {prod.cantidad}, Precio: {prod.precio}")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
