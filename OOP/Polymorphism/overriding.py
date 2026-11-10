#method overriding ->one way to achieve polymorphism,parent class method is overridden in child class
class Animal():
    def sound(self):
        print('Animal makes sound')
class Dog(Animal):
    def sound(self):
        print('Dog barks')
class Cat(Animal):
    def sound(self):
        print('Cat meows')
d1 = Dog()
c1 = Cat()
a1 = Animal()
a1.sound()
d1.sound()
c1.sound()
