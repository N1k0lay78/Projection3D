class Base:
    def __init__(self, x, y=-1, z=-1):
        self.__x = x
        self.__y = y
        self.__z = z

    def __getattr__(self, item):
        # Проекции на плоскость может не быть, если её ещё не задали
        if item == "x":
            return self.__x
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
