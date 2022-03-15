# Marco Antonio Alvarez Ramirez
# Clasico a lo Cuantico / CNYT /

import matplotlib.pyplot as plt
import NComplex as nc


# Los experimentos de la canicas con coeficiente booleanos (canicas)
# Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas. (probabilistico)
# Experimento de las múltiples rendijas cuántico. (cuantico)
# Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen. (barras)

def canicas(m, e, r):
    re = [0 for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            re[i] = re[i] + (m[i][j] * e[j])
    return canicas(m, re, r - 1) if r > 0 else re


def propabilistico(m, e, r):
    re = [0 for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            re[i] = re[i] + (m[i][j] * e[j])
    return propabilistico(m, re, r - 1) if r > 0 else re


def cuantico(m, e, r):
    re = [(0, 0) for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            re[i] = nc.sumacplx(re[i], (nc.producplx(m[i][j], e[j])))
    return propabilistico(m, re, r - 1) if r > 0 else re


def barras(eje_x, eje_y, z):
    plt.bar(eje_x, eje_y, color="Green")
    plt.ylabel('Probabilidad')
    plt.xlabel('Estado')
    plt.title(z)
    plt.show()