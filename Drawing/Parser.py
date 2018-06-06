import json
import re

from Drawing.Screen import Screen
from Figures.Point import Point
from Figures.Circle import Circle
from Figures.Rectangle import Rectangle
from Figures.Polygon import Polygon
from Figures.Square import Square

def parse_key(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None

def parse_color(color, palette):

    if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
        return color

    elif re.match('\([0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\)', color):
        color = eval('(' + color + ')')
        color = '#%02x%02x%02x' % color
        return color

    elif color in palette:
        return palette[color]

    else:
        return None


class Parser:
    def __init__(self, path):
        json_file = open(path)
        self.dict = json.load(json_file)
        json_file.close()

        self.colors_pallete = self.get_palette()
        self.screen_properties = self.get_screen()
        self.all_figures = self.get_figures()

    def get_palette(self):
        palette = parse_key(self.dict, "Palette")
        res = {}
        for key, value in palette.items():
            color = parse_color(value, palette)
            res[key] = color

        return res

    def get_screen(self):
        screen = parse_key(self.dict, "Screen")

        width = parse_key(screen, "width")
        height = parse_key(screen, "height")

        bg_color = parse_key(screen, "bg_color")
        if bg_color not in self.colors_pallete:
            bg_color = parse_color(bg_color, self.colors_pallete)

        fg_color = parse_key(screen, "fg_color")
        if fg_color not in self.colors_pallete:
            fg_color = parse_color(fg_color, self.colors_pallete)

        return Screen(width, height, bg_color, fg_color)

    def get_figures(self):
        figures = parse_key(self.dict, "Figures")
        res = []

        for figure in figures:
            obj = None
            type = parse_key(figure, "type")
            if (type == "point"):
                obj = Point.set_point(figure, self.colors_pallete)
            if (type == "polygon"):
                obj = Polygon.set_polygon(figure, self.colors_pallete)
            if (type == "rectangle"):
                obj = Rectangle.set_rectangle(figure, self.colors_pallete)
            if (type == "circle"):
                obj = Circle.set_circle(figure, self.colors_pallete)
            if (type == "square"):
                obj = Square.set_square(figure, self.colors_pallete)

            if obj:
                res += [obj]
            else:
                print("Unknown figure name: " + type)
        return res

    def check_input(filepath):

        mode = 'r'
        regex = '.+(\.json)'

        match = re.match(regex, filepath)
        if not match:
            print("'{}' incorrect file type - file must be <sample>.json".format(filepath))
            return False
        try:
            file = open(filepath, mode)
            file.close()
        except OSError:
            print("'{}' incorrect filepath.".format(filepath))
            return False

        return True

    def check_output(filepath):
        mode = 'w'
        regex = '.+(\.png)'

        match = re.match(regex, filepath)
        if not match:
            print("'{}' incorrect file type - file must be <sample>.png".format(filepath))
            return False
        try:
            file = open(filepath, mode)
            file.close()
        except OSError:
            print("'{}' is incorrect filepath.".format(filepath))
            return False

        return True