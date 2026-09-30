import turtle


def sierpinski(size, depth):
    if depth == 0:
        for i in range(3):
            pen.forward(size)
            pen.left(120)
        return
    half = size / 2
    sierpinski(half, depth - 1)
    pen.forward(half)
    sierpinski(half, depth - 1)
    pen.backward(half)
    pen.left(60)
    pen.forward(half)
    pen.right(60)
    sierpinski(half, depth - 1)
    pen.left(60)
    pen.backward(half)
    pen.right(60)


screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-170, 200)
pen.setheading(270)
pen.pendown()
sierpinski(400, 6)
screen.exitonclick()
