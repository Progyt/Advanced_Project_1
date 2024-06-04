# Datos TOPFLUX Aerosols

import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Datos de ejemplo
data_1 = """
  3.000e-01  1.211e+01  1.246e+01  1.330e+01  1.277e+01  1.335e+01
  4.000e-01  1.093e+03  1.113e+03  1.158e+03  1.130e+03  1.161e+03
  5.000e-01  1.390e+03  1.409e+03  1.454e+03  1.426e+03  1.457e+03
  6.000e-01  1.317e+03  1.333e+03  1.369e+03  1.346e+03  1.371e+03
  7.000e-01  8.017e+02  8.088e+02  8.245e+02  8.148e+02  8.254e+02
  8.000e-01  4.938e+02  4.968e+02  5.031e+02  4.993e+02  5.035e+02
  9.000e-01  2.761e+02  2.780e+02  2.822e+02  2.796e+02  2.825e+02
  1.000e+00  3.291e+02  3.307e+02  3.341e+02  3.321e+02  3.343e+02
  1.100e+00  1.907e+02  1.919e+02  1.945e+02  1.928e+02  1.946e+02
  1.200e+00  1.981e+02  1.991e+02  2.013e+02  2.000e+02  2.014e+02
  1.300e+00  1.888e+02  1.897e+02  1.917e+02  1.905e+02  1.918e+02
  1.400e+00  6.121e-02  6.195e-02  6.367e-02  6.259e-02  6.378e-02
  1.500e+00  1.497e+02  1.505e+02  1.521e+02  1.511e+02  1.522e+02
  1.600e+00  1.386e+02  1.391e+02  1.401e+02  1.395e+02  1.402e+02
  1.700e+00  1.241e+02  1.244e+02  1.252e+02  1.247e+02  1.252e+02
  1.800e+00  1.451e+01  1.458e+01  1.473e+01  1.463e+01  1.474e+01
  1.900e+00  2.958e-04  2.979e-04  3.027e-04  2.997e-04  3.031e-04
  2.000e+00  3.816e+01  3.825e+01  3.847e+01  3.833e+01  3.848e+01
  2.100e+00  6.394e+01  6.405e+01  6.430e+01  6.415e+01  6.432e+01
  2.200e+00  4.606e+01  4.613e+01  4.631e+01  4.620e+01  4.632e+01
  2.300e+00  4.484e+01  4.492e+01  4.510e+01  4.499e+01  4.511e+01
  2.400e+00  2.886e+01  2.892e+01  2.907e+01  2.898e+01  2.908e+01
"""

# Función para parsear datos y realizar la interpolación
def parse_and_interpolate(data):
    lines = data.strip().split('\n')
    um = []
    w_m2_um = []
    for line in lines:
        values = line.split()
        um.append(float(values[0]))
        w_m2_um.append([float(val) for val in values[1:]])

    return np.array(um), np.array(w_m2_um)

um_1, w_m2_um_1 = parse_and_interpolate(data_1)

# Ahora podemos realizar la interpolación lineal para cada columna e integrar
def integrate_w_m2_um(um, w_m2_um):
    integrals = []
    for i in range(w_m2_um.shape[1]):
        interp_func = interp1d(um, w_m2_um[:, i], kind='linear', fill_value="extrapolate")
        integral, _ = quad(interp_func, min(um), max(um))
        integrals.append(integral)
    return integrals

integrals_1 = integrate_w_m2_um(um_1, w_m2_um_1)
print(integrals_1)


# Función para parsear datos y realizar la interpolación
def parse_and_interpolate(data):
    lines = data.strip().split('\n')
    um = []
    w_m2_um = []
    for line in lines:
        values = line.split()
        um.append(float(values[0]))
        w_m2_um.append([float(val) for val in values[1:]])

    return np.array(um), np.array(w_m2_um)

# Función para graficar datos con interpolación lineal
def plot_interpolation(data):
    um, w_m2_um = parse_and_interpolate(data)
    x_new = np.linspace(min(um), max(um), 500)
    
    plt.figure(figsize=(12, 8))
    
    for i in range(w_m2_um.shape[1]):
        AOD = [0, 0.2, 0.4, 0.6, 0.8, 1]
        interp_func = interp1d(um, w_m2_um[:, i], kind='linear', fill_value="extrapolate")
        y_new = interp_func(x_new)
        plt.plot(um, w_m2_um[:, i], 'o')
        plt.plot(x_new, y_new, '-', label=f'AOD500nm {AOD[i]}')
    
    plt.xlabel('wavelenght (µm)')
    plt.ylabel('W/m^2/µm')
    plt.title('TOPFLUX aerosols')
    plt.legend()
    plt.grid(True)
    plt.show()

# Datos de ejemplo (misma cadena que antes)
data_1 = """
 3.000e-01  1.211e+01  1.246e+01  1.330e+01  1.277e+01  1.335e+01
  4.000e-01  1.093e+03  1.113e+03  1.158e+03  1.130e+03  1.161e+03
  5.000e-01  1.390e+03  1.409e+03  1.454e+03  1.426e+03  1.457e+03
  6.000e-01  1.317e+03  1.333e+03  1.369e+03  1.346e+03  1.371e+03
  7.000e-01  8.017e+02  8.088e+02  8.245e+02  8.148e+02  8.254e+02
  8.000e-01  4.938e+02  4.968e+02  5.031e+02  4.993e+02  5.035e+02
  9.000e-01  2.761e+02  2.780e+02  2.822e+02  2.796e+02  2.825e+02
  1.000e+00  3.291e+02  3.307e+02  3.341e+02  3.321e+02  3.343e+02
  1.100e+00  1.907e+02  1.919e+02  1.945e+02  1.928e+02  1.946e+02
  1.200e+00  1.981e+02  1.991e+02  2.013e+02  2.000e+02  2.014e+02
  1.300e+00  1.888e+02  1.897e+02  1.917e+02  1.905e+02  1.918e+02
  1.400e+00  6.121e-02  6.195e-02  6.367e-02  6.259e-02  6.378e-02
  1.500e+00  1.497e+02  1.505e+02  1.521e+02  1.511e+02  1.522e+02
  1.600e+00  1.386e+02  1.391e+02  1.401e+02  1.395e+02  1.402e+02
  1.700e+00  1.241e+02  1.244e+02  1.252e+02  1.247e+02  1.252e+02
  1.800e+00  1.451e+01  1.458e+01  1.473e+01  1.463e+01  1.474e+01
  1.900e+00  2.958e-04  2.979e-04  3.027e-04  2.997e-04  3.031e-04
  2.000e+00  3.816e+01  3.825e+01  3.847e+01  3.833e+01  3.848e+01
  2.100e+00  6.394e+01  6.405e+01  6.430e+01  6.415e+01  6.432e+01
  2.200e+00  4.606e+01  4.613e+01  4.631e+01  4.620e+01  4.632e+01
  2.300e+00  4.484e+01  4.492e+01  4.510e+01  4.499e+01  4.511e+01
  2.400e+00  2.886e+01  2.892e+01  2.907e+01  2.898e+01  2.908e+01
"""

# Usar la función para graficar los datos con interpolación
plot_interpolation(data_1)

