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


#Polymorphism with inheritance(Method Overriding)
class Employee:
    def work(self):
        print("Employees work 8 hours.") 

class Developer(Employee):
    def work(self):
        print("Developer writes code.")

class Manager(Employee):
    def work(self):
        print("Manager manages team.")

workers=[Developer(), Manager()]
for worker in workers:
    worker.work()               #Employee ko work ma comment hudahudai developer ra manager ko message print vairakhe ko xa on function call


#operator overloading
#__sub__, __add__, __mul__, __truediv__, __lt__, __gt__, __eq__, __init__



# Operator overloading with +
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, other):       #overloading the +  operator
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
    
p1=Point(4,5)
p2=Point(2,4)
p3=p1+p2                    #internally calls p1.__add__(p2)
print(p3)