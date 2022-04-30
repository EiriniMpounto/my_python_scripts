'Author: Irene Bounto'

import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)


def function():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.color('red', 'pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
function()
turtle.left(120)
function()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done
