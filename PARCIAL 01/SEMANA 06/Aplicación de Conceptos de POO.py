# Clase base: Instrumento
class Instrumento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre            # Atributo público
        self.__tipo = tipo              # Atributo privado (encapsulación)

    def describir(self):
        print(f"Este instrumento es un {self.__tipo} llamado {self.nombre}.")

    def tocar(self):
        print(f"{self.nombre} está siendo tocado de forma genérica.")

    # Método para acceder al atributo privado __tipo
    def obtener_tipo(self):
        return self.__tipo


# Clase derivada: Guitarra
class Guitarra(Instrumento):
    def __init__(self, nombre, cuerdas):
        super().__init__(nombre, "cuerda")  # Herencia: invoca al constructor de Instrumento
        self.cuerdas = cuerdas              # Atributo adicional para guitarra

    # Sobreescribimos el método tocar (polimorfismo por sobrescritura)
    def tocar(self):
        print(f"{self.nombre}, una guitarra de {self.cuerdas} cuerdas, está siendo tocada con rasgueos.")

    # Polimorfismo por argumentos opcionales
    def afinar(self, nivel="medio"):
        print(f"{self.nombre} se está afinando a un nivel {nivel}.")


# Clase derivada: Piano
class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "teclado")  # Herencia con tipo específico

    def tocar(self):
        print(f"{self.nombre} está siendo tocado con notas suaves y dulces.")

    def afinar(self):
        print(f"{self.nombre} está siendo afinado por un musico profesional.")


# ===========================
# Uso del programa (Instancias)
# ===========================

guitarra1 = Guitarra("Fender Acústica", 6)
piano1 = Piano("Yamaha Grand de 8 octavas")

# Encapsulación: accediendo al atributo privado a través de método público
print("Tipo de instrumento (encapsulado):", guitarra1.obtener_tipo())

# Herencia y polimorfismo: invocando métodos compartidos y sobrescritos
instrumentos = [guitarra1, piano1]
for instrumento in instrumentos:
    instrumento.describir()
    instrumento.tocar()  # Polimorfismo: comportamiento distinto para cada clase

# Polimorfismo adicional: métodos con diferentes firmas
guitarra1.afinar("alto")
guitarra1.afinar()  # Usa nivel por defecto
piano1.afinar()