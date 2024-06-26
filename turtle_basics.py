# 1. Importing Turtle Functions
# 2. Drawing
#   - forward(units)
#   - left(degrees) / right(degrees)
#   - goto(x, y)
#   - circle(radius)
#   - penup()
#   - pendown()
# 3. done() - not closing after drawing

# we are importing a library of functions for drawing
from turtle import *

# draw 100 steps forward
forward(100)

# rotate the pen left 90 degrees
left(90)

# draw 200 steps forward
forward(200)

# draw a circle with a radius of 30
circle(30)

# move the pen to (0,0)
goto(0,0)

# lifts up the pencil
penup()

# move the pen to (-200,-200)
goto(-200,-200)

# puts the pencil back down
pendown()

# draw a half a circle (180 deg) with radius of 20
circle(20, 180)

# keeps the window open after the drawing is done
done()