# Week 2 Day 5
# Worksheet Titled "day-5-Portfolio-Turtle"
# Steven D. Garcia

import turtle
turtle.Screen()
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor("red")

def rectangle(width, height):
    for each in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
# rectangle(width=20, height=260)

def octagon(length):
    for each in range(8):
        turtle.forward(length)
        turtle.left(45)
# octagon(length=145)

def stop_sign(height, length):
    for each in range(1):
        octagon(length)
        turtle.forward(20)
        turtle.right(90)
        rectangle(width=260, height=20)
stop_sign(height=60, length=60)

turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.pendown()
turtle.color("blue")

def stop_sign(height, length):
    for each in range(1):
        octagon(length)
        turtle.forward(10)
        turtle.right(90)
        rectangle(width=130, height=10)
stop_sign(height=30, length=30)


turtle.Screen().exitonclick()