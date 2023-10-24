'''ECUACIÓN 1'''

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
    return (2 - x - y)/(x - y + 4)


#azul
x1 = 3 
y1 = 4
h1 = 0.1
n1 = 55
u1, v1 = euler(f, x1, y1, h1, n1)

#naranja
x2 = -2
y2 = 0
h2 = 0.1
n2 = 55
u2, v2 = euler(f, x2, y2, h2, n2)


#verde
x3 = -3
y3 = 4
h3 = 0.1
n3 = 55
u3, v3 = euler(f, x3, y3, h3, n3)

# Graficar la solución

plt.plot(u1, v1)
plt.plot(u2, v2)
plt.plot(u3, v3)
plt.grid(True)
plt.show()