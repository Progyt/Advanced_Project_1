# ARF SW
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Flujos sin aerosoles 
TOPFLUX_NOAOD = 771.8881029460798
BOTFLUX_NOAOD = 1002.6085882709475
Delta_NOaerosols = BOTFLUX_NOAOD - TOPFLUX_NOAOD



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

# Función para realizar la interpolación lineal para cada columna e integrar
def integrate_w_m2_um(um, w_m2_um):
    integrals = []
    for i in range(w_m2_um.shape[1]):
        interp_func = interp1d(um, w_m2_um[:, i], kind='linear', fill_value="extrapolate")
        integral, _ = quad(interp_func, min(um), max(um))
        integrals.append(integral)
    return integrals

# Función para graficar datos con interpolación lineal
def plot_interpolation(um, w_m2_um):
    x_new = np.linspace(min(um), max(um), 500)
    plt.figure(figsize=(12, 8))
    for i in range(w_m2_um.shape[1]):
        interp_func = interp1d(um, w_m2_um[:, i], kind='linear', fill_value="extrapolate")
        y_new = interp_func(x_new)
        plt.plot(um, w_m2_um[:, i], 'o', label=f'Datos {i+1}')
        plt.plot(x_new, y_new, '-', label=f'Interpolación {i+1}')
    plt.xlabel('Um (µm)')
    plt.ylabel('W/m^2/µm')
    plt.title('Interpolación lineal de los datos')
    plt.legend()
    plt.grid(True)
    plt.show()

# Datos
TOPFLUX = """
  3.000e-01  1.669e+01  1.549e+01  1.434e+01  1.324e+01  1.221e+01  1.124e+01
  4.000e-01  1.326e+03  1.270e+03  1.213e+03  1.155e+03  1.099e+03  1.043e+03
  5.000e-01  1.608e+03  1.559e+03  1.507e+03  1.452e+03  1.395e+03  1.339e+03
  6.000e-01  1.492e+03  1.453e+03  1.411e+03  1.367e+03  1.321e+03  1.276e+03
  7.000e-01  8.693e+02  8.574e+02  8.417e+02  8.235e+02  8.038e+02  7.828e+02
  8.000e-01  5.158e+02  5.140e+02  5.094e+02  5.028e+02  4.946e+02  4.856e+02
  9.000e-01  2.945e+02  2.911e+02  2.868e+02  2.820e+02  2.766e+02  2.710e+02
  1.000e+00  3.411e+02  3.400e+02  3.375e+02  3.339e+02  3.296e+02  3.247e+02
  1.100e+00  2.025e+02  2.001e+02  1.973e+02  1.943e+02  1.910e+02  1.876e+02
  1.200e+00  2.075e+02  2.058e+02  2.036e+02  2.011e+02  1.984e+02  1.955e+02
  1.300e+00  1.977e+02  1.959e+02  1.939e+02  1.916e+02  1.891e+02  1.865e+02
  1.400e+00  7.045e-02  6.807e-02  6.578e-02  6.356e-02  6.142e-02  5.934e-02
  1.500e+00  1.579e+02  1.560e+02  1.541e+02  1.520e+02  1.499e+02  1.478e+02
  1.600e+00  1.434e+02  1.424e+02  1.412e+02  1.400e+02  1.387e+02  1.374e+02
  1.700e+00  1.275e+02  1.268e+02  1.260e+02  1.251e+02  1.242e+02  1.232e+02
  1.800e+00  1.529e+01  1.510e+01  1.491e+01  1.472e+01  1.453e+01  1.435e+01
  1.900e+00  3.213e-04  3.149e-04  3.086e-04  3.024e-04  2.964e-04  2.905e-04
  2.000e+00  3.927e+01  3.900e+01  3.873e+01  3.846e+01  3.818e+01  3.791e+01
  2.100e+00  6.520e+01  6.491e+01  6.460e+01  6.429e+01  6.397e+01  6.364e+01
  2.200e+00  4.693e+01  4.673e+01  4.652e+01  4.630e+01  4.608e+01  4.585e+01
  2.300e+00  4.576e+01  4.554e+01  4.532e+01  4.509e+01  4.486e+01  4.463e+01
  2.400e+00  2.959e+01  2.941e+01  2.924e+01  2.906e+01  2.888e+01  2.870e+01
"""

BOTFLUX = """
  3.000e-01  3.633e+02  3.633e+02  3.633e+02  3.632e+02  3.632e+02  3.632e+02
  4.000e-01  1.326e+03  1.300e+03  1.276e+03  1.252e+03  1.230e+03  1.210e+03
  5.000e-01  1.627e+03  1.610e+03  1.591e+03  1.570e+03  1.550e+03  1.531e+03
  6.000e-01  1.589e+03  1.575e+03  1.559e+03  1.543e+03  1.526e+03  1.509e+03
  7.000e-01  1.040e+03  1.050e+03  1.057e+03  1.061e+03  1.064e+03  1.067e+03
  8.000e-01  6.122e+02  6.329e+02  6.509e+02  6.670e+02  6.815e+02  6.948e+02
  9.000e-01  6.543e+02  6.635e+02  6.718e+02  6.792e+02  6.860e+02  6.921e+02
  1.000e+00  3.623e+02  3.775e+02  3.912e+02  4.039e+02  4.156e+02  4.265e+02
  1.100e+00  4.462e+02  4.518e+02  4.569e+02  4.615e+02  4.659e+02  4.699e+02
  1.200e+00  3.255e+02  3.316e+02  3.373e+02  3.426e+02  3.475e+02  3.521e+02
  1.300e+00  2.961e+02  3.009e+02  3.053e+02  3.094e+02  3.133e+02  3.169e+02
  1.400e+00  3.549e+02  3.546e+02  3.544e+02  3.542e+02  3.540e+02  3.538e+02
  1.500e+00  2.518e+02  2.529e+02  2.540e+02  2.550e+02  2.558e+02  2.567e+02
  1.600e+00  1.676e+02  1.697e+02  1.717e+02  1.736e+02  1.754e+02  1.771e+02
  1.700e+00  1.455e+02  1.471e+02  1.486e+02  1.500e+02  1.513e+02  1.526e+02
  1.800e+00  1.693e+02  1.693e+02  1.692e+02  1.691e+02  1.691e+02  1.690e+02
  1.900e+00  1.354e+02  1.353e+02  1.353e+02  1.353e+02  1.352e+02  1.352e+02
  2.000e+00  1.159e+02  1.159e+02  1.159e+02  1.159e+02  1.158e+02  1.158e+02
  2.100e+00  8.061e+01  8.076e+01  8.091e+01  8.104e+01  8.117e+01  8.130e+01
  2.200e+00  6.062e+01  6.077e+01  6.091e+01  6.104e+01  6.117e+01  6.129e+01
  2.300e+00  5.815e+01  5.822e+01  5.829e+01  5.835e+01  5.841e+01  5.847e+01
  2.400e+00  5.207e+01  5.206e+01  5.205e+01  5.204e+01  5.203e+01  5.202e+01
"""

# Calcular las integrales e imprimir los resultados
um_top, w_m2_um_top = parse_and_interpolate(TOPFLUX)
um_bot, w_m2_um_bot = parse_and_interpolate(BOTFLUX)

integrales_top = integrate_w_m2_um(um_top, w_m2_um_top)
integrales_bot = integrate_w_m2_um(um_bot, w_m2_um_bot)

print("Integrales TOPFLUX:", integrales_top)
print("Integrales BOTFLUX:", integrales_bot)

# Graficar las interpolaciones
#plot_interpolation(um_top, w_m2_um_top)
#plot_interpolation(um_bot, w_m2_um_bot)

DeltaFlux = []
for i in range (0, len(integrales_top)):
    DeltaFlux.append(integrales_bot[i] - integrales_top[i] - Delta_NOaerosols)


print(DeltaFlux)
