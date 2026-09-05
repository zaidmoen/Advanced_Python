"""An abstract base class defines a shared area contract."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the non-negative area."""


class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side: float):
        if side < 0:
            raise ValueError("Side cannot be negative")
        self.side = side

    def area(self) -> float:
        return self.side ** 2


if __name__ == "__main__":
    for shape in [Circle(2), Square(3)]:
        print(round(shape.area(), 2))  # 12.57, 9
