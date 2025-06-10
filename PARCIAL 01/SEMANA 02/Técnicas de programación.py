# encapsulación
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria("Marcelo", 1000)
cuenta.depositar(600)
cuenta.retirar(300)
print("Saldo disponible:", cuenta.mostrar_saldo())  # Salida esperada: 1300

from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass  # Método abstracto que debe implementarse en las subclases

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

# Uso
c = Circulo(5)
print("Área del círculo:", c.area())  # Salida esperada: 78.54


# herencia
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Empleado(Persona):  # Hereda de Persona
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Salario: {self.salario}"

# Uso
empleado = Empleado("Marcelo", 30, 2800)
print(empleado.mostrar_info())  # Salida esperada: Nombre: Marcelo, Edad: 30, Salario: 2800


# polimorfismo
class Perro:
    def sonido(self):
        return "Guau"

class Gato:
    def sonido(self):
        return "Miau"

def describir_animal(animal):
    print(f"El animal dice: {animal.sonido()}")

# Uso
perro = Perro()
gato = Gato()

describir_animal(perro)  # Salida esperada: El animal dice: Guau
describir_animal(gato)   # Salida esperada: El animal dice: Miau