# What is a class?
#   - constructor function: def __init__()
#   - default values
#   - default methods

# Instantiation
#   - accessing object attributes
#   - accessing object methods

# Examples of classes and objects
#   - turtle
#   - random

class Animal:
    def __init__(self, name, color, sound, extinct):
        self.name = name
        self.color = color
        self.sound = sound
        self.extinct = extinct

    def describe(self):
        print(self.name, "is", self.color, "and makes a", self.sound, "sound")

    def findPet(self):
        if (self.extinct):
            print("can't be a pet, they are exctinct")
        else:
            print("you went to the pet store and got one!")

spot = Animal("dog", "white and brown", "woof", False)

spot.describe()
spot.findPet()

mammoth = Animal("wooly mammoth", "brown", "who knows", True)

mammoth.findPet()




















# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     # Default attributes
#     description = "This is a car"

#     # Default methods (functions from an object)
#     def drive():
#         print("{self.model} is driving")

#     def showAge():
#         print("the car is made in {self.year}")

# firstCar = Car("toyota", "corolla", 2003)

