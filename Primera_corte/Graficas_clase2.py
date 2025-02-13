import matplotlib.pyplot as plt
import numpy as np

c = 2  
n_values = np.linspace(0.1, 10, 1000)  

def grafica1(c, n_values):
    return c * n_values **2

def grafica2(c, n_values):
    return c * n_values * np.log(n_values)

y1 = grafica1(c, n_values)
y2 = grafica2(c, n_values)

plt.plot(n_values, y1, label=r'$y = 2n^2$', color='b')  
plt.plot(n_values, y2, label=r'$y = 2n \log(n)$', color='g')  
plt.title("graficas")
plt.legend()
plt.grid()
plt.show()
