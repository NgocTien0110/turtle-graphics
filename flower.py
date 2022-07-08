import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
col = ["yellow", "red", "pink", "cyan", "light green", "blue"]

for i in range(150):
    t.pencolor(col[i % 6])
    t.circle(190-i/2,90)
    t.left(90)
    t.circle(190-i/3,90)
    t.left(60)

t.penup()
t.goto(130,-300)
t.pendown()
t.write('by Ngọc Tiến', font=("Bradley Hand ITC", 20, "bold"))    
t.hideturtle();

s.exitonclick()