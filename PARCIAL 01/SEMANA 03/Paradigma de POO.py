#  Encapsulamiento
# Esta clase guarda los datos del clima como atributos "protegidos" usando guion bajo.
class RegistroClima:
    def __init__(self, temperatura, humedad, presion):
        self._temp = temperatura  # Atributo protegido
        self._hum = humedad       # Encapsulado: no accedemos directamente desde fuera
        self._pres = presion

    def resumen(self):
        # Método público que devuelve los datos como texto. Permite acceder sin mostrar el interior.
        return f"{self._temp}°C, {self._hum}%, {self._pres} hPa"

    def obtener_temp(self):
        # Método para recuperar solo la temperatura (accesor).
        return self._temp

# Herencia + Polimorfismo
# Esta subclase hereda todo de RegistroClima.
class ClimaDiario(RegistroClima):  # <== Herencia
    def __init__(self, dia, t, h, p):
        super().__init__(t, h, p)  # Usamos el constructor de la clase padre
        self.dia = dia             # Atributo adicional propio de esta subclase

    def resumen(self):  # <== Polimorfismo
        # Redefinimos el método de la clase padre para mostrar también el día
        return f"{self.dia}: {super().resumen()}"  # Llamamos al método original con super()

#  Uso del programa

# Creamos una lista de objetos ClimaDiario (uno por día de la semana)
semana = [
    ClimaDiario("Lunes", 22, 60, 1012),
    ClimaDiario("Martes", 24, 55, 1010),
    ClimaDiario("Miércoles", 21, 58, 1008),
    ClimaDiario("Jueves", 23, 62, 1011),
    ClimaDiario("Viernes", 25, 50, 1007),
    ClimaDiario("Sábado", 26, 53, 1009),
    ClimaDiario("Domingo", 20, 65, 1006)
]

# Mostramos los datos de cada día con el método sobrescrito (polimorfismo en acción)
for dia in semana:
    print(dia.resumen())

# Calculamos el promedio de temperatura con una suma simple y división
suma = 0
for dia in semana:
    suma += dia.obtener_temp()  # Acceso seguro a través del método (encapsulamiento)
promedio = suma / len(semana)

# Mostramos el resultado final
print(f"Promedio semanal: {promedio:.2f} °C")