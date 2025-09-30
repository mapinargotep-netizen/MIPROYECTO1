# --- Escritura de Archivo de Texto ---
# Creamos un nuevo archivo llamado my_notes.txt
# El modo "w" sobrescribe el archivo si ya existe
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales en el archivo
archivo.write("Hoy aprendí a trabajar con archivos de texto en Python.\n")
archivo.write("Me parece importante cerrar los archivos después de usarlos.\n")
archivo.write("Practicar me ayuda a entender mejor la programación.\n")

# Cerramos el archivo después de escribir
archivo.close()

# --- Lectura de Archivo de Texto ---
# Abrimos el archivo my_notes.txt en modo lectura
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline()
print("Contenido del archivo my_notes.txt:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina el salto de línea al mostrar
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
