from Drawing import Parser

def set_circle(properties, palette):
    x = Parser.parse_key(properties, "x")
    y = Parser.parse_key(properties, "y")
    radius = Parser.parse_key(properties, "radius")
    color = Parser.parse_key(properties, "color")
    if color:
        color = Parser.parse_color(color, palette)
        return Circle(x, y, radius, color)

    return Circle(x, y, color)

class Circle:
    def __init__(self, x, y, radius, color=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.__name__ = "Circle"

    def __str__(self):
        return self.__name__ + ": Point({},{}), radius = {}, color = {}".format(self.x, self.y, self.radius, self.color)

    def set_circle(properties, palette):
        x = Parser.parse_key(properties, "x")
        y = Parser.parse_key(properties, "y")
        radius = Parser.parse_key(properties, "radius")
        color = Parser.parse_key(properties, "color")
        if color:
            color = Parser.parse_color(color, palette)
            return Circle(x, y, radius, color)

        return Circle(x,y,color)