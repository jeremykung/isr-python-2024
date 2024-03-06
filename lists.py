# LISTS
# Declaring ✅
# Indexes ✅
# Accessing ✅
# Adding (append() & insert()) ✅
# Deleting (pop()) ✅

#                0        1         2
chessPieces = ["rook", "knight", "king"]

print(chessPieces[2])           # prints "king"

chessPieces.append("queen")     # adds "queen" to end of list

chessPieces.insert(0, "pawn")   # inserts "pawn" at the 0 index of list

chessPieces.pop()               # deletes the last item in the list

print(chessPieces)              # print out the list