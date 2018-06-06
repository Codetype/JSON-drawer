import matplotlib.pyplot as plt

from Figures.Point import Point
from Figures.Circle import Circle
from Figures.Rectangle import Rectangle
from Figures.Polygon import Polygon
from Figures.Square import Square

def draw_figures(parsed_file, output_file, img_flag):
    objects_list = parsed_file.all_figures
    screen = parsed_file.screen_properties
    palette = parsed_file.colors_pallete

    size = plt.rcParams["figure.figsize"]
    size[1] = screen.height / 96
    size[0] = screen.width / 96

    plt.axes()
    ax = plt.gca()
    ax.set_facecolor(screen.bg_color)
    plt.axis([0, screen.width, 0, screen.height])

    for obj in objects_list:

        fig_color = obj.color
        if not fig_color:
            obj.color = screen.fg_color
        try:
            #print(obj)
            if isinstance(obj, Point):
                point = plt.Circle((obj.x, obj.y), radius=1, fc=obj.color)
                ax.add_patch(point)
            elif isinstance(obj, Circle):
                circle = plt.Circle((obj.x, obj.y), radius=obj.radius, fc = obj.color)
                ax.add_patch(circle)
            elif isinstance(obj, Square):
                square = plt.Rectangle((obj.x, obj.y), width=obj.size, height=obj.size , fc=obj.color)
                ax.add_patch(square)
            elif isinstance(obj, Rectangle):
                rectangle = plt.Rectangle((obj.x, obj.y), width=obj.width, height=obj.height , fc=obj.color)
                ax.add_patch(rectangle)
            elif isinstance(obj, Polygon):
                polygon = plt.Polygon(obj.points, fc=fig_color)
                ax.add_patch(polygon)
        except TypeError:
            print("Unresolved drawing error")

    if img_flag:
        plt.savefig(output_file)
    plt.show()