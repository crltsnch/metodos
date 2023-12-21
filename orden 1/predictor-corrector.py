import matplotlib.pyplot as plt
from math import e

# Método predictor-corrector (Euler mejorado)
def true_solucion(x):
    return (x**2)*e**(-x**2)

def predictor_corrector(f, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        # Predictor (método de Euler)
        y_pred = y + h * f(x, y)
        
        # Corrector (método de Euler mejorado)
        y = y + 0.5 * h * (f(x, y) + f(x + h, y_pred))
        
        x = x + h
        u.append(x)
        v.append(y)
    return u, v


def f(x, y):
    return 2*x*(e**(-x**2)-y)  # Esto se modifica


#Error
def error(v,v_aprox):
    return abs(v-v_aprox)

x_inicial = float(input('Ingrese el valor de x inicial: '))
x_final = float(input('Ingrese el valor de x final: '))
x = 0 # Esto se modifica
y = 0  # Esto se modifica
m = 10   # Esto se modifica
h = (x_final - x_inicial)/m

u, v = predictor_corrector(f, x, y, h, m)

print('w_100', v[-1])
print('Solucion real:', true_solucion(1.5))

#Error
print('Error:', error(true_solucion(1.5),v[-1]))

# Gráfico
plt.plot(u, v, label='Predictor-Corrector')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.show()