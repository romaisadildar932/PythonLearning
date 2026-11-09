#class -> is the blueprint or template for creating objects. It defines the properties and behaviors that the objects created from the class will have.
#object -> is an instance of a class. It is created based on the blueprint defined by the class and can have its own unique values for the properties defined in the class.
#without attributes
class Car: #create class
    #method
    def  start(self):
        print("Car is starting")
    def stop(self):
        print("Car is stopping")
car1 = Car() #Creates an object (instance) of the Car class.
car2 = Car()

car1.start() #Calls the start() method of the car1 object.
car1.stop()

#class with attributes
class Cars:
    def details(self,model,color):
        self.model = model
        self.color = color
    def show_details(self):
        print("Car model:", self.model)
        print("Car color:", self.color)
car = Cars()
car.details('Tesla','Red')
car.show_details()