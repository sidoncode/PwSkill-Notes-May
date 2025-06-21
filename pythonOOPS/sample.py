class Animal:
    pass

class Dog(Animal):
    pass

#function: is -> Boolean (True / False)

print(issubclass(Dog,Animal)) # True
print(issubclass(Animal,Dog)) #False

dog = Dog()
print(isinstance(dog,Dog)) # True
print(isinstance(dog,Animal)) # True



