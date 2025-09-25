
# 1) Crear el diccionario
informacion_personal = {
    "Nombre": "Martha Pinargote",
    "Edad": 28,
    "Ciudad": "Quito",
    "Profesion": "Analista de datos"
}

# 2) Acceder al valor asociado con "ciudad" y mostrarlo
print("Ciudad original:", informacion_personal["Ciudad"])

# 3) Modificar la ciudad por otra
informacion_personal["Ciudad"] = "Guayaquil"
print("Ciudad modificada:", informacion_personal["Ciudad"])

# 4) Agregar o actualizar la clave "profesion" (según la instrucción)
# Aquí la actualizamos a una profesión distinta (si no existía, se agregaría).
informacion_personal["Profesion"] = "Desarrolladora Python"
print("Profesión actualizada:", informacion_personal["Profesion"])

# 5) Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 9 1234 5678"  # número ficticio
    print("Se agregó la clave 'telefono'.")

# 6) Eliminar la clave "edad" porque no es necesaria
if "edad" in informacion_personal:
    informacion_personal.pop("edad")
    print("Se eliminó la clave 'edad'.")

# 7) Imprimir el diccionario final
print("\nDiccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
