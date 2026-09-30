import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(4)

for i in range(200):
    pen.forward(i * 1)
    pen.right(60)

