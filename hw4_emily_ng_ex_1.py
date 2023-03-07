'''
Homework 4 Exercise 1
Emily Ng
3/5/2023
This program contains the Rectangle, Circle, and Square Classes
Each class has a function to compute the area
The Rectangle and Square classes have a method to calculate the diagonal
The circle class has a method to calculate the diameter
All classes have a method to calculate the perimeter
'''
import math


class Rectangle:
    #constructor
    def __init__(self, length, width):
        self._length = length
        self._width = width

    #area
    def area(self):
        return self._length * self._width

    #perimeter
    def perimeter(self):
        return (2 * self._length) + (2 * self._width)

    #diagonal
    def diagonal(self):
        return math.sqrt(math.pow(self._length, 2) + math.pow(self._width, 2))

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Circle:
    # constructor
    def __init__(self, radius):
        self._radius = radius

    # area
    def area(self):
        return math.pi * math.pow(self._radius, 2)

    # circumference
    def circumference(self):
        return 2 * math.pi * self._radius

    # diagonal
    def diameter(self):
        return 2 * self._radius

def main():

    #calculate rectangle and diagonal
    rectangle = Rectangle(20, 10)

    diag = rectangle.diagonal()

    square = Square(10)

    #calculate circumfrence of a circle
    circle = Circle(diag)

    print(circle.circumference())

main()