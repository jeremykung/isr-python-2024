# 1. Conditions ✅
#   - == equal to
#   - != not equal to
#   - > greater than
#   - >= greater than or equal to
#   - < less than
#   - <= less than or equal to
# 2. Multiple Conditions ✅
#   - and
#   - or
# 3. If Statements ✅
#   - if
#   - else
#   - elif
# 4. Converting "Strings" to Ints


print(5 > 3)
print(5 == 3)

benAge = 15
benCountry = "Peru"

# if
if benAge > 18:
    print("Ben can drive a car")

# if else
if benAge > 12:
    print("Ben is a teenager")
else:
    print("Ben is a little boy")

# if elif else
if benCountry == "America":
    print("Make America Great Again!")
elif benCountry == "Latvia":
    print("Make Latvia Great Again!")
elif benCountry == "Afghanistan":
    print("Make The Middle East Great Again!")
else:
    print("Ben is homeless")


# multiple conditions
    
# both conditions must be true
print(benCountry == "America" and benAge >= 21)

# only one condition must be true
print(benCountry == "America" or benAge >= 21)

# 1. Make an if statement that checks if the user can drive without an adult in the car. You must be 18 or over to drive without an adult.

# 2. Modify your if statement to check if they are over 16. If they are over 16, print that they can drive only with an adult. If they are over 18, print they can drive solo.
    
# 3. Modify the if statement again, this time if the user is under 16, print that they can roller blade instead.


# Get a user input as a number

favNumber = input("what is ur fav num")

# int() takes a string and converts it to a number 
favNumber = int(favNumber) # changes "4" to 4

print(favNumber == 4)

# shorthand way of writing the above
favNumber = int(input("what is ur fav num"))


