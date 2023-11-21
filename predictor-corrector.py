import matplotlib.pyplot as plt

# Método predictor-corrector (Euler mejorado)
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
    return (1+4*x*y) / (3*x**2)  # Esto se modifica

x = 0.5 # Esto se modifica
y = -1  # Esto se modifica
h = 0.035 # Esto se modifica
m = 100   # Esto se modifica

u, v = predictor_corrector(f, x, y, h, m)

print('w_100', v[-1])

#Error

def error(v,v_aprox):
    return abs(v-v_aprox)

print('Error:', error(-11.46,v[-1]))

# Gráfico
plt.plot(u, v, label='Predictor-Corrector')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.show()