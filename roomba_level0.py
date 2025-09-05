# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
 
forward(156)
left(90)
forward(156)
left(90)
forward(156)
left(90)
forward(126)
left(90)
forward(126)
left(90)
forward(95)
left(90)
forward(95)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(45)
 
# End your code here
###
 
window.exitonclick()