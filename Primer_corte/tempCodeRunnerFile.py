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