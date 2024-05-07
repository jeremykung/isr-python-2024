# 1. Looping through lists ✅
# 2. list(range()) for number lists ✅
    # - range(start, stop) ✅
    # - range(start, stop, step) ✅
# 3. min(), max(), sum() ✅
# 4. Working with lists in loops ✅

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

print(colors[0])        # this is bad because we are copy pasting code too much!
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])
print(colors[5])

for thing in colors:    # use a for loop instead :)
    print(thing)

nums = list(range(1, 10))
print(nums)

evenNums = list(range(0,21,2))
print(evenNums)

# print a list of numbers that count by 3 up to 60
multiplesOfThree = list(range(0, 60, 3))
print(multiplesOfThree)

# print odd numbers only up to 20
oddNums = list(range(1,20,2))
print(oddNums)

straightNums = [4, 2, 6, 7, 5]
print(max(straightNums))
print(min(straightNums))
print(sum(straightNums))

# print each number in colorfulNums doubled
colorfulNums = [15, 9, 3, 12, 6]
for number in colorfulNums:
    print(number)
    numberDoubled = number * 2
    print(numberDoubled)

# List Comprehension
    # - a fast way to write simple for loops
addOne = [num + 1 for num in colorfulNums]
print("addOne", addOne)
