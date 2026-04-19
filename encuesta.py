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

promedio = df["calificacion"].mean()
por_genero = df["genero"].value_counts().reset_index()
por_genero.columns = ["genero", "cantidad"]
bajo_3 = df[df["calificacion"] < 3]

print("=== RESULTADOS ===")
print()

print("Promedio de calificacion:", promedio)
print()

print("Cantidad de opiniones por genero:")
print(por_genero)
print()

print("Opiniones con calificacion menor a 3:")
print(bajo_3)

df.to_excel("encuesta_datos.xlsx", index=False)
por_genero.to_excel("encuesta_por_genero.xlsx", index=False)
bajo_3.to_excel("encuesta_bajo_3.xlsx", index=False)

print()
print("Archivos exportados: encuesta_datos.xlsx, encuesta_por_genero.xlsx, encuesta_bajo_3.xlsx")
