from turtle import *
color("green")
bgcolor("black")
hideturtle()
speed(11)
b = 0
right(100)
while b < 200:
    right(b)
    forward(b*3)
    b = b+1
exitonclick()
