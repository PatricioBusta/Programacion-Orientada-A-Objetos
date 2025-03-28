import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

def mark_completed():
    try:
        selected = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected)
        listbox_tasks.delete(selected)
        listbox_tasks.insert(selected, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea para marcarla como completada.")

def delete_task():
    try:
        selected = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected)
    except IndexError:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea para eliminar.")

def add_task_enter(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada
tk.Label(root, text="Nueva Tarea:").pack(pady=5)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
entry_task.bind("<Return>", add_task_enter)

# Botones
tk.Button(root, text="Añadir Tarea", command=add_task).pack(pady=5)
tk.Button(root, text="Marcar como Completada", command=mark_completed).pack(pady=5)
tk.Button(root, text="Eliminar Tarea", command=delete_task).pack(pady=5)

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
