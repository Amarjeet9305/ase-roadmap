# Write a program on Car dependency and instance

# Creating a class of car (like bluePrint)

# Class (blueprint)
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"{self.color} {self.brand} is driving!")

# Object (instance)
car1 = Car("XUV", "Black")
car1.drive()
