# My first graphic shape.

import turtle

""" 't' becomes the object that is the canvas.
Alternatively one can write 'turtle.Turtle()' to begin and use 'turtle.<method>()' to draw.
"""
# Sets t as canvas object.
t = turtle.Turtle()
# line width is 5 px
# t.width(5)
# Drawing speed is 1 - 9 (slow to fast). 0 is almost instant (based on computer speed)
t.speed(1)
"""
# Moves forward 100 px
t.forward(100)
# Turns left 90 degrees
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
# Finishes as a box.
"""
# Go to a specific spot
t.up()
t.goto(100, 100)
t.down()
# Makes a circle
t.circle(150)
# "Lifts" pencil from canvas. No line is left.
# t.up()
# Places pencil back down on canvas. Line begins writing.
# t.down
# Returns to home coordinates leaving behind a line.
#t.home()
# filling a cicle
t.begin_fill()
t.fillcolor("#007FFF")
t.circle(75)
t.end_fill()

t.up()
t.goto(-100, -100)
t.down()
t.circle(150)
t.begin_fill()
t.fillcolor("#FF0080")
t.circle(75)
t.end_fill()

t.up()
t.goto(100, -100)
t.down()
t.circle(150)
t.begin_fill()
t.fillcolor("#80FF00")
t.circle(75)
t.end_fill()

t.up()
t.goto(-100, 100)
t.down()
t.circle(150)
t.begin_fill()
t.fillcolor("#FF8000")
t.circle(75)
t.end_fill()
