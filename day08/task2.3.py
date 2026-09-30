import turtle


def draw_polygon(sides):
    pen = turtle.Turtle()
    angle = 360 / sides
    for i in range(sides):
        pen.forward(100)
        pen.right(angle)


screen = turtle.Screen()
draw_polygon(3)
draw_polygon(4)
draw_polygon(5)
draw_polygon(6)
screen.exitonclick()
