def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio de cada ciudad.
    Recibe una lista de listas con temperaturas [ciudades][semanas].
    Devuelve una lista con los promedios de cada ciudad.
    """
    promedios = []

    # Recorremos cada ciudad
    for ciudad in temperaturas:
        suma = 0
        # Recorremos las semanas de esa ciudad
        for temp in ciudad:
            suma += temp
        # Promedio de la ciudad
        promedio = suma / len(ciudad)
        promedios.append(promedio)

    return promedios


# Bloque principal
if __name__ == "__main__":
    # Ejemplo de matriz de temperaturas: 3 ciudades, 4 semanas
    temperaturas = [
        [20.5, 22.0, 19.8, 21.3],  # Ciudad 1
        [25.0, 24.5, 26.1, 23.9],  # Ciudad 2
        [18.2, 19.0, 17.5, 18.7]   # Ciudad 3
    ]

    # Llamamos a la función
    promedios = calcular_promedio(temperaturas)

    # Mostramos resultados
    for i in range(len(promedios)):
        print(f"Ciudad {i+1} - Promedio: {promedios[i]:.2f} °C")
