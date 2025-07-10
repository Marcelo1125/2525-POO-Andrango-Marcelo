#******** PRIMER EJEMPLO ******
class Persona:
    # El constructor se llama automáticamente al crear el objeto
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Hola, me llamo {self.nombre}.")

    # El destructor se llama cuando el objeto deja de usarse o el programa termina
    def __del__(self):
        print(f"Adiós, {self.nombre} se va.")

# Uso del programa
persona1 = Persona("Marcelo")  # Se llama al constructor
print("La persona está haciendo algo...")
# Cuando termina el programa o se borra persona1, se llama al destructor
#*********SEGUNDO EJEMPLO **********

class Mascota:
    # El constructor se llama automáticamente al crear una mascota
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"{self.nombre} es una {self.tipo} muy feliz.")

    # El destructor se llama cuando el objeto ya no se necesita
    def __del__(self):
        print(f"{self.nombre} se ha ido a dormir. ¡Hasta pronto!")

# Ejemplo de uso
mascota1 = Mascota("Luna", "gatita")  # Se crea la mascota (llama a __init__)
print("Luna está jugando con una pelota.")
# Al terminar el programa o eliminar mascota1, se llama a __del__