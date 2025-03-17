import tkinter as tk
from tkinter import messagebox

def agregar_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_lista():
    listbox.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

# Etiqueta
label = tk.Label(root, text="Ingrese un elemento:")
label.pack(pady=5)

# Campo de texto
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Botón para agregar
btn_agregar = tk.Button(root, text="Agregar", command=agregar_item)
btn_agregar.pack(pady=5)

# Lista para mostrar datos
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

# Botón para limpiar
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
