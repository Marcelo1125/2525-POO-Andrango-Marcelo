import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar con: pip install tkcalendar

# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal 🗓️")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f4f7")

        # --- Frame superior: Entrada de datos ---
        self.frame_input = tk.Frame(root, bg="#dbe9f4", padx=10, pady=10)
        self.frame_input.pack(fill=tk.X)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_input, text="Fecha:", bg="#dbe9f4").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_input, text="Hora (HH:MM):", bg="#dbe9f4").grid(row=0, column=2, padx=5)
        self.time_entry = tk.Entry(self.frame_input, width=10)
        self.time_entry.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_input, text="Descripción:", bg="#dbe9f4").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_input, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # --- Frame medio: Botones de acción ---
        self.frame_buttons = tk.Frame(root, bg="#f0f4f7", pady=10)
        self.frame_buttons.pack()

        self.add_btn = tk.Button(self.frame_buttons, text="➕ Agregar Evento", command=self.add_event, bg="#a3d9a5")
        self.add_btn.grid(row=0, column=0, padx=10)

        self.delete_btn = tk.Button(self.frame_buttons, text="🗑️ Eliminar Seleccionado", command=self.delete_event, bg="#f7a4a4")
        self.delete_btn.grid(row=0, column=1, padx=10)

        self.exit_btn = tk.Button(self.frame_buttons, text="🚪 Salir", command=root.quit, bg="#d3d3d3")
        self.exit_btn.grid(row=0, column=2, padx=10)

        # --- Frame inferior: Lista de eventos ---
        self.frame_list = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
        self.frame_list.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=400)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar para TreeView
        scrollbar = ttk.Scrollbar(self.frame_list, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # --- Función para agregar evento ---
    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    # --- Función para eliminar evento seleccionado ---
    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)

# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
