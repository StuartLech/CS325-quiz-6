from abc import ABC, abstractmethod
from math import tan, pi

# Observer pattern interfaces, assuming they are relevant but not detailed here
class Observer(ABC):
    @abstractmethod
    def update(self, activity):
        pass

class Observable(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, activity):
        for observer in self.observers:
            observer.update(activity)

# Shape.py
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# Circle.py
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

# Rectangle.py
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

# Polygon.py, corrected with math imports
class Polygon(Shape):
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def get_area(self):
        perimeter = self.sides * self.length
        apothem = self.length / (2 * tan(pi / self.sides))
        return (perimeter * apothem) / 2

# main function to demonstrate functionality
def main():
    shapes = [Circle(5), Rectangle(4, 5), Polygon(5, 3)]
    for shape in shapes:
        print(f"Shape area: {shape.get_area()}")

if __name__ == "__main__":
    main()
