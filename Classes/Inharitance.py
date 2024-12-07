# Создайте базовый класс Shape, который:
# Содержит метод area, возвращающий 0.
# Содержит метод perimeter, возвращающий 0.
# Создайте классы-наследники Rectangle и Circle:
# Rectangle принимает ширину и высоту и реализует методы area и perimeter.
# Circle принимает радиус и реализует методы area и perimeter.
# Создайте список из нескольких объектов этих классов, затем пройдитесь по нему и
# вызовите area и perimeter для каждого объекта.
import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(5, 4)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(5)
print(circle.area())
print(circle.perimeter())
