#inheritence -> mechanism by which one class can acquire the properties and methods of another class

class Animal:
    def speak(self):
        print('Animal speaks')
class Dog(Animal):
    def bark(self):
        print('Dog Barks')
d = Dog()
d.bark() #calls the bark method of Dog class
d.speak() #calls the speak method of Animal class(parent), which is inherited by Dog class(child)