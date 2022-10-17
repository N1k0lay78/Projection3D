from math import pi

import pygame as pg
from matrix import *
from camera import Camera
from projection import Projection
from point import Point


class app:
    def __init__(self):
        pg.init()
        self.size = self.w, self.h = 1920, 1080
        self.hw, self.hh = self.w / 2, self.h / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.objects = []
        self.create_object()

    def create_object(self):
        self.camera = Camera(self, (0.5, 1, -4))
        self.projection = Projection(self)
        self.objects.append(Point(self, (0, 0, 0)))
        self.objects[-1].translate([0.2, 0.4, 0.2])
        self.objects[-1].rotate_y(pi / 6)


    def draw(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects:
            obj.draw()

    def run(self):
        while True:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.VIDEORESIZE:
                    self.size = self.w, self.h = event.size[0], event.size[1]
                    self.H_WIDTH, self.H_HEIGH = self.w / 2, self.h / 2
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()


app().run()