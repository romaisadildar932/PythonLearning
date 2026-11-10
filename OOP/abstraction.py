'''abstraction -> process of hiding the internal/complex details of an object and showing only the essential features
abstract class -> a class that cannot be instantiated and is meant to be subclassed. It serves as a blueprint for other classes and may contain abstract methods that must be implemented by its subclasses.
'''
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass #abstract method
    @abstractmethod
    def perimeter(self):
        pass #abstract method

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
      print(3.14 * self.radius * self.radius)
    def perimeter(self):
       print(2 * 3.14 * self.radius)
c =Circle(5)
c.area()
c.perimeter()