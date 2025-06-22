print("\n" + "="*50)
print("Simulación: Tienda")
print("="*50 + "\n")
# Clase que representa un producto de la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f}"

# Clase que representa un carrito de compras
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        print("Carrito de Compras:")
        for producto in self.productos:
            print(" -", producto.mostrar_info())

    def total(self):
        return sum(p.precio for p in self.productos)

# Simulación
if __name__ == "__main__":
    # Creamos algunos productos
    p1 = Producto("Manzanas", 1.25)
    p2 = Producto("Pan", 2.50)
    p3 = Producto("leche", 1.50)

    # Creamos un carrito y añadimos productos
    carrito = Carrito()
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)
    # Mostramos el contenido del carrito y el total
    carrito.mostrar_carrito()
    print(f"Total a pagar: ${carrito.total():.2f}")


#*********gestor de biblioteca*******
    print("\n" + "=" * 40)
    print("Simulación Programa de Biblioteca")
    print("=" * 40 + "\n")
    # Clase que representa un libro
    class Libro:
        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor
            self.prestado = False  # Estado del libro

        def prestar(self):
            if not self.prestado:
                self.prestado = True
                return f"Has prestado el libro: {self.titulo}"
            return f"El libro '{self.titulo}' ya está prestado."

        def devolver(self):
            if self.prestado:
                self.prestado = False
                return f"Has devuelto el libro: {self.titulo}"
            return f"El libro '{self.titulo}' no estaba prestado."


    # Clase que administra los libros
    class Biblioteca:
        def __init__(self):
            self.libros = []
            print("Biblioteca Personal:")

        def agregar_libro(self, libro):
            self.libros.append(libro)

        def mostrar_libros(self):
            for libro in self.libros:
                estado = "Prestado" if libro.prestado else "Disponible"
                print(f"{libro.titulo} por {libro.autor} - {estado}")


    # Simulación
    if __name__ == "__main__":
        libro1 = Libro("1984", "George Orwell")
        libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

        mi_biblioteca = Biblioteca()
        mi_biblioteca.agregar_libro(libro1)
        mi_biblioteca.agregar_libro(libro2)

        mi_biblioteca.mostrar_libros()
        print(libro1.prestar())
        mi_biblioteca.mostrar_libros()
        print(libro1.devolver())
        mi_biblioteca.mostrar_libros()

