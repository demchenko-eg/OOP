import turtle
from random import randint, uniform
import time

class Triangle:
    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(self.size)
            turtle.left(120)
        turtle.end_fill()

def generate_random_triangle():
    size = randint(50, 200)
    color = (uniform(0, 1), uniform(0, 1), uniform(0, 1))
    x = randint(-300, 300)
    y = randint(-300, 300)
    return Triangle(size, color, x, y)

turtle.speed(0)
turtle.hideturtle()
turtle.delay(0)
turtle.tracer(0)

triangles = []
for i in range(100):
    triangle = generate_random_triangle()
    triangle.draw()
    turtle.update()
    triangles.append(triangle)
    time.sleep(1 / 10)
angle = 0
while angle <= 360:
    turtle.clear()
    for triangle in triangles:
        turtle.setheading(angle)
        triangle.draw()
    turtle.update()
    angle += 3


turtle.exitonclick()
