# Shape.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# Circle.py
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

# Square.py
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

# main function
def main():
    shapes = [Circle(5), Square(4)]
    for shape in shapes:
        print(f"Shape area: {shape.get_area()}")

if __name__ == "__main__":
    main()
