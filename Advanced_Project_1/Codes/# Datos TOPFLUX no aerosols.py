# Datos TOPFLUX no aerosols
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Datos de ejemplo
data_1 = """
  3.000e-01  1.669e+01
  4.000e-01  1.326e+03
  5.000e-01  1.608e+03
  6.000e-01  1.492e+03
  7.000e-01  8.693e+02
  8.000e-01  5.158e+02
  9.000e-01  2.945e+02
  1.000e+00  3.411e+02
  1.100e+00  2.025e+02
  1.200e+00  2.075e+02
  1.300e+00  1.977e+02
  1.400e+00  7.045e-02
  1.500e+00  1.579e+02
  1.600e+00  1.434e+02
  1.700e+00  1.275e+02
  1.800e+00  1.529e+01
  1.900e+00  3.213e-04
  2.000e+00  3.927e+01
  2.100e+00  6.520e+01
  2.200e+00  4.693e+01
  2.300e+00  4.576e+01
  2.400e+00  2.959e+01
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
        interp_func = interp1d(um, w_m2_um[:, i], kind='linear', fill_value="extrapolate")
        y_new = interp_func(x_new)
        plt.plot(um, w_m2_um[:, i], 'o')
        plt.plot(x_new, y_new, '-')
    
    plt.xlabel('wavelenght (µm)')
    plt.ylabel('W/m^2/µm')
    plt.title('TOPFLUX no aerosols')
    plt.legend()
    plt.grid(True)
    plt.show()

# Datos de ejemplo (misma cadena que antes)
data_1 = """
  3.000e-01  1.669e+01
  4.000e-01  1.326e+03
  5.000e-01  1.608e+03
  6.000e-01  1.492e+03
  7.000e-01  8.693e+02
  8.000e-01  5.158e+02
  9.000e-01  2.945e+02
  1.000e+00  3.411e+02
  1.100e+00  2.025e+02
  1.200e+00  2.075e+02
  1.300e+00  1.977e+02
  1.400e+00  7.045e-02
  1.500e+00  1.579e+02
  1.600e+00  1.434e+02
  1.700e+00  1.275e+02
  1.800e+00  1.529e+01
  1.900e+00  3.213e-04
  2.000e+00  3.927e+01
  2.100e+00  6.520e+01
  2.200e+00  4.693e+01
  2.300e+00  4.576e+01
  2.400e+00  2.959e+01
"""

# Usar la función para graficar los datos con interpolación
plot_interpolation(data_1)
