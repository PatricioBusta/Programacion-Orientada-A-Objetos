import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para entrada de datos
entry_frame = tk.Frame(root, padx=10, pady=10)
entry_frame.pack(fill="x")

# Etiquetas y entradas
tk.Label(entry_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(entry_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Spinboxes para seleccionar hora y minutos
tk.Label(entry_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
hour_spinbox = tk.Spinbox(entry_frame, from_=0, to=23, width=5, format="%02.0f")
hour_spinbox.grid(row=1, column=1, padx=2, pady=5, sticky="w")
tk.Label(entry_frame, text=":").grid(row=1, column=1, padx=(45, 0), pady=5)
minute_spinbox = tk.Spinbox(entry_frame, from_=0, to=59, width=5, format="%02.0f")
minute_spinbox.grid(row=1, column=1, padx=(65, 0), pady=5, sticky="w")

tk.Label(entry_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(entry_frame, width=40)
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame para TreeView
tree_frame = tk.Frame(root, padx=10, pady=10)
tree_frame.pack(fill="both", expand=True)

event_tree = ttk.Treeview(tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
event_tree.heading("Fecha", text="Fecha")
event_tree.heading("Hora", text="Hora")
event_tree.heading("Descripción", text="Descripción")
event_tree.pack(fill="both", expand=True)

# Funciones
def limpiar_campos():
    date_entry.set_date('')
    hour_spinbox.delete(0, tk.END)
    hour_spinbox.insert(0, "00")
    minute_spinbox.delete(0, tk.END)
    minute_spinbox.insert(0, "00")
    description_entry.delete(0, tk.END)

def agregar_evento():
    fecha = date_entry.get()
    hora = f"{int(hour_spinbox.get()):02}:{int(minute_spinbox.get()):02}"
    descripcion = description_entry.get()
    if fecha and descripcion:
        event_tree.insert("", "end", values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar completos")

def eliminar_evento():
    selected_item = event_tree.selection()
    if selected_item:
        if messagebox.askyesno("Confirmación", "¿Desea eliminar el evento seleccionado?"):
            event_tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

# Frame para botones
button_frame = tk.Frame(root, padx=10, pady=10)
button_frame.pack(fill="x")

add_button = tk.Button(button_frame, text="Agregar Evento", command=agregar_evento)
add_button.pack(side="left", padx=5)

delete_button = tk.Button(button_frame, text="Eliminar Evento Seleccionado", command=eliminar_evento)
delete_button.pack(side="left", padx=5)

exit_button = tk.Button(button_frame, text="Salir", command=root.quit)
exit_button.pack(side="right", padx=5)

# Ejecutar aplicación
root.mainloop()
