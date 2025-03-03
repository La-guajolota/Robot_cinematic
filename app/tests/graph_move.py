#import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

def plot_3d_points_and_vectors(points, vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot points
    for point in points:
        ax.scatter(point[0], point[1], point[2], color='b')

    # Plot vectors
    for vector in vectors:
        start, direction = vector
        ax.quiver(start[0], start[1], start[2], direction[0], direction[1], direction[2], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def plot_3d_points_and_vectors_by_angle(points, vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])

    # Plot points
    for point in points:
        ax.scatter(point[0], point[1], point[2], color='b')

    # Plot vectors
    for vector in vectors:
        start, magnitude, angles = vector
        theta, phi = angles
        direction = [
            magnitude * np.sin(theta) * np.cos(phi),
            magnitude * np.sin(theta) * np.sin(phi),
            magnitude * np.cos(theta)
        ]
        ax.quiver(start[0], start[1], start[2], direction[0], direction[1], direction[2], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Example usage
points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
vectors = [((1, 2, 3), (1, 0, 0)), ((4, 5, 6), (0, 1, 0)), ((7, 8, 9), (0, 0, 1))]
vectors_by_angle = [((1, 2, 3), 1, (np.pi/4, np.pi/4)), ((4, 5, 6), 1, (np.pi/2, np.pi/4)), ((7, 8, 9), 1, (np.pi/3, np.pi/4))]

#plot_3d_points_and_vectors(points, vectors)
plot_3d_points_and_vectors_by_angle(points, vectors_by_angle)