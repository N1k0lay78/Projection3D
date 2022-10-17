import pygame as pg
from matrix import *


class Point:
    def __init__(self, app, pos):
        self.app = app
        self.point = np.array([*pos, 1])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        point = self.point @ self.app.camera.camera_matrix()
        point = point @ self.app.projection.projection_matrix
        point = point @ self.app.projection.to_screen_matrix
        point = point[:2]

        print(point)
        pg.draw.circle(self.app.screen, pg.Color('white'), point, 6)

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
