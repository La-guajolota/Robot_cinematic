import numpy as np

class Eslabon:
    def __init__(self, phi, rho, theta, x=0, y=0, z=0):
        self.rho = np.radians(rho)
        self.phi = np.radians(phi)
        self.theta = np.radians(theta)
        self.x = x
        self.y = y
        self.z = z
        self.matriz = self.matriz_homogenea(rho, phi, theta, x, y, z)

    def __str__(self):
        return f"Eslabon(rho={self.rho}, phi={self.phi}, theta={self.theta}, x={self.x}, y={self.y}, z={self.z})"

    @staticmethod
    def matriz_homogenea(rho=0, phi=0, theta=0, x=0, y=0, z=0):
        """
        Crea una matriz homogénea de transformación 3D.

        Parámetros:
        rho (float): Ángulo de rotación alrededor del eje Z (en radianes).
        phi (float): Ángulo de rotación alrededor del eje Y (en radianes).
        theta (float): Ángulo de rotación alrededor del eje X (en radianes).
        x (float): Traslación en el eje X.
        y (float): Traslación en el eje Y.
        z (float): Traslación en el eje Z.

        Retorna:
        numpy.ndarray: Matriz homogénea de transformación 4x4.
        """
        # Matriz de rotación y traslación
        T = np.array([
            [np.cos(rho) * np.cos(phi), np.cos(rho) * np.sin(phi) * np.sin(theta) - np.sin(rho) * np.cos(theta), np.cos(rho) * np.sin(phi) * np.cos(theta) + np.sin(rho) * np.sin(theta), x],
            [np.sin(rho) * np.cos(phi), np.sin(rho) * np.sin(phi) * np.sin(theta) + np.cos(rho) * np.cos(theta), np.sin(rho) * np.sin(phi) * np.cos(theta) - np.cos(rho) * np.sin(theta), y],
            [-np.sin(phi), np.cos(phi) * np.sin(theta), np.cos(phi) * np.cos(theta), z],
            [0, 0, 0, 1]
        ])
        return T

    def unit_vect(self):
        # Toma los vectores unitarios de las matrices homogéneas
        Xvect = self.matriz[:3, 0]
        Yvect = self.matriz[:3, 1]
        Zvect = self.matriz[:3, 2]
        return Xvect, Yvect, Zvect

    def frame_position(self):
        # Toma el vector posición
        frame_ptn = self.matriz[:3, 3]
        return frame_ptn

    def __matmul__(self, other):
        if not isinstance(other, Eslabon):
            raise ValueError("El operando debe ser una instancia de Eslabon")
        nueva_matriz = np.dot(other.matriz, self.matriz)
        # Extraer los parámetros de la nueva matriz
        x, y, z = nueva_matriz[:3, 3]
        rho = np.arctan2(nueva_matriz[1, 0], nueva_matriz[0, 0])
        phi = np.arcsin(-nueva_matriz[2, 0])
        theta = np.arctan2(nueva_matriz[2, 1], nueva_matriz[2, 2])
        return Eslabon(np.degrees(phi), np.degrees(rho), np.degrees(theta), x, y, z)
    

if __name__ == "__main__":
    eslabon1 = Eslabon(30, 45, 60, 1, 2, 3)
    eslabon2 = Eslabon(15, 30, 45, 4, 5, 6)
    
    eslabon3 = eslabon1 @ eslabon2
    
    print("Eslabon 1:", eslabon1)
    print("Eslabon 2:", eslabon2)
    print("Eslabon 3 (resultado de eslabon1 @ eslabon2):", eslabon3)