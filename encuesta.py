import pandas as pd

opiniones = []

print("=== SISTEMA DE ENCUESTAS DE OPINION ===")
print()

continuar = True
while continuar:
    print("--- Registro de opinion ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = input("Genero (M/F/O): ")
    
    calif_valida = False
    while not calif_valida:
        calif = int(input("Calificacion (1-5): "))
        if calif >= 1 and calif <= 5:
            calif_valida = True
        else:
            print("Error: La calificacion debe estar entre 1 y 5")
    
    persona = {
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "calificacion": calif
    }
    opiniones.append(persona)
    print()
    
    respuesta = input("Desea continuar? (s/n): ")
    print()
    if respuesta.lower() != "s":
        continuar = False

df = pd.DataFrame(opiniones)

print("=== RESULTADOS ===")
print()

print("Promedio de calificacion:", df["calificacion"].mean())
print()

print("Cantidad de opiniones por genero:")
print(df["genero"].value_counts())
print()

print("Opiniones con calificacion menor a 3:")
bajo_3 = df[df["calificacion"] < 3]
print(bajo_3)
