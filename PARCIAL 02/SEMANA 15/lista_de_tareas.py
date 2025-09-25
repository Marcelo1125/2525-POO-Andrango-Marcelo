# LISTA DE TAREAS
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Lista para almacenar las tareas (cada tarea es un diccionario con texto y estado)
tareas = []

# Función para añadir una nueva tarea
def añadir_tarea(event=None):
    texto = entrada_tarea.get().strip()
    if texto:
        tareas.append({"texto": texto, "completada": False})
        entrada_tarea.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Entrada vacía", "Por favor escribe una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = not tareas[index]["completada"]
        actualizar_lista()
    else:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla.")

# Función para eliminar una tarea
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        del tareas[index]
        actualizar_lista()
    else:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")

# Función para actualizar visualmente la lista de tareas
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        texto = tarea["texto"]
        if tarea["completada"]:
            texto += " ✔️"
        lista_tareas.insert(tk.END, texto)

# Función para manejar doble clic en una tarea (marcar como completada)
def doble_click(event):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = not tareas[index]["completada"]
        actualizar_lista()

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(root, font=("Arial", 12))
entrada_tarea.pack(pady=10, padx=10, fill=tk.X)
entrada_tarea.bind("<Return>", añadir_tarea)  # Añadir tarea con Enter

# Botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)

btn_añadir = tk.Button(frame_botones, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(side=tk.LEFT, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
lista_tareas.bind("<Double-Button-1>", doble_click)  # Doble clic para marcar como completada

# Ejecutar la aplicación
root.mainloop()
