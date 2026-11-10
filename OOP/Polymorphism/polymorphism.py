'''polymorphism - one name - many forms 
  same method behaves differently for different classes'''

 #polymorphism
class Bird:
   def move(self):
       print('Bird Flies')

class Fish:
    def move(self):
         print('Fish swims')

bird = Bird()
fish = Fish()

bird.move()
fish.move()
        
 