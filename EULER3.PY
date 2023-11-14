'''ECUACIÓN 1'''

import matplotlib.pyplot as plt

#Definir el método de Euler con Taylor
def euler(f, x, y, h, n):
    u = []
    v = []
    for i in range(n):
        x = x + h
        y = y + h * f(x, y)
        u.append(x)
        v.append(y)
    return u, v

# Definir la EDO
def f(x, y):
    return (2-3*x-y)/(x-1)


#azul
x = 2
y = -1
h = 0.04
n = 100
u, v = euler(f, x, y, h, n)
#imprime la ultima y del bucle
print(v[-1])

# Graficar la solución

'''plt.plot(u1, v1)
plt.grid(True)
plt.show()'''