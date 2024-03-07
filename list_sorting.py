# LISTS (Part 2)
# Sorting ✅
# Sorting (non-permanent) ✅
# Reverse Sorting ✅
# Reverse Order ✅
# List Length ✅

words = ["people", "gun", "gum", "rudolf", "hockey"]
randomNumbers = [3, 1, 5, 2, 4]

randomNumbers.sort(reverse=True)
print(randomNumbers)

print(words)

words.sort()                # sorts alphabetically (permanently)
print(words)

print(sorted(words))        # sorts but doesn't change original list
print(words)

words.sort(reverse=True)    # sorts in reverse (permanently)
print(words)

print(sorted(words, reverse=True))  # sorts in reverse but doesn't change original list
print(words)

words.reverse()             # reverse the order (permanently)
print(words)

print(len(words))           # shows the length of the list