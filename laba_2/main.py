#!/usr/bin/python3
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pandas as pd

N = 20

def main():
    r = Rectangle(N, N, "Синий")
    c = Circle(N, "Зеленый")
    s = Square(N, "Красный")
    print(r)
    print(c)
    print(s)
    print()

    data = [
            [r.get_name, N, N, '-', r.color.color_prop, f"{r.square():.2f}"],
            [c.get_name, '-', '-', N, c.color.color_prop, f"{c.square():.2f}"],
            [s.get_name, N, N, '-', s.color.color_prop, f"{s.square():.2f}"]
    ]
    columns = ["Фигура", "Ширина", "Высота", "Радиус", "Цвет", "Площадь"]

    tab = pd.DataFrame(data, columns=columns)
    print(tab)

if __name__ == "__main__":
    main()