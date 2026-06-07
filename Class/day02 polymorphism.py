#polymorphism 
""" 
    -polymorphism means "of many form"
    -the same function or method name can perform different tasks based on the object that calls it.

 """

#polymorphism with Class Methods: 'two different classes with the same name'

class Dog():
    def sound(self):
        return "woof!"

class Cat():
    def sound(self):
        return "meow!"

animals=[Dog(), Cat()]
for animal in animals:
    print(animal.sound()) 