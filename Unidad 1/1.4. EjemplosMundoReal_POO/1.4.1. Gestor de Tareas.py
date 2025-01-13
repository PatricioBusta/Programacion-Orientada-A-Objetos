class Task:
    # Clase que representa una tarea individual.
    

    def __init__(self, title, description):
        # Inicializa una tarea con un título y una descripción.

        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        # Marca la tarea como completada.

        self.completed = True

    def __str__(self):
        # Devuelve una representación legible de la tarea.

        status = "Completada" if self.completed else "Pendiente"
        return f"[{'X' if self.completed else ' '}] {self.title}: {self.description} ({status})"


class TaskManager:
    # Clase que gestiona un conjunto de tareas.

    def __init__(self):
        # Inicializa el gestor de tareas con una lista vacía de tareas.

        self.tasks = []

    def add_task(self, title, description):
        # Agrega una nueva tarea al gestor.

        new_task = Task(title, description)
        self.tasks.append(new_task)

    def remove_task(self, index):
        # Elimina una tarea por su índice.

        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Tarea eliminada: {removed_task.title}")
        else:
            print("Índice inválido. No se eliminó ninguna tarea.")

    def complete_task(self, index):
        # Marca una tarea como completada por su índice.

        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Tarea marcada como completada: {self.tasks[index].title}")
        else:
            print("Índice inválido. No se pudo completar la tarea.")

    def list_tasks(self):
        # Lista todas las tareas con su estado.

        if not self.tasks:
            print("No hay tareas en el gestor.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")


def main():
    # Función principal para interactuar con el Gestor de Tareas.

    task_manager = TaskManager()

    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Listar tareas")
        print("5. Salir")

        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if option == 1:
            title = input("Título de la tarea: ")
            description = input("Descripción de la tarea: ")
            task_manager.add_task(title, description)
            print("Tarea agregada con éxito.")
        elif option == 2:
            task_manager.list_tasks()
            try:
                index = int(input("Índice de la tarea a eliminar: "))
                task_manager.remove_task(index)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif option == 3:
            task_manager.list_tasks()
            try:
                index = int(input("Índice de la tarea a completar: "))
                task_manager.complete_task(index)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif option == 4:
            task_manager.list_tasks()
        elif option == 5:
            print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija nuevamente.")


if __name__ == "__main__":
    main()
