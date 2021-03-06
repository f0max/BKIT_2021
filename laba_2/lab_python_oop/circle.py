from .figure import Figure
from .color import FigureColor
from math import pi

class Circle(Figure):
    "Класс 'Круг'"

    NAME = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.color_prop = color

    def square(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return f"{self.color.color_prop} {self.NAME} с радиусом {self.radius} имеет площадь {self.square():.2f}"

    @property
    def get_name(self):
        return self.NAME