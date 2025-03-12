from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def plot_3d_line(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    z_values = [point[2] for point in points]

    ax.plot(x_values, y_values, z_values, color='orange', marker='o', markerfacecolor='orange')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()

if __name__ == "__main__":
    points = [np.array([0, 0, 0]), np.array([1, 2, 3]), np.array([2, 3, 4]), np.array([3, 5, 7])]
    plot_3d_line(points)
