import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def extender_linea(punto1, punto2, longitud_total):
    """
    Calcula un tercer punto extendiendo la línea que pasa por punto1 y punto2,
    de manera que la distancia desde punto1 hasta el punto3 sea igual a longitud_total.
    
    Args:
        punto1: Coordenadas del primer punto (x1, y1, z1)
        punto2: Coordenadas del segundo punto (x2, y2, z2)
        longitud_total: Distancia deseada desde punto1 hasta punto3
        
    Returns:
        punto3: Coordenadas del tercer punto calculado
    """
    # Convertir a arrays de numpy
    p1 = np.array(punto1)
    p2 = np.array(punto2)
    
    # Calcular el vector de dirección
    vector = p2 - p1
    
    # Calcular la distancia actual entre p1 y p2
    distancia_actual = np.linalg.norm(vector)
    
    # Normalizar el vector (convertirlo en vector unitario)
    vector_unitario = vector / distancia_actual
    
    # Calcular el punto3 usando la longitud total deseada
    punto3 = p1 + vector_unitario * longitud_total
    
    return punto3

def visualizar_linea(punto1, punto2, punto3):
    """
    Visualiza los tres puntos y las líneas que los conectan en un gráfico 3D.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extraer coordenadas
    x = [punto1[0], punto2[0], punto3[0]]
    y = [punto1[1], punto2[1], punto3[1]]
    z = [punto1[2], punto2[2], punto3[2]]
    
    # Dibujar los puntos
    ax.scatter(x, y, z, color=['red', 'green', 'blue'], s=100)
    
    # Dibujar las líneas
    ax.plot([punto1[0], punto2[0]], [punto1[1], punto2[1]], [punto1[2], punto2[2]], 'gray')
    ax.plot([punto2[0], punto3[0]], [punto2[1], punto3[1]], [punto2[2], punto3[2]], 'gray', linestyle='--')
    
    # Etiquetar los puntos
    ax.text(punto1[0], punto1[1], punto1[2], "Punto 1", color='red')
    ax.text(punto2[0], punto2[1], punto2[2], "Punto 2", color='green')
    ax.text(punto3[0], punto3[1], punto3[2], "Punto 3", color='blue')
    
    # Configurar los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Extensión de línea en 3D')
    
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Definir dos puntos en el espacio 3D
    punto1 = (1, 2, 3)
    punto2 = (4, 5, 6)
    
    # Longitud total deseada desde punto1 hasta punto3
    longitud_deseada = 10
    
    # Calcular el tercer punto
    punto3 = extender_linea(punto1, punto2, longitud_deseada)
    
    # Mostrar resultados
    print(f"Punto 1: {punto1}")
    print(f"Punto 2: {punto2}")
    print(f"Punto 3: {punto3}")
    
    # Verificar la distancia
    distancia_total = np.linalg.norm(np.array(punto3) - np.array(punto1))
    print(f"Distancia desde punto1 a punto3: {distancia_total}")
    
    # Visualizar los puntos y la línea
    visualizar_linea(punto1, punto2, punto3)