class FigureColor:
    "Класс для свойства 'Цвет фигуры'"

    def __init__(self):
        self._color = None

    @property
    def color_prop(self):
        return self._color

    @color_prop.setter
    def set_color(self, value):
        self._color = value