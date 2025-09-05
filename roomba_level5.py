# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here
def draw_shape(number_of_sides=5):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        forward(30)
        right(angle)

draw_shape()
draw_shape()    
draw_shape()    
draw_shape()    

# End your code here
###
 
window.exitonclick()