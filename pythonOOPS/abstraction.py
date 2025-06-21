from abc import ABC, abstractmethod

#abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Baww Baww")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# cannot instantiace abstract class directly
# a = Animal() # this will not be working..

d = Dog()
c = Cat()
d.make_sound()
c.make_sound()