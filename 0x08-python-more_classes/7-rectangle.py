#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            print()
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        count = ""
        for i in range(self.__height):
            for j in range(self.__width):
                count += "#"
            count += "\n"
        return count

    def __repr__(self):
        return (f"({self.__width}, {self.__height})")
        Rectangle.print_symbol += ""
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
