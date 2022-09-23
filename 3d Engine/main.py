import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]  # x, y

angle = 0

points = []

# all the cube vertices
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j, points):
    pygame.draw.line(
        screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

def Rotate_Z():
    i = 0
    for point in points:
        # if pressed X, rotate around X axis
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1

def Rotate_Y():
    i = 0
    for point in points:
        # if pressed X, rotate around X axis
        rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1

def Rotate_X():
    i = 0
    for point in points:
        # if pressed X, rotate around X axis
        rotated2d = np.dot(rotation_x, point.reshape((3, 1)))
        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1

clock = pygame.time.Clock()
while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # update stuff

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])
    
    screen.fill(WHITE)
    # if pressed X, rotate around X axis
    X_pressed = pygame.key.get_pressed()[pygame.K_x]
    Y_pressed = pygame.key.get_pressed()[pygame.K_y]
    Z_pressed = pygame.key.get_pressed()[pygame.K_z]
    controls = [X_pressed, Y_pressed, Z_pressed]

    if controls == [True, False, False]:
        Rotate_X()
        angle += 0.01
    elif controls == [False, True, False]:
        Rotate_Y()
        angle += 0.01
    elif controls == [False, False, True]:
        Rotate_Z()
        angle += 0.01
    elif controls == [True, True, False]:
        Rotate_X()
        Rotate_Y()
        angle += 0.01
    elif controls == [True, False, True]:
        Rotate_X()
        Rotate_Z()
        angle += 0.01
    elif controls == [False, True, True]:
        Rotate_Y()
        Rotate_Z()
        angle += 0.01
    elif controls == [True, True, True]:
        Rotate_X()
        Rotate_Y()
        Rotate_Z()
        angle += 0.01
    else:
        pass
    


    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    pygame.display.update()