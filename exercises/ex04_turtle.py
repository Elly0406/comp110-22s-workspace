"""EX04 - Turtle - structure program and use turtle to design a graphic on screen."""

__author__ = "730365499"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entry point of the program and call each function with different number."""
    ertle: Turtle = Turtle()
    colormode(255)
    draw_star(ertle, 200, 250, 10)
    draw_star(ertle, -200, 200, 10)
    draw_star(ertle, -40, 300, 15)
    draw_star(ertle, 250, 150, 15)
    draw_star(ertle, -300, 300, 15)
    draw_star(ertle, 30, 180, 13)
    draw_star(ertle, -330, 120, 13)
    tree_one(ertle, -250, 0, 60, 90)
    tree_one(ertle, -270, -40, 90, 113)
    tree_one(ertle, -290, -80, 120, 160)
    tree_two(ertle, -220, -80, 120, 30)
    meteor(ertle, 0, 100)
    meteor(ertle, -260, 250)
    meteor(ertle, -290, 20)
    done()


def draw_star(a: Turtle, x: float, y: float, width: float) -> None:
    """Draw a star of given size whose start point is located at x, y."""
    a.penup()
    a.goto(x, y) 
    a.setheading(0.0)
    a.pendown()
    a.speed(500)
    a.fillcolor("yellow")
    a.begin_fill()
    i: int = 0
    while i < 5:
        a.forward(width)
        a.left(72)
        a.forward(width)
        a.right(144) 
        i = i + 1
    a.end_fill()


def tree_one(b: Turtle, x: float, y: float, side_one: float, side_two: float) -> None:
    """Draw a isosceles acute triangle as part of tree. The size is defined by length of three sides."""
    b.penup()
    b.goto(x, y)
    b.setheading(0.0)
    b.pendown()
    b.speed(500)
    b.color("green", "green")
    b.begin_fill()
    b.left(40)
    b.forward(side_one)
    b.right(80)
    b.forward(side_one)
    b.right(140)
    b.forward(side_two)
    b.end_fill()


def tree_two(c: Turtle, x: float, y: float, height: float, width: float) -> None:
    """Draw a rectangular as tree trunk of given height and width."""
    c.penup()
    c.goto(x, y)
    c.setheading(0.0)
    c.pendown()
    c.speed(500)
    c.color(68, 27, 0)
    c.begin_fill()
    i: int = 0
    while i < 2:
        c.forward(width)
        c.right(90)
        c.forward(height)
        c.right(90)
        i += 1
    c.end_fill()


def meteor(d: Turtle, x: float, y: float) -> None:
    """Draw continuous incomplete circle to form shape like meteor."""
    d.penup()
    d.goto(x, y)
    d.setheading(0.0)
    d.pendown()
    d.color(169, 176, 180)
    i: int = 0
    while i < 6:
        d.circle(100, 80)
        d.forward(1)
        d.circle(100, -80)
        i += 1


if __name__ == "__main__":
    main()