# Week 2 day 5
# Worksheet titled "day5-Portfolio-Turtle"
# Steven D. Garcia

import turtle
turtle.Screen()
turtle.shape("turtle") # optional
turtle.speed(1)
turtle.pensize(4)
turtle.pencolor("blue")

# Step 7. Draw a picture with functions
# Square
def square(length):
    for each in range(4):
        turtle.forward(length)
        turtle.right(90)
# square(150)

# Move turtle
turtle.penup()
turtle.home()
turtle.forward(200)
turtle.pendown()

# Triangle
def triangle(length):
    for each in range(3):
        turtle.forward(length)
        turtle.left(120)
# triangle(120)

def house(length):
    for each in range(1):
        square(length)
        triangle(length)
house(length=184)





turtle.Screen().exitonclick()