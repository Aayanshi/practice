import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
left(90)
forward(70)
for i in range(100):
    color("white")
    circle(i*0.7)
    color("black")
    circle(i*0.5)
    left(3)
    forward(3)
color("black")
right(30)
forward(270)
left(30)
for i in range(100):
    color("white")
    circle(i*0.7)
    color("black")
    circle(i*0.5)
    left(3)
    forward(3)



done()
