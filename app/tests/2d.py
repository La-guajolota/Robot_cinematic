import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Longitudes iniciales de los eslabones
L1 = 2.4
L2 = 1.9

# Ángulos iniciales en grados
theta1 = 28.45  # 45 grados
theta2 = 49.78  # 45 grados

def calcular_puntos(theta1, theta2, L1, L2):
    """Calcula las posiciones de los eslabones dados los ángulos y longitudes"""
    theta1_rad = np.deg2rad(theta1)
    theta2_rad = np.deg2rad(theta2)
    x1, y1 = L1 * np.cos(theta1_rad), L1 * np.sin(theta1_rad)
    x2, y2 = x1 + L2 * np.cos(theta1_rad + theta2_rad), y1 + L2 * np.sin(theta1_rad + theta2_rad)
    return (0, 0), (x1, y1), (x2, y2)

def actualizar(val):
    """Actualiza la posición de los eslabones con los valores del slider"""
    theta1 = slider1.val
    theta2 = slider2.val
    L1 = sliderL1.val
    L2 = sliderL2.val
    p0, p1, p2 = calcular_puntos(theta1, theta2, L1, L2)
    linea.set_data([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]])
    texto.set_text(f'Punto final: ({p2[0]:.2f}, {p2[1]:.2f})')
    fig.canvas.draw_idle()

# Crear figura
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.grid(True)

# Dibujar el eslabón inicial
p0, p1, p2 = calcular_puntos(theta1, theta2, L1, L2)
linea, = ax.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], 'o-', markersize=8, lw=3)
texto = ax.text(-1.5, 1.8, f'Punto final: ({p2[0]:.2f}, {p2[1]:.2f})', fontsize=12)

# Sliders para ángulos
ax_slider1 = plt.axes([0.2, 0.2, 0.65, 0.03])
ax_slider2 = plt.axes([0.2, 0.15, 0.65, 0.03])
slider1 = Slider(ax_slider1, "Theta1", 0, 360, valinit=theta1)
slider2 = Slider(ax_slider2, "Theta2", 0, 360, valinit=theta2)

# Sliders para longitudes
ax_sliderL1 = plt.axes([0.2, 0.25, 0.65, 0.03])
ax_sliderL2 = plt.axes([0.2, 0.3, 0.65, 0.03])
sliderL1 = Slider(ax_sliderL1, "L1", 0.1, 2.0, valinit=L1)
sliderL2 = Slider(ax_sliderL2, "L2", 0.1, 2.0, valinit=L2)

# Conectar los sliders con la función de actualización
slider1.on_changed(actualizar)
slider2.on_changed(actualizar)
sliderL1.on_changed(actualizar)
sliderL2.on_changed(actualizar)

plt.show()
