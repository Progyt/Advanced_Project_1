# Datos BOTFLUX Aerosols
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Datos de ejemplo
data_1 = """
  3.000e-01  3.632e+02  3.632e+02  3.632e+02  3.632e+02  3.632e+02
  4.000e-01  1.228e+03  1.236e+03  1.253e+03  1.242e+03  1.255e+03
  5.000e-01  1.548e+03  1.555e+03  1.571e+03  1.561e+03  1.572e+03
  6.000e-01  1.524e+03  1.530e+03  1.543e+03  1.535e+03  1.544e+03
  7.000e-01  1.065e+03  1.064e+03  1.061e+03  1.063e+03  1.061e+03
  8.000e-01  6.829e+02  6.780e+02  6.662e+02  6.737e+02  6.654e+02
  9.000e-01  6.866e+02  6.843e+02  6.789e+02  6.823e+02  6.785e+02
  1.000e+00  4.167e+02  4.127e+02  4.033e+02  4.093e+02  4.027e+02
  1.100e+00  4.663e+02  4.648e+02  4.613e+02  4.635e+02  4.611e+02
  1.200e+00  3.480e+02  3.463e+02  3.423e+02  3.449e+02  3.421e+02
  1.300e+00  3.137e+02  3.124e+02  3.092e+02  3.112e+02  3.090e+02
  1.400e+00  3.540e+02  3.540e+02  3.542e+02  3.541e+02  3.542e+02
  1.500e+00  2.559e+02  2.556e+02  2.549e+02  2.554e+02  2.549e+02
  1.600e+00  1.755e+02  1.749e+02  1.735e+02  1.744e+02  1.734e+02
  1.700e+00  1.514e+02  1.510e+02  1.499e+02  1.506e+02  1.498e+02
  1.800e+00  1.691e+02  1.691e+02  1.691e+02  1.691e+02  1.691e+02
  1.900e+00  1.352e+02  1.352e+02  1.353e+02  1.352e+02  1.353e+02
  2.000e+00  1.158e+02  1.158e+02  1.159e+02  1.159e+02  1.159e+02
  2.100e+00  8.119e+01  8.114e+01  8.104e+01  8.110e+01  8.103e+01
  2.200e+00  6.118e+01  6.114e+01  6.103e+01  6.110e+01  6.103e+01
  2.300e+00  5.842e+01  5.840e+01  5.835e+01  5.838e+01  5.835e+01
  2.400e+00  5.203e+01  5.203e+01  5.204e+01  5.204e+01  5.204e+01
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
    plt.title('BOTFLUX aerosols')
    plt.legend()
    plt.grid(True)
    plt.show()

# Datos de ejemplo (misma cadena que antes)
data_1 = """
  3.000e-01  3.632e+02  3.632e+02  3.632e+02  3.632e+02  3.632e+02
  4.000e-01  1.228e+03  1.236e+03  1.253e+03  1.242e+03  1.255e+03
  5.000e-01  1.548e+03  1.555e+03  1.571e+03  1.561e+03  1.572e+03
  6.000e-01  1.524e+03  1.530e+03  1.543e+03  1.535e+03  1.544e+03
  7.000e-01  1.065e+03  1.064e+03  1.061e+03  1.063e+03  1.061e+03
  8.000e-01  6.829e+02  6.780e+02  6.662e+02  6.737e+02  6.654e+02
  9.000e-01  6.866e+02  6.843e+02  6.789e+02  6.823e+02  6.785e+02
  1.000e+00  4.167e+02  4.127e+02  4.033e+02  4.093e+02  4.027e+02
  1.100e+00  4.663e+02  4.648e+02  4.613e+02  4.635e+02  4.611e+02
  1.200e+00  3.480e+02  3.463e+02  3.423e+02  3.449e+02  3.421e+02
  1.300e+00  3.137e+02  3.124e+02  3.092e+02  3.112e+02  3.090e+02
  1.400e+00  3.540e+02  3.540e+02  3.542e+02  3.541e+02  3.542e+02
  1.500e+00  2.559e+02  2.556e+02  2.549e+02  2.554e+02  2.549e+02
  1.600e+00  1.755e+02  1.749e+02  1.735e+02  1.744e+02  1.734e+02
  1.700e+00  1.514e+02  1.510e+02  1.499e+02  1.506e+02  1.498e+02
  1.800e+00  1.691e+02  1.691e+02  1.691e+02  1.691e+02  1.691e+02
  1.900e+00  1.352e+02  1.352e+02  1.353e+02  1.352e+02  1.353e+02
  2.000e+00  1.158e+02  1.158e+02  1.159e+02  1.159e+02  1.159e+02
  2.100e+00  8.119e+01  8.114e+01  8.104e+01  8.110e+01  8.103e+01
  2.200e+00  6.118e+01  6.114e+01  6.103e+01  6.110e+01  6.103e+01
  2.300e+00  5.842e+01  5.840e+01  5.835e+01  5.838e+01  5.835e+01
  2.400e+00  5.203e+01  5.203e+01  5.204e+01  5.204e+01  5.204e+01
"""

# Usar la función para graficar los datos con interpolación
plot_interpolation(data_1)