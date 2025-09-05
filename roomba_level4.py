# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius=5)

###
# Start your code here
 
step_size = 40      
num_rows = 24     
row_length = 762  


right(270)

for i in range(num_rows):
    forward(row_length)
    if i < num_rows - 1:
        if i % 2 == 0:
            right(90)
            forward(step_size)
            right(90)
        else:
            left(90)
            forward(step_size)
            left(90)
 
# End your code here
###
 
window.exitonclick()