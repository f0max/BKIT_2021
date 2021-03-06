from .figure import Figure
from .color import FigureColor

class Rectangle(Figure):
    "Класс 'Прямоугольник'"

    NAME = "Прямоугольник"

    def __init__(self, width, height, color):
        self.widht = width
        self.height = height
        self.color = FigureColor()
        self.color.color_prop = color
    
    def square(self):
        return self.widht * self.height

    def __repr__(self):
        return f"{self.color.color_prop} {self.NAME} с шириной {self.widht} и высотой {self.height} имеет площадь {self.square():.2f}"

    @property
    def get_name(self):
        return self.NAME