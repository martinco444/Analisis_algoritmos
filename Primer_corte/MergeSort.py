import numpy as np
import matplotlib.pyplot as plt
import time

# Generar arreglo sin números repetidos
array = np.random.choice(range(0, 101), size=20, replace=False)  # Números únicos sin repetición

def mergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle].copy()  
        right = array[middle:].copy()

        mergeSort(left)
        mergeSort(right)
        
        merge(array, left, right)  
        
def merge(array, left, right):
    i = 0  # Índice de la izquierda
    j = 0  # Índice de la derecha
    k = 0  # Índice combinado

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
        
def graficaComputo():
    tamanos = []
    times = []
    
    for tamano in range(100, 1001, 100):
        array = np.random.choice(range(0, tamano * 2), size=tamano, replace=False)
        start_time = time.perf_counter()
        mergeSort(array)
        end_time = time.perf_counter()
        tiempo = (end_time - start_time) * 1000

        
        tamanos.append(tamano)
        times.append(tiempo)
        
    plt.plot(tamanos, times, color='green')
    plt.title("Variación del Tiempo de Cómputo con Merge Sort")
    plt.xlabel("Tamaño del Arreglo")
    plt.ylabel("Tiempo(ms)")
    plt.grid(True)
    plt.legend()
    plt.show()
        
def mesureTime():
    print(f"original array: {array}")
    start_time = time.perf_counter()
    print(f"start time: {start_time:.1f} seconds")

    mergeSort(array)

    end_time = time.perf_counter()
    print(f"time ends: {end_time:.1f} seconds")
    print("Total time: {:.3f} seconds".format(end_time - start_time))
    print(f"sorted array: {array}")

def main():
    mesureTime()
    graficaComputo()

if __name__ == "__main__":
    main()
