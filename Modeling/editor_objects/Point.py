import pygame as pg
from Modeling.editor_objects.Base import Base


class Point(Base):
    def __init__(self, app, name, pos=[-1, -1, -1]):
        super().__init__(app, name, 'point')
        self.__x = pos[0]
        self.__y = pos[1]
        # print(pos[1] != -1, self.y)
        self.__y_is_fixed = pos[1] != -1
        self.__z = pos[2]
        self.__z_is_fixed = pos[2] != -1

    def draw_object(self):
        x0, y0 = self.app.zero_point
        if self.xy:
            print("1", self.xy)
            self.app.screen.blit(self.app.textures[1], (x0 - 9 - self.x * 16, y0 - 9 + self.y * 16))
        if self.xz:
            print("2", self.xz)
            self.app.screen.blit(self.app.textures[1], (x0 - 9 - self.x * 16, y0 - 9 - self.z * 16))

    def draw_name(self):
        x0, y0 = self.app.zero_point
        if self.xy:
            self.app.screen.blit(self.app.font_h.render(self.obj_name, True, (0, 0, 255)),
                             (x0 + 6 - self.x * 16, y0 - 30 + self.y * 16))
        if self.xz:
            self.app.screen.blit(self.app.font_h.render(self.obj_name, True, (0, 255, 0)),
                             (x0 + 6 - self.x * 16, y0 - 30 - self.z * 16))

    def draw_indexes(self):
        x0, y0 = self.app.zero_point
        if self.xy:
            self.app.screen.blit(self.app.font_l.render("1", True, (0, 0, 255)),
                             (x0 + 21 - self.x * 16, y0 - 19 + self.y * 16))
        if self.xz:
            self.app.screen.blit(self.app.font_l.render("2", True, (0, 255, 0)),
                             (x0 + 21 - self.x * 16, y0 - 19 - self.z * 16))

    def draw_coordinate(self):
        x0, y0 = self.app.zero_point
        if self.xy:
            text = self.app.font_m.render(f"({self.x}, {self.y})", True, (0, 0, 255))
            self.app.screen.blit(text, (x0 - text.get_width()//2 - self.x * 16, y0 + 5 + self.y * 16))
        if self.xz:
            text = self.app.font_m.render(f"({self.x}, {self.z})", True, (0, 255, 0))
            self.app.screen.blit(text, (x0 - text.get_width()//2 - self.x * 16, y0 + 5 - self.z * 16))

    def __getattr__(self, item):
        # Проекции на плоскость может не быть, если её ещё не задали
        if item == "x":
            if self.__x != -1:
                return self.__x
            else:
                return None
        elif item == "y":
            if self.__y != -1:
                return self.__y
            else:
                return None
        elif item == "z":
            if self.__z != -1:
                return self.__z
            else:
                return None
        elif item == "xy":
            if self.__y != -1:
                return self.__x, self.__y
            else:
                return None
        elif item == "xz":
            if self.__z != -1:
                return self.__x, self.__z
            else:
                return None

    def drafting_update(self, event):
        if event.type == pg.MOUSEMOTION:
            if not self.__y_is_fixed and not self.__z_is_fixed:
                self.__x = round((self.app.zero_point[0] - event.pos[0]) / 16, 2)
            if event.pos[1] >= self.app.zero_point[1] and not self.__y_is_fixed:
                self.__y = round((event.pos[1] - self.app.zero_point[1]) / 16, 2)
                # print(self.y)
                if not self.__z_is_fixed:
                    self.__z = -1
            elif event.pos[1] <= self.app.zero_point[1] and not self.__z_is_fixed:
                if not self.__y_is_fixed:
                    self.__y = -1
                self.__z = round((self.app.zero_point[1] - event.pos[1]) / 16, 2)
        # print(self.xy, self.xz)
        if event.type == pg.MOUSEBUTTONUP:
            if not self.__y_is_fixed and self.__y != -1:
                self.__y_is_fixed = True
            elif not self.__z_is_fixed and self.__z != -1:
                self.__z_is_fixed = True
            if self.__y_is_fixed and self.__z_is_fixed:
                self.set_object_ready()
        return self.is_object_ready()
