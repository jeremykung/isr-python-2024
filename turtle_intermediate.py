# Pen Width ✅
# Pen Colors ✅
#   - color() ✅
#   - Hex ✅
# Fill  ✅
#   - fillcolor() ✅
#   - begin_fill() ✅
#   - end_fill() ✅

import turtle

turtle.forward(100)

# change pen width
turtle.width(10)
turtle.forward(100)

# change pen color
turtle.color('red')        # using color name
turtle.forward(50)
turtle.color('#29e3c1')    # using color hex
turtle.left(90)
turtle.forward(100)

# add fill color
turtle.fillcolor('green')
turtle.begin_fill()        # start filling
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()          # end filling

turtle.done()





















# import turtle



# turtle.forward(100)
# turtle.color('#109080')
# turtle.width(4)
# turtle.fillcolor('blue')
# turtle.begin_fill()
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.end_fill()

# turtle.done()