from .rectangle import Rectangle
from .color import FigureColor

class Square(Rectangle):
    "Класс 'Квадрат'"

    NAME = "Квадрат"

    def __init__(self, side, color):
        self.side = side
        self.color = FigureColor()
        self.color = color
        super().__init__(self.side, self.side, self.color)

    def __repr__(self):
        return f"{self.color} {self.NAME} со стороной {self.side} имеет площадь {self.square()}"

    @property
    def get_name(self):
        return self.NAME