import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Registro Interactivo de Datos")  # Título descriptivo
root.geometry("500x400")  # Tamaño de la ventana

# -------------------------------
# Funciones de la aplicación
# -------------------------------

def agregar_dato():
    """Agrega el texto del campo de entrada a la tabla si no está vacío."""
    texto = entrada.get().strip()
    if texto:
        tabla.insert("", "end", values=(texto,))
        entrada.delete(0, tk.END)  # Limpiar campo de texto

def limpiar_datos():
    """Elimina todos los elementos de la tabla."""
    for item in tabla.get_children():
        tabla.delete(item)

# -------------------------------
# Componentes GUI
# -------------------------------

# Etiqueta descriptiva
label = tk.Label(root, text="Ingrese un dato para registrar:", font=("Arial", 12))
label.pack(pady=10)

# Campo de texto para entrada de datos
entrada = tk.Entry(root, font=("Arial", 12), width=40)
entrada.pack(pady=5)

# Botón para agregar datos
btn_agregar = tk.Button(root, text="Agregar", font=("Arial", 12), command=agregar_dato)
btn_agregar.pack(pady=5)

# Botón para limpiar datos
btn_limpiar = tk.Button(root, text="Limpiar", font=("Arial", 12), command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Tabla para mostrar los datos ingresados
tabla = ttk.Treeview(root, columns=("Dato"), show="headings")
tabla.heading("Dato", text="Dato Registrado")
tabla.pack(pady=20, fill="both", expand=True)

# Ejecutar la aplicación
root.mainloop()
