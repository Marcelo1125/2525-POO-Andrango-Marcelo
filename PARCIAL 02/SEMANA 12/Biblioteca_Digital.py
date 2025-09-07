
# 📚 Clase Libro: representa un libro con atributos inmutables
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable: (autor, título)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# 👤 Clase Usuario: representa un usuario con libros prestados
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


# 🏛️ Clase Biblioteca: gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # ISBN: Libro
        self.usuarios = {}            # ID: Usuario
        self.ids_registrados = set()  # Conjunto de IDs únicos

    # 📥 Añadir libro
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"✅ Libro añadido: {libro}")
        else:
            print("⚠️ El libro ya está registrado.")

    # 🗑️ Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"🗑️ Libro con ISBN {isbn} eliminado.")
        else:
            print("❌ Libro no encontrado.")

    # 🧾 Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_registrados:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_registrados.add(usuario.id_usuario)
            print(f"👤 Usuario registrado: {usuario}")
        else:
            print("⚠️ ID de usuario ya registrado.")

    # ❌ Dar de baja usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_registrados.remove(id_usuario)
            print(f"👋 Usuario con ID {id_usuario} dado de baja.")
        else:
            print("❌ Usuario no encontrado.")

    # 📚 Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"📖 Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("❌ Usuario o libro no disponible.")

    # 🔄 Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"✅ Libro devuelto: {libro}")
                    return
            print("⚠️ El usuario no tiene este libro.")
        else:
            print("❌ Usuario no encontrado.")

    # 🔍 Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # 📋 Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].libros_prestados
        else:
            print("❌ Usuario no encontrado.")
            return []

#  menú interactivo
def mostrar_menu():
    print("\n📚 MENÚ DE BIBLIOTECA DIGITAL")
    print("1. Añadir libro")
    print("2. Quitar libro por ISBN")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados a usuario")
    print("9. Salir")

# Crear instancia de biblioteca
biblio = Biblioteca()

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-9): ")

    if opcion == "1":
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")
        libro = Libro(titulo, autor, categoria, isbn)
        biblio.añadir_libro(libro)

    elif opcion == "2":
        isbn = input("ISBN del libro a eliminar: ")
        biblio.quitar_libro(isbn)

    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID único del usuario: ")
        usuario = Usuario(nombre, id_usuario)
        biblio.registrar_usuario(usuario)

    elif opcion == "4":
        id_usuario = input("ID del usuario a dar de baja: ")
        biblio.dar_baja_usuario(id_usuario)

    elif opcion == "5":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro a prestar: ")
        biblio.prestar_libro(id_usuario, isbn)

    elif opcion == "6":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro a devolver: ")
        biblio.devolver_libro(id_usuario, isbn)

    elif opcion == "7":
        criterio = input("Buscar por (titulo/autor/categoria): ").lower()
        valor = input("Valor de búsqueda: ")
        resultados = biblio.buscar_libros(criterio, valor)
        if resultados:
            for libro in resultados:
                print("🔎 Encontrado:", libro)
        else:
            print("📭 No se encontraron libros con ese criterio.")

    elif opcion == "8":
        id_usuario = input("ID del usuario: ")
        libros = biblio.listar_libros_prestados(id_usuario)
        if libros:
            for libro in libros:
                print("📚 Prestado:", libro)
        else:
            print("📭 No hay libros prestados o el usuario no existe.")

    elif opcion == "9":
        print("👋 Saliendo del sistema. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción inválida. Intenta nuevamente.")
