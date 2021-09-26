from .rectangle import Rectangle

class Square(Rectangle):
    "Класс 'Квадрат'"

    NAME = "Квадрат"

    def __init__(self, side, color):
        self.side = side
        super().__init__(self.side, self.side, color)

    def __repr__(self):
        return f"{self.color.color_prop} {self.NAME} со стороной {self.side} имеет площадь {self.square():.2f}"

    @property
    def get_name(self):
        return self.NAME