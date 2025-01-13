class Contact:
    # Clase que representa un contacto individual.

    def __init__(self, name, phone, address):
        # Inicializa un contacto con nombre, teléfono y dirección.

        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        # Devuelve una representación legible del contacto.

        return f"Nombre: {self.name}, Teléfono: {self.phone}, Dirección: {self.address}"


class ContactAgenda:
    # Clase que gestiona una agenda de contactos.

    def __init__(self):
        # Inicializa la agenda con una lista vacía de contactos.

        self.contacts = []

    def add_contact(self, name, phone, address):
        # Agrega un nuevo contacto a la agenda.

        new_contact = Contact(name, phone, address)
        self.contacts.append(new_contact)
        print(f"Contacto agregado: {new_contact.name}")

    def remove_contact(self, name):
        # Elimina un contacto de la agenda por su nombre.

        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contacto eliminado: {name}")
                return
        print(f"Contacto con el nombre '{name}' no encontrado.")

    def search_contact(self, name):
        # Busca un contacto por su nombre.

        for contact in self.contacts:
            if contact.name == name:
                print("Contacto encontrado:")
                print(contact)
                return
        print(f"Contacto con el nombre '{name}' no encontrado.")

    def list_contacts(self):
        # Lista todos los contactos en la agenda.

        if not self.contacts:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contact in self.contacts:
                print(contact)


def main():
    # Función principal para interactuar con la Agenda de Contactos.

    agenda = ContactAgenda()

    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Listar contactos")
        print("5. Salir")

        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if option == 1:
            name = input("Nombre del contacto: ")
            phone = input("Teléfono del contacto: ")
            address = input("Dirección del contacto: ")
            agenda.add_contact(name, phone, address)
        elif option == 2:
            name = input("Nombre del contacto a eliminar: ")
            agenda.remove_contact(name)
        elif option == 3:
            name = input("Nombre del contacto a buscar: ")
            agenda.search_contact(name)
        elif option == 4:
            agenda.list_contacts()
        elif option == 5:
            print("Saliendo de la Agenda de Contactos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija nuevamente.")


if __name__ == "__main__":
    main()
