import os

# Clase que representa un producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio, peso):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.peso = peso

    def __str__(self):
        return f"{self.id:<5} | {self.nombre:<20} | {self.cantidad:<8} | ${self.precio:<8.2f} | {self.peso:<6.2f} kg 🏋️"

# Clase que gestiona el inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.\n")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                print("🗑️ Producto eliminado.\n")
                return
        print("❌ Producto no encontrado.\n")

    def actualizar_producto(self, id, cantidad=None, precio=None, peso=None):
        for p in self.productos:
            if p.id == id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                if peso is not None:
                    p.peso = peso
                print("🔄 Producto actualizado.\n")
                return
        print("❌ Producto no encontrado.\n")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("\n🔍 Resultados de búsqueda:")
            self.mostrar_productos(encontrados)
        else:
            print("❌ No se encontraron productos con ese nombre.\n")

    def mostrar_productos(self, lista=None):
        if lista is None:
            lista = self.productos
        if not lista:
            print("📦 No hay productos en el inventario.\n")
            return
        print("\n╔════════════════════════════════════════════════════════════════════╗")
        print("║                         📋 LISTA DE PRODUCTOS                      ║")
        print("╠═════╦════════════════════╦══════════╦════════════╦═══════════╣")
        print("║ ID  ║ Nombre             ║ Cantidad ║ Precio     ║ Peso (kg) ║")
        print("╠═════╬════════════════════╬══════════╬════════════╬═══════════╣")
        for p in lista:
            print(f"║ {p.id:<3} ║ {p.nombre:<18} ║ {p.cantidad:<8} ║ ${p.precio:<9.2f} ║ {p.peso:<8.2f}  ║")
        print("╚═════╩════════════════════╩══════════╩════════════╩═══════════╝\n")

# Función para limpiar la consola
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para validar entrada numérica
def pedir_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            return valor
        except ValueError:
            print("⚠️ Entrada inválida. Intenta nuevamente.")

# Menú principal
def menu():
    inventario = Inventario()
    while True:
        print("╔════════════════════════════════════════╗")
        print("║         📋 MENÚ DE INVENTARIO          ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Agregar producto                    ║")
        print("║ 2. Eliminar producto por ID           ║")
        print("║ 3. Actualizar cantidad, precio o peso ║")
        print("║ 4. Buscar producto por ID       ║")
        print("║ 5. Mostrar todos los productos        ║")
        print("║ 6. Salir                              ║")
        print("╚════════════════════════════════════════╝")
        opcion = input(" Elige una opción (1-6): ")

        limpiar()

        if opcion == "1":
            id = input("🆔 ID del producto: ")
            nombre = input("📛 Nombre: ")
            cantidad = pedir_numero("🔢 Cantidad: ", int)
            precio = pedir_numero("💲 Precio: ")
            peso = pedir_numero(" Peso (kg): ")
            producto = Producto(id, nombre, cantidad, precio, peso)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("🆔 ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("🆔 ID del producto a actualizar: ")
            cantidad = pedir_numero("🔢 Nueva cantidad: ", int)
            precio = pedir_numero("💲 Nuevo precio: ")
            peso = pedir_numero(" Nuevo peso (kg): ")
            inventario.actualizar_producto(id, cantidad, precio, peso)

        elif opcion == "4":
            nombre = input("🔍 Nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 ¡Gracias por usar el sistema de inventario!")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.\n")

# Ejecutar el menú
if __name__ == "__main__":
    menu()



