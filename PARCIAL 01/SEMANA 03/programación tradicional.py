# Función para devolver una lista con las temperaturas de la semana
def ingresar_temperaturas():
    # Temperaturas de ejemplo en grados Celsius
    return [21, 12.1, 11, 14.3, 20.8, 18.7, 16.0]


# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)

    print("Temperaturas registradas:")
    for i, temp in enumerate(temperaturas, start=1):
        print(f"Día {i}: {temp:.1f}°C")

    print(f"\nPromedio semanal: {promedio:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()