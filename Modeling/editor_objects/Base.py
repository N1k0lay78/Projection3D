class Base:
    def __init__(self, app, name, type):
        self.app = app
        self.obj_name = name
        self.obj_type = type
        self.__ready = False

    def draw(self):
        if self.obj_type in self.app.draw_types:
            self.draw_object()
            if self.obj_type in self.app.draw_names:
                self.draw_name()
                if self.app.draw_plane_indexes:
                    self.draw_indexes()
            if self.obj_type in self.app.draw_coordinate:
                self.draw_coordinate()

    def set_object_ready(self):
        self.__ready = True

    def is_object_ready(self):
        return self.__ready

    def drafting_update(self, event):
        pass

    def __getattr__(self, item):
        return None

    def draw_object(self):
        pass

    def draw_name(self):
        pass

    def draw_indexes(self):
        pass
