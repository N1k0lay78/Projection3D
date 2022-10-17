from math import ceil
import pygame as pg
import pygame.font
from loguru import logger
from Modeling.load_image import load_image


# TODO:1) сделать класс прямой, линии, создание линий
# TODO:2) сохранение в файл и загрузка из файла .obj и мб других
# TODO:3) отправка через сокеты
class AppModeling:
    def __init__(self):
        pg.init()
        # textures
        self.textures = []
        self.load_textures()
        self.font_h = pygame.font.Font("Source/Fonts/roboto.ttf", 24)
        self.font_l = pygame.font.Font("Source/Fonts/roboto.ttf", 12)
        # window
        self.size = self.w, self.h = 0, 0
        self.screen = None
        self.background = None
        self.zero_point = (0, 0)
        self.full_update_ui(64*10, 64*10)
        # app params
        self.running = True
        self.points = [[3, 3, 3], [10, 20, 15]]
        self.point_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lines = []
        self.line_names = self.point_names.lower()
        # settings
        # points
        self.print_points = True
        self.print_point_names = True
        self.print_plane_index = True
        # line
        # WIP
        self.print_lines = False
        self.print_line_name = False
        self.print_line_points = False

    def load_textures(self):
        logger.info(f'Load textures')
        self.textures = [load_image('instruments'), load_image('instruments').subsurface((128, 0, 17, 17))]

    def full_update_ui(self, w, h):
        logger.info(f'New video size ({w}, {h})')
        self.size = self.w, self.h = w, h
        self.zero_point = (self.w, 64 * ceil(h / 128) - 16)
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        self.background = pg.Surface((w, h))
        for i in range(ceil(h / 64)):
            for j in range(ceil(w / 64)):
                if j == 0:
                    self.background.blit(self.textures[0].subsurface((0, 64, 64, 64)), (j*64, i*64))
                elif j == 1:
                    if i == h // 64 // 2 - 1:
                        self.background.blit(self.textures[0].subsurface((64, 128, 64, 64)), (j * 64, i * 64))
                    else:
                        self.background.blit(self.textures[0].subsurface((64, 64, 64, 64)), (j * 64, i * 64))
                elif j == ceil(w / 64) - 1 and i == 0:
                    self.background.blit(self.textures[0].subsurface((0, 128, 64, 64)), (j * 64, i * 64))
                elif j == ceil(w / 64) - 1 and i == ceil(h / 64) - 1:
                    self.background.blit(self.textures[0].subsurface((0, 192, 64, 64)), (j * 64, i * 64))
                elif j == ceil(w / 64) - 1 and i == h // 64 // 2 - 1:
                    self.background.blit(self.textures[0].subsurface((64, 192, 64, 64)), (j * 64, i * 64))
                else:
                    self.background.blit(self.textures[0].subsurface((64, 0, 64, 64)), (j * 64, i * 64))

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                elif event.type == pg.VIDEORESIZE:
                    self.full_update_ui(event.w, event.h)
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        quit()
                    elif event.key == pg.K_r:
                        self.load_textures()
                        self.full_update_ui(*self.size)

            # self.screen.fill(pg.Color("#20394f"))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.textures[0].subsurface((0, 0, 64, 64)), (0, 0))
            for line in self.lines:
                pg.draw.aaline(self.screen, (255, 255, 255), self.points[line[0]][:2], self.points[line[1]][:2])
                pg.draw.aaline(self.screen, (255, 255, 255), self.points[line[0]][::2], self.points[line[1]][::2])
            if self.print_points:
                for i, point in enumerate(self.points):
                    self.screen.blit(self.textures[1],
                                     (self.zero_point[0] - 9 - point[0] * 16, self.zero_point[1] - 9 + point[1] * 16))
                    if self.print_point_names:
                        self.screen.blit(self.font_h.render(self.point_names[i], True, (0, 0, 255)),
                                         (self.zero_point[0] + 6 - point[0] * 16, self.zero_point[1] - 30 + point[1] * 16))
                        if self.print_plane_index:
                            self.screen.blit(self.font_l.render("1", True, (0, 0, 255)),
                                             (self.zero_point[0] + 21 - point[0] * 16, self.zero_point[1] - 19 + point[1] * 16))
                    self.screen.blit(self.textures[1],
                                     (self.zero_point[0] - 9 - point[0] * 16, self.zero_point[1] - 9 - point[2] * 16))
                    if self.print_point_names:
                        self.screen.blit(self.font_h.render(self.point_names[i], True, (0, 255, 0)),
                                         (self.zero_point[0] + 6 - point[0] * 16, self.zero_point[1] - 30 - point[2] * 16))
                        if self.print_plane_index:
                            self.screen.blit(self.font_l.render("2", True, (0, 255, 0)),
                                             (self.zero_point[0] + 21 - point[0] * 16, self.zero_point[1] - 19 - point[2] * 16))
            pg.display.update()


if __name__ == '__main__':
    AppModeling().run()