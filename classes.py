# What is a class? ✅
#   - constructor function: def __init__() ✅
#   - default values ✅
#   - default methods ✅

# Instantiation ✅
#   - accessing object attributes ✅
#   - accessing object methods ✅

# Examples of classes and objects ✅
#   - turtle ✅


# Create a blueprint for house (Class)

class House:
    # constructor function
    def __init__(self, roof, numWindows, color):
        self.roof = roof
        self.numWindows = numWindows
        self.color = color

    # custom functions
    def heatHouse(self, degrees):
        print("we are heating the house to", degrees)



# Create objects using the Class (Instantiate)

vladsHouse = House("cube", 69, "light blue")
vladsHouse.heatHouse(25)

domsHouse = House("circle", 7, "orange")
jinheHouse = House("triangle", 5, "black")
mrkungHouse = House("no roof", 0, "clay")

print(domsHouse.color)          # orange
print(domsHouse.numWindows)     # 7



# Car Example

class Car:
    def __init__(self, spoiler, doors, color):
        self.spoiler = spoiler
        self.doors = doors
        self.color = color

    def honk(self):
        print("your car honked")

    def describeCar(self):
        print("your car is", self.color, "and has", self.doors, "doors" )

maxCar = Car(True, 2, "Red")
alexCar = Car(True, 2, "Black")
klaraCar = Car(False, 7, "Purple")

klaraCar.describeCar()
maxCar.honk()














# class Animal:
#     def __init__(self, name, color, sound, extinct):
#         self.name = name
#         self.color = color
#         self.sound = sound
#         self.extinct = extinct

#     def describe(self):
#         print(self.name, "is", self.color, "and makes a", self.sound, "sound")

#     def findPet(self):
#         if (self.extinct):
#             print("can't be a pet, they are exctinct")
#         else:
#             print("you went to the pet store and got one!")

# spot = Animal("dog", "white and brown", "woof", False)

# spot.describe()
# spot.findPet()

# mammoth = Animal("wooly mammoth", "brown", "who knows", True)

# mammoth.findPet()




















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

