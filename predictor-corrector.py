import matplotlib.pyplot as plt
from math import e

# Método predictor-corrector (Euler mejorado)
def true_solucion(x):
    return (x + 1)**2 - (e**x)/2

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
    return y-x**2+1  # Esto se modifica


#Error
def error(v,v_aprox):
    return abs(v-v_aprox)

x = 0# Esto se modifica
y = 1/2  # Esto se modifica
h = 0.05 # Esto se modifica
m = 10   # Esto se modifica

u, v = predictor_corrector(f, x, y, h, m)

print('w_100', v[-1])
print('Solucion real:', true_solucion(1/2))

#Error
print('Error:', error(true_solucion(1/2),v[-1]))

# Gráfico
plt.plot(u, v, label='Predictor-Corrector')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.show()