import random

# Dimensiones
ciudades = 3
semanas = 2
dias = 7

# Matriz 3D: [ciudad][semana][dia]
temperaturas = [[[0 for d in range(dias)] for s in range(semanas)] for c in range(ciudades)]

# Nombres de ejemplo
nombres_ciudades = ["Buenos Aires", "Las Golondrinas", "Esmeraldas"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Llenar con temperaturas aleatorias (10°C a 35°C)
for c in range(ciudades):
    for s in range(semanas):
        for d in range(dias):
            temperaturas[c][s][d] = random.randint(10, 35)

# Calcular y mostrar promedios
for c in range(ciudades):
    print(f"\nCiudad: {nombres_ciudades[c]}")
    for s in range(semanas):
        suma = sum(temperaturas[c][s])
        promedio = suma / dias
        print(f"  Semana {s+1}: Promedio = {promedio:.2f} °C")

# Mostrar todos los datos (opcional)
print("\n=== Datos registrados ===")
for c in range(ciudades):
    print(f"\nCiudad: {nombres_ciudades[c]}")
    for s in range(semanas):
        print(f"  Semana {s+1}:")
        for d in range(dias):
            print(f"    {dias_semana[d]}: {temperaturas[c][s][d]} °C")
