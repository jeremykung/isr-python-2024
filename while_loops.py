# While loops keep doing what is in the loop until the condition is no longer true
# while CONDITION:
#   // code to run


# Here we run a game until something causes it to be false

run = True

while run:
    print('run the game code...')
    run = False



# Here we run the code until score is over 10

score = 0

while score < 10:
    print('play game!!')
    print('current score:', score)
    score = score + 1