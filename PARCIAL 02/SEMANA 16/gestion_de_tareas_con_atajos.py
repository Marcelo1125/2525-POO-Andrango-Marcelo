import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Lista para almacenar las tareas
tareas = []

# Función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        tareas.append({"texto": tarea, "completada": False})
        entrada_tarea.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()

# Función para eliminar una tarea
def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    root.quit()

# Función para actualizar la lista visual de tareas
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        texto = tarea["texto"]
        if tarea["completada"]:
            texto = f"[✔] {texto}"
        else:
            texto = f"[ ] {texto}"
        lista_tareas.insert(tk.END, texto)

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(root, font=("Arial", 14))
entrada_tarea.pack(pady=10, padx=10, fill=tk.X)

# Botón para añadir tarea
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

# Botón para marcar como completada
btn_completar = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

# Botón para eliminar tarea
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas (Listbox)
lista_tareas = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Asociar atajos de teclado
root.bind("<Return>", agregar_tarea)       # Enter para añadir tarea
root.bind("<c>", completar_tarea)          # C para completar tarea
root.bind("<d>", eliminar_tarea)           # D para eliminar tarea
root.bind("<Delete>", eliminar_tarea)      # Delete también elimina
root.bind("<Escape>", cerrar_aplicacion)   # Escape para cerrar

# Ejecutar la aplicación
root.mainloop()
