import numpy as np

class Eslabon:
    def __init__(self, phi, rho, theta, x=0, y=0, z=0):
        """
        Inicializa un eslabón con ángulos de rotación y posición.
        
        Parámetros:
        phi (float): Ángulo de rotación alrededor del eje Y (en grados).
        rho (float): Ángulo de rotación alrededor del eje Z (en grados).
        theta (float): Ángulo de rotación alrededor del eje X (en grados).
        x, y, z (float): Posición del origen del marco de referencia.
        """
        # Convertir grados a radianes
        self.phi = np.radians(phi)
        self.rho = np.radians(rho)
        self.theta = np.radians(theta)
        self.x = x
        self.y = y
        self.z = z
        # Calcular la matriz homogénea utilizando los ángulos en radianes
        self.matriz = self.matriz_homogenea(self.rho, self.phi, self.theta, x, y, z)

    def __str__(self):
        return f"Eslabon(phi={np.degrees(self.phi):.2f}°, rho={np.degrees(self.rho):.2f}°, theta={np.degrees(self.theta):.2f}°, x={self.x}, y={self.y}, z={self.z})"

    @staticmethod
    def matriz_homogenea(rho, phi, theta, x=0, y=0, z=0):
        """
        Crea una matriz homogénea de transformación 3D usando rotaciones ZYX.

        Parámetros:
        rho (float): Ángulo de rotación alrededor del eje Z (en radianes).
        phi (float): Ángulo de rotación alrededor del eje Y (en radianes).
        theta (float): Ángulo de rotación alrededor del eje X (en radianes).
        x, y, z (float): Traslación en los ejes X, Y, Z.

        Retorna:
        numpy.ndarray: Matriz homogénea de transformación 4x4.
        """
        # Matriz de rotación en orden Z-Y-X (rho-phi-theta)
        # Equivalente a R = Rz(rho) * Ry(phi) * Rx(theta)
        R = np.array([
            [np.cos(rho) * np.cos(phi), np.cos(rho) * np.sin(phi) * np.sin(theta) - np.sin(rho) * np.cos(theta), np.cos(rho) * np.sin(phi) * np.cos(theta) + np.sin(rho) * np.sin(theta)],
            [np.sin(rho) * np.cos(phi), np.sin(rho) * np.sin(phi) * np.sin(theta) + np.cos(rho) * np.cos(theta), np.sin(rho) * np.sin(phi) * np.cos(theta) - np.cos(rho) * np.sin(theta)],
            [-np.sin(phi), np.cos(phi) * np.sin(theta), np.cos(phi) * np.cos(theta)]
        ])
        
        # Construcción de la matriz homogénea completa
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = [x, y, z]
        
        return T

    def unit_vect(self):
        """
        Devuelve los vectores unitarios X, Y, Z del marco de referencia.
        """
        Xvect = self.matriz[:3, 0]
        Yvect = self.matriz[:3, 1]
        Zvect = self.matriz[:3, 2]
        return Xvect, Yvect, Zvect

    def frame_position(self):
        """
        Devuelve la posición del origen del marco de referencia.
        """
        return self.matriz[:3, 3]

    def __matmul__(self, other):
        """
        Sobrecarga del operador @ para componer transformaciones.
        La operación es self @ other, lo que significa que primero se aplica other y luego self.
        """
        if not isinstance(other, Eslabon):
            raise ValueError("El operando debe ser una instancia de Eslabon")
        
        # La multiplicación de matrices representa la composición de transformaciones
        nueva_matriz = self.matriz @ other.matriz
        
        # Extraer los parámetros de la nueva matriz para crear un nuevo eslabón
        x, y, z = nueva_matriz[:3, 3]
        
        # Extraer ángulos de Euler de la matriz de rotación (orden ZYX)
        # NOTA: Este método puede tener problemas con la singularidad (gimbal lock)
        phi = np.arcsin(-nueva_matriz[2, 0])
        
        # Caso especial para evitar divisiones por cero cerca de la singularidad
        if np.abs(np.cos(phi)) > 1e-10:
            rho = np.arctan2(nueva_matriz[1, 0], nueva_matriz[0, 0])
            theta = np.arctan2(nueva_matriz[2, 1], nueva_matriz[2, 2])
        else:
            # En caso de singularidad (gimbal lock)
            # Hay infinitas soluciones, así que fijamos rho en 0
            rho = 0
            theta = np.arctan2(-nueva_matriz[0, 1], nueva_matriz[1, 1])
            
        return Eslabon(np.degrees(phi), np.degrees(rho), np.degrees(theta), x, y, z)

# Prueba del código
if __name__ == "__main__":
    eslabon1 = Eslabon(30, 45, 60, 1, 2, 3)
    eslabon2 = Eslabon(15, 30, 45, 4, 5, 6)
    
    # Componer transformaciones
    eslabon3 = eslabon1 @ eslabon2
    
    print("Eslabon 1:", eslabon1)
    print("Matriz 1:\n", eslabon1.matriz)
    print("\nEslabon 2:", eslabon2)
    print("Matriz 2:\n", eslabon2.matriz)
    print("\nEslabon 3 (resultado de eslabon1 @ eslabon2):", eslabon3)
    print("Matriz 3:\n", eslabon3.matriz)
    
    # Verificar la composición de manera alternativa
    matriz_compuesta = eslabon1.matriz @ eslabon2.matriz
    print("\nMatriz compuesta directamente:\n", matriz_compuesta)
    print("¿Son iguales las matrices?: ", np.allclose(eslabon3.matriz, matriz_compuesta))