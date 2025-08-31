import json
#"""""""""""""SISTEMA DE INVENTARI""""""""""
#"""""""""" Clase que representa un producto individual""""""""""""""
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto            # ID único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible
        self.precio = precio            # Precio unitario

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad  # Actualiza la cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio      # Actualiza el precio

    def __str__(self):
        # Representación legible del producto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# """""""Clase que gestiona el conjunto de productos usando un diccionario"""""""""""""
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: clave = ID, valor = objeto Producto

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("❌ El producto ya existe en el inventario.")
        else:
            self.productos[producto.id] = producto
            print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
 #"""""""""""" Búsqueda por nombre (insensible a mayúsculas)"""""""""""""
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, archivo):
        # Serializa el inventario a un archivo JSON
        with open(archivo, 'w') as f:
            json.dump({id: vars(p) for id, p in self.productos.items()}, f)
        print("💾 Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        # Carga el inventario desde un archivo JSON
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id: Producto(**info) for id, info in datos.items()}
            print("📂 Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se inicia inventario vacío.")


# Menú interactivo para el usuario
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n📋 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio unitario: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no aplica): ")
            precio = input("Nuevo precio (dejar vacío si no aplica): ")
            inventario.actualizar_producto(
                id,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("🔍 No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario.json")
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
