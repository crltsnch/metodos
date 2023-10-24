import numpy as np
import matplotlib.pyplot as plt

def euler(f, x, y, h, n):
    u = []
    v = []
    for i in range(n):
        x = x + h
        y = y + h * f(x, y)
        u.append(x)
        v.append(y)
    return u, v
# Definir la EDO y el método de Euler con Taylor de primer orden
def f(x, y):
    return (2 - x - y) / (x - y + 4)

# Parámetros para el método de Euler con Taylor
x = 0  # Valor inicial de x
y = 2.0  # Valor inicial de y
h = 0.05  # Tamaño del paso
n = 100  # Número de pasos
u, v = euler(f, x, y, h, n)

# Graficar la solución
plt.plot(u, v)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Solución de y' = (2-x-y) / (x-y+4) con Euler y Taylor")
plt.grid(True)
plt.show()