import numpy as np

# Representa una rotación pura
class Joint:
    def __init__(self, angle, eje='theta'):
        # angle in degrees and radians
        self.angle_deg = angle
        self.angle_rad = np.deg2rad(angle)

        # theta, phi, ro
        self.axis = eje  # default

        # Create the homogeneous rotation matrix
        if self.axis == 'theta':
            self.rotation_matrix = np.array([
            [np.cos(self.angle_rad), -np.sin(self.angle_rad), 0, 0],
            [np.sin(self.angle_rad), np.cos(self.angle_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ])  
        elif self.axis == 'phi':  
            self.rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(self.angle_rad), -np.sin(self.angle_rad), 0],
            [0, np.sin(self.angle_rad), np.cos(self.angle_rad), 0],
            [0, 0, 0, 1]
            ])
        elif self.axis == 'ro':
            self.rotation_matrix = np.array([
            [np.cos(self.angle_rad), 0, np.sin(self.angle_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(self.angle_rad), 0, np.cos(self.angle_rad), 0],
            [0, 0, 0, 1]
            ])

    def __repr__(self):
        return (f"Joint(angle={self.angle_deg:.2f} deg | {self.angle_rad:.2f} rad, axis={self.axis})\n"
            f"Rotation Matrix:\n{self.rotation_matrix}")

# Representa una traslación pura
class Link:
    def __init__(self, length, eje='theta'):
        self.length = length

        # Create the homogeneous translation matrix
        self.axis = eje  
        if self.axis == 'theta':
            self.translation_matrix = np.array([
            [1, 0, 0, self.length],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ])
        elif self.axis == 'phi':
            self.translation_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, self.length],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ])
        elif self.axis == 'ro':
            self.translation_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, self.length],
            [0, 0, 0, 1]
            ])

    def __repr__(self):
        return (f"Link(length={self.length}, axis={self.axis})\n"
            f"Translation Matrix:\n{self.translation_matrix}")


if __name__ == '__main__':
    # tests    
    J0 = Joint(45, 'theta')
    print(J0)
    print()

    L0 = Link(10, 'ro')
    print(L0)
    print()
