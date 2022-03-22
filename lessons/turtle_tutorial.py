from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.fillcolor(194, 161, 175)
leo.pencolor("black")
leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.color(77, 65, 70)
bob.speed(500)

leo.penup()
leo.goto(50, 50)
leo.pendown()

leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1 
leo.end_fill()

bob.penup()
bob.goto(50, 50)
bob.pendown()

side_length: float = 300

i: int = 0
while (i < 150):
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
    side_length = side_length + 0.979
done()
