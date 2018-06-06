from Drawing import Parser


class Polygon:
    def __init__(self, points, color=None):
        self.points = points
        self.color = color
        self.__name__ = "Polygon"

    def __str__(self):
        return self.__name__ + ": Points: {}, color = {}".format(self.points, self.color)

    def set_polygon(properties, palette):
        points = Parser.parse_key(properties, "points")
        color = Parser.parse_key(properties, "color")
        if color:
            color = Parser.parse_color(color, palette)
            return Polygon(points, color)

        return Polygon(points)