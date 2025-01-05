import turtle
import random

screen = turtle.Screen()
screen.title("Colorful Dot Painting")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

dot_size = 20
grid_size = 10
spacing = 50

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

screen.colormode(1.0)

pen.goto(-grid_size * spacing // 2, grid_size * spacing // 2)

for row in range(grid_size):
    for col in range(grid_size):
        pen.dot(dot_size, random_color())
        pen.forward(spacing)
    pen.backward(grid_size * spacing)
    pen.right(90)
    pen.forward(spacing)
    pen.left(90)

screen.mainloop()
