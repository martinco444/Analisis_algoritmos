import random
import matplotlib.pyplot as plt
import time 


def distance(p, q):
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2) ** 0.5

def brute_force(points):
    min_d = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return min_d, pair

def closest_pair_rec(Px, Py):
    """Algoritmo de divide y vencerás."""
    n = len(Px)
    if n <= 3:
        return brute_force(Px)
    
    mid = n // 2
    mid_point = Px[mid]

    Qx, Rx = Px[:mid], Px[mid:]
    Qy, Ry = [], []
    for p in Py:
        (Qy if p[0] <= mid_point[0] else Ry).append(p)

    d_left, pair_left = closest_pair_rec(Qx, Qy)
    d_right, pair_right = closest_pair_rec(Rx, Ry)

    d_min, pair_min = (d_left, pair_left) if d_left < d_right else (d_right, pair_right)

    strip = [p for p in Py if abs(p[0] - mid_point[0]) < d_min]
    
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d_min:
                break
            d = distance(strip[i], strip[j])
            if d < d_min:
                d_min, pair_min = d, (strip[i], strip[j])

    return d_min, pair_min

def closest_pair(points):
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(Px, Py)

def main():
    n = int(input("Ingresa el número de puntos: "))
    start_time = time.time()  # Inicio del cronómetro

    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

    print("Puntos generados:")
    for p in points:
        print(p)

    d, pair = closest_pair(points)
    print(f"\nLa menor distancia es: {d}\nEntre los puntos: {pair[0]} y {pair[1]}")

    x_vals, y_vals = zip(*points)
    plt.scatter(x_vals, y_vals, color="blue", label="Puntos")
    plt.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], "r-", lw=2, label="Par más cercano")
    plt.legend()
    plt.grid()
    plt.show()  

    end_time = time.time()  
    print(f"\nTiempo: {end_time - start_time:.5f} segundos")

if __name__ == '__main__':
    main()
