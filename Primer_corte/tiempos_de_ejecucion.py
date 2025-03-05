import matplotlib.pyplot as plt
import time
import math

Array = list(range(1,23))

ejecuciones1 = []
ejecuciones2 = []
ejecuciones3 = []
ejecuciones4 = []
ejecuciones5 = []
ejecuciones6 = []
ejecuciones7 = []
ejecuciones8 = []
ejecuciones9 = []
ejecuciones10 = []

#Soluciones para i*=2

def tiempo1():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n):
            i*=2
        end_time = time.perf_counter()
        ejecuciones1.append(end_time - start_time)

def tiempo2():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n**2):
            i*=2
        end_time = time.perf_counter()
        ejecuciones2.append(end_time - start_time)

def tiempo3():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n**3):
            i*=2
        end_time = time.perf_counter()
        ejecuciones3.append(end_time - start_time)

def tiempo4():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(int(math.log(n))):
            i*=2
        end_time = time.perf_counter()
        ejecuciones4.append(end_time - start_time)

def tiempo5():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(2**n):
            i*=2
        end_time = time.perf_counter()
        ejecuciones5.append(end_time - start_time)

#Soluciones para i+=2

def tiempo6():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n):
            i*=2
        end_time = time.perf_counter()
        ejecuciones6.append(end_time - start_time)

def tiempo7():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n**2):
            i*=2
        end_time = time.perf_counter()
        ejecuciones7.append(end_time - start_time)

def tiempo8():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(n**3):
            i*=2
        end_time = time.perf_counter()
        ejecuciones8.append(end_time - start_time)

def tiempo9():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(int(math.log(n))):
            i*=2
        end_time = time.perf_counter()
        ejecuciones9.append(end_time - start_time)

def tiempo10():
    for n in Array:
        start_time = time.perf_counter()
        for i in range(2**n):
            i*=2
        end_time = time.perf_counter()
        ejecuciones10.append(end_time - start_time)

def main():

    tiempo1()
    tiempo2()
    tiempo3()
    tiempo4()
    tiempo5()
    tiempo6()
    tiempo7()
    tiempo8()
    tiempo9()
    tiempo10()

    # Grafica los resultados para i*=2
    plt.plot(Array, ejecuciones1, linestyle='-', color='#FF0000', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones2, linestyle='-', color='#A52A2A', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones3, linestyle='-', color='#00FF00', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones4, linestyle='-', color='#0000FF', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones5, linestyle='-', color='#FFFF00', label="Tiempo de ejecución")
    
    # Grafica los resultados para i+=2
    plt.plot(Array, ejecuciones6, linestyle='-', color='#800080', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones7, linestyle='-', color='#FFA500', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones8, linestyle='-', color='#00FFFF', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones9, linestyle='-', color='#808080', label="Tiempo de ejecución")
    plt.plot(Array, ejecuciones10, linestyle='-',color = '#FFC0CB', label="Tiempo de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Complejidad temporal del tiempo")
    plt.yscale("log")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
