# Program: Translation, Rotation, and Scaling of a 2D Object
# Author: Puja Kumari
# Subject: Computer Graphics (BCA 5th Semester)

import matplotlib.pyplot as plt
import numpy as np

# Original square points
points = np.array([[1, 1],
                   [1, 3],
                   [3, 3],
                   [3, 1],
                   [1, 1]])

# Function to apply transformation
def transform(points, matrix):
    ones = np.ones((len(points), 1))
    homogenous = np.hstack([points, ones])
    transformed = homogenous @ matrix.T
    return transformed[:, :2]

# Translation matrix (tx=2, ty=1)
translation_matrix = np.array([[1, 0, 2],
                               [0, 1, 1],
                               [0, 0, 1]])

# Rotation matrix (theta=45°)
theta = np.radians(45)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]])

# Scaling matrix (sx=1.5, sy=0.5)
scaling_matrix = np.array([[1.5, 0, 0],
                           [0, 0.5, 0],
                           [0, 0, 1]])

translated = transform(points, translation_matrix)
rotated = transform(points, rotation_matrix)
scaled = transform(points, scaling_matrix)

# Plotting
plt.figure()
plt.plot(points[:, 0], points[:, 1], 'b-o', label='Original')
plt.plot(translated[:, 0], translated[:, 1], 'r-o', label='Translated')
plt.plot(rotated[:, 0], rotated[:, 1], 'g-o', label='Rotated')
plt.plot(scaled[:, 0], scaled[:, 1], 'm-o', label='Scaled')

plt.title("2D Transformations: Translation, Rotation, Scaling")
plt.legend()
plt.grid(True)
plt.show()
