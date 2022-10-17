import pygame as pg
from matrix import *


class Point:
    def __init__(self, app, pos):
        self.app = app
        self.point = np.array([[*pos, 1], [1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertices = self.point @ self.app.camera.camera_matrix()
        vertices = vertices @ self.app.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.app.projection.to_screen_matrix
        vertices = vertices[:, :2]
        print("ASDASDASD")
        for point in vertices:
            pg.draw.circle(self.app.screen, pg.Color('#ffffff'), point, 6)

    def translate(self, pos):
        self.point = self.point @ translate(pos)

    def scale(self, n):
        self.point = self.point @ scale(n)

    def rotate_x(self, a):
        self.point = self.point @ rotate_x(a)

    def rotate_y(self, a):
        self.point = self.point @ rotate_y(a)

    def rotate_z(self, a):
        self.point = self.point @ rotate_z(a)
