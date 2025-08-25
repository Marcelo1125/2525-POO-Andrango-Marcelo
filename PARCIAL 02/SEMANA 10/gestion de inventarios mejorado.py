import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio, peso):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.peso = peso

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio},{self.peso}"

class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo = "inventario.txt"

    def agregar_producto(self, producto):
        self.productos.append(producto)
        try:
            with open(self.archivo, "a", encoding="utf-8") as f:
                f.write(str(producto) + "\n")
            print("✅ Producto agregado y guardado correctamente.")
        except Exception as e:
            print(f"❌ Error al guardar producto: {e}")

    def eliminar_producto_por_id(self, id):
        self.productos = [p for p in self.productos if p.id != id]
        self.actualizar_archivo()

    def actualizar_producto(self, id, cantidad=None, precio=None, peso=None):
        for p in self.productos:
            if p.id == id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                if peso is not None:
                    p.peso = peso
                self.actualizar_archivo()
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_producto_por_id(self, id):
        for p in self.productos:
            if p.id == id:
                print(f"🆔 {p.id} | 📛 {p.nombre} | 🔢 {p.cantidad} | 💲 {p.precio} | ⚖️ {p.peso} kg")
                return
        print("❌ Producto no encontrado.")

    def mostrar_todos(self):
        if not self.productos:
            print("📂 Inventario vacío.")
        for p in self.productos:
            print(f"🆔 {p.id} | 📛 {p.nombre} | 🔢 {p.cantidad} | 💲 {p.precio} | ⚖️ {p.peso} kg")

    def actualizar_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
        except Exception as e:
            print(f"❌ Error al actualizar archivo: {e}")

def menu():
    inventario = Inventario()

    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║         📋 MENÚ DE INVENTARIO          ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Agregar producto                    ║")
        print("║ 2. Eliminar producto por ID           ║")
        print("║ 3. Actualizar cantidad, precio o peso ║")
        print("║ 4. Buscar producto por ID             ║")
        print("║ 5. Mostrar todos los productos        ║")
        print("║ 6. Salir                              ║")
        print("╚════════════════════════════════════════╝")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            id = input("🆔 ID del producto: ")
            nombre = input("📛 Nombre: ")
            cantidad = int(input("🔢 Cantidad: "))
            precio = float(input("💲 Precio: "))
            peso = float(input("⚖️ Peso (kg): "))
            producto = Producto(id, nombre, cantidad, precio, peso)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("🆔 ID del producto a eliminar: ")
            inventario.eliminar_producto_por_id(id)

        elif opcion == "3":
            id = input("🆔 ID del producto a actualizar: ")
            cantidad = input("🔢 Nueva cantidad (Enter para omitir): ")
            precio = input("💲 Nuevo precio (Enter para omitir): ")
            peso = input("⚖️ Nuevo peso (kg) (Enter para omitir): ")
            inventario.actualizar_producto(
                id,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None,
                float(peso) if peso else None
            )

        elif opcion == "4":
            id = input("🆔 ID del producto a buscar: ")
            inventario.buscar_producto_por_id(id)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
