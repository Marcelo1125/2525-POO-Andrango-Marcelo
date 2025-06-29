# Convertidor de distancias: metros, kilómetros y centímetros

def convertir_distancia(valor: float, opcion: int) -> float:
    """
    Convierte una distancia según la opción seleccionada.
    Opción 1: Metros a kilómetros
    Opción 2: Metros a centímetros
    Opción 3: Kilómetros a metros
    """
    if opcion == 1:
        return valor / 1000
    elif opcion == 2:
        return valor * 100
    elif opcion == 3:
        return valor * 1000
    else:
        print("Opción inválida.")
        return None

# Mostrar opciones
print("=== Convertidor de Distancias ===")
print("1. Metros a Kilómetros")
print("2. Metros a Centímetros")
print("3. Kilómetros a Metros")

# Entrada usuario
opcion = int(input("Selecciona una opción (1-3): "))
valor_original = float(input("Ingresa el valor a convertir: "))

#  mostrar resultado
resultado = convertir_distancia(valor_original, opcion)

if resultado is not None:
    print("Resultado:", round(resultado, 2))
    # Verificación booleana: ¿el resultado es mayor que 1000?
    es_grande = resultado > 1000
    print("¿Es una distancia grande?", es_grande)