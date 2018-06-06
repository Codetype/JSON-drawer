from Drawing import Parser


class Point:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color
        self.__name__ = "Point"

    def __str__(self):
        return "Point({},{}), color = {}".format(self.x, self.y, self.color)

    def set_point(properties, palette):
        x = Parser.parse_key(properties, "x")
        y = Parser.parse_key(properties, "y")
        color = Parser.parse_key(properties, "color")
        if color:
            color = Parser.parse_color(color, palette)
            return Point(x, y, color)

        return Point(x, y)
