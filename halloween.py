from turtle import *

print('Happy Halloween... ')
title('Happy Halloween')
bgcolor("black")


def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def drawcircle(x, y):
    color("orangered")
    penup()
    goto(x, y)
    begin_fill()
    circle(70)
    end_fill()


drawcircle(20, 0)
drawcircle(-20, 0)


def triangle(x, y):
    color("yellow")
    penup()
    goto(x, y)
    begin_fill()
    for i in range(3):
        forward(40)
        left(360/3)
    end_fill()


triangle(15, 80)
triangle(-55, 80)
triangle(-20, 50)


def mouth():
    color("yellow")
    up()
    goto(-60, 40)
    down()
    begin_fill()
    goto(-30, 20)
    goto(30, 20)
    goto(60, 40)
    goto(0, 30)
    end_fill()


mouth()


def stem():
    color("green")
    up()
    goto(-40, 130)
    down()
    begin_fill()
    goto(40, 130)
    goto(20, 150)
    goto(10, 170)
    goto(0, 180)
    goto(-15, 175)
    goto(-10, 155)
    goto(-15, 140)
    goto(-40, 130)
    end_fill()


stem()

my_goto(-170, -70)
write('Happy Halloween', font=("Bradley Hand ITC", 35, "bold"))
my_goto(-80, -140)
write('by Ngọc Tiến ', font=("Bradley Hand ITC", 35, "bold"))

exitonclick()
