class Screen:
    def __init__(self, width, height, bg_color, fg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color

    def __str__(self):
        return "width = {}, height = {}, bg_color = {}, fg_color = {}".format(self.width, self.height, self.bg_color, self.fg_color)
