#martin correa
def orden_multiplicacion_matrices(dim):
    cantidad = len(dim) - 1
    costos = [[0 for _ in range(cantidad)] for _ in range(cantidad)]
    cortes = [[0 for _ in range(cantidad)] for _ in range(cantidad)]

    for longitud in range(2, cantidad + 1):
        for inicio in range(cantidad - longitud + 1):
            fin = inicio + longitud - 1
            costos[inicio][fin] = float('inf')
            for division in range(inicio, fin):
                temp = costos[inicio][division] + costos[division + 1][fin] + dim[inicio] * dim[division + 1] * dim[fin + 1]
                if temp < costos[inicio][fin]:
                    costos[inicio][fin] = temp
                    cortes[inicio][fin] = division
    return costos, cortes

def mostrar_parentesis_optimos(cortes, izq, der):
    if izq == der:
        print(f"M{izq+1}", end="")
    else:
        print("(", end="")
        mostrar_parentesis_optimos(cortes, izq, cortes[izq][der])
        mostrar_parentesis_optimos(cortes, cortes[izq][der] + 1, der)
        print(")", end="")

def imprimir_matriz(matriz, nombre="Tabla"):
    print(f"{nombre}:")
    for fila in matriz:
        print("[" + "  ".join(f"{valor:5}" for valor in fila) + "]")

dimensiones = [1, 2, 3, 4, 5]
tabla_costos, tabla_cortes = orden_multiplicacion_matrices(dimensiones)

print("Costo mínimo de multiplicaciones:", tabla_costos[0][-1])
print("Paréntesis óptimos:", end=" ")
mostrar_parentesis_optimos(tabla_cortes, 0, len(dimensiones) - 2)
print("\n")

imprimir_matriz(tabla_costos, "Tabla de costos mínimos")
imprimir_matriz(tabla_cortes, "Tabla de cortes óptimos")