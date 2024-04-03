# 0. What are Functions? ✅
# 1. Defining ✅
# 2. Calling ✅
# 3. Parameters & Arguments ✅
# 4. Default Values ✅
# 5. Return Values

# Cooking steak
# 1. Kill cow
# 2. Transport cow
# 3. Cut the cow
# 4. Cook the cow
# 5. Add seasoning

# Defining a function
def makeSteak():
    print("kill cow")
    print("transport cow")
    print("cut cow")
    print("cook")
    print("season")

# Call a function (actually do it)
# makeSteak()

# Function with a PARAMETER (topping)
def makeRice(topping):
    print("I made rice with", topping)

# Call the function with an ARGUMENT (chicken)
makeRice("chicken")
# Call the function with an ARGUMENT (cheeseburgers)
makeRice("cheeseburgers")

def add_drink(drink):
    print("I ordered my meal with", drink)

add_drink("coke")
add_drink("Philip drinking milk")

# Create a function that accepts your lucky number as a parameter. Call the function a few times with different numbers as arguments.

# def luckyNumber(number):
#     print("this is my lucky number:", number)

# luckyNumber(3)
# luckyNumber(12)

# Functions with multiple parameters/arguments
def makeSandwich(meat, vegetable, sauce):
    print("I made a", meat, vegetable, "sandwich with", sauce)

makeSandwich("ham", "ketchup", "lettuce")

# Make a function that accepts two numbers as parameters
# Add the numbers together
# Print the sum


# Default Parameters
def salute(name="Mr. Kung"):
    print("goodbye", name)

salute("Klara")

salute()

# Make a function with two parameters (person1, person2)
# Each parameter should have a default value
# The function will say hi to both people
# Call it with arguments
# Call it without arguments
# Call it with one argument

def greet(person1="Mr. Kung", person2="Venla"):
    print("hi", person1, "and", person2)

greet("Dominika", "Maria F")
greet()
greet("Olivers")

# Function with return value ("purple")
def giveMeColour():
    return "purple"


maxCatcher = "giveMeColour()"
print(maxCatcher)

def add_one(number):
    number_plus_one = number + 1
    return number_plus_one

result = add_one(1)
print(result)

# Create a function that returns a number minus 2
# return that number
# catch it in a variable
# print the variable

def minusTwo(number):
    answer = number - 2
    return answer

result = minusTwo(7)
print(result)




