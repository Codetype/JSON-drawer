from Drawing import Parser


class Square:
    def __init__(self, x, y, size, color=None):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.__name__ = "Square"

    def __str__(self):
        return self.__name__ + ": Point({},{}), size = {}, color = {}".format(self.x, self.y, self.size, self.color)

    def set_square(properties, palette):
        x = Parser.parse_key(properties, "x")
        y = Parser.parse_key(properties, "y")
        size = Parser.parse_key(properties, "size")
        color = Parser.parse_key(properties, "color")
        if color:
            color = Parser.parse_color(color, palette)
            return Square(x, y, size, color)

        return Square(x, y, size)

