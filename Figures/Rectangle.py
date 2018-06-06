from Drawing import Parser


class Rectangle:
    def __init__(self, x, y, width, height, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.__name__ = "Rectangle"

    def __str__(self):
        return self.__name__ + ": Point({},{}), width = {}, height = {}, color = {}".format(self.x, self.y, self.width, self.height, self.color)

    def set_rectangle(properties, palette):
        x = Parser.parse_key(properties, "x")
        y = Parser.parse_key(properties, "y")
        height = Parser.parse_key(properties, "height")
        width = Parser.parse_key(properties, "width")
        color = Parser.parse_key(properties, "color")
        if color:
            color = Parser.parse_color(color, palette)
            return Rectangle(x, y, width, height, color)

        return Rectangle(x, y, width, height)