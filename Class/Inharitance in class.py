""" #class
#object
#self
#initiator/constructor
#inheritance:
        -single inheritance
        -multiple inheritance
        -multi-level inheritance

 """


# Single Inheritance Example (Vehicle → Car)
# Parent class
class Vehicle:
    def show_info(self):
        print("This is a vehicle.")

# Child class
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Create object of Car
c = Car()

# Call both methods
c.show_info()
c.car_info()





# Multiple Inheritance Example (Teacher + Singer → Person)

# First parent class
class Teacher:
    def teach(self):
        print("Teaching students")

# Second parent class
class Singer:
    def sing(self):
        print("Singing a song")

# Child class inheriting from both Teacher and Singer
class Person(Teacher, Singer):
    pass

# Create object of Person
p = Person()

# Call all methods
p.teach()
p.sing()