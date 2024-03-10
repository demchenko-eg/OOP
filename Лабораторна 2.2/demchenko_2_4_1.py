import turtle
from datetime import datetime

class ClockHand:
    def __init__(self, length, angle, color="black"):
        self.length = length
        self.angle = angle
        self.color = color

    def draw(self):
        turtle.color(self.color)
        turtle.width(self.thickness)
        turtle.pendown()
        turtle.right(self.angle + 270)
        turtle.forward(self.length)
        turtle.backward(self.length)
        turtle.left(self.angle + 270)
        turtle.penup()

class Digit:
    def __init__(self, num, radius, color="black"):
        self.num = num
        self.radius = radius
        self.color = color

    def draw(self):
        turtle.color(self.color)
        turtle.penup()
        angle = self.num * 30 - 90
        turtle.right(angle)
        turtle.forward(self.radius)
        turtle.write(str(self.num), align="center", font=("Arial", 12, "normal"))
        turtle.backward(self.radius)
        turtle.left(angle)
        turtle.penup()

class CircleDrawer:
    def __init__(self, radius1, radius2, center1, center2):
        self.radius1 = radius1
        self.radius2 = radius2
        self.center1 = center1
        self.center2 = center2

    def draw_circles(self):
        turtle.penup()
        turtle.goto(self.center1[0], self.center1[1] - self.radius1)
        turtle.pendown()
        turtle.color("black")
        turtle.circle(self.radius1)
        turtle.penup()
        turtle.color("white")
        turtle.goto(self.center2[0], self.center2[1] - self.radius2)
        turtle.pendown()
        turtle.circle(self.radius2)
        turtle.penup()

class AnalogClock:
    def __init__(self):
        self.hour_hand = ClockHand(100, 0, color="black")
        self.minute_hand = ClockHand(130, 0, color="black")
        self.second_hand = ClockHand(160, 0, color="black")
        self.hour_hand.thickness = 6
        self.minute_hand.thickness = 3
        self.second_hand.thickness = 1
        self.digits = [Digit(i, 160, color="black") for i in range(1, 13)]
        self.circle_drawer = CircleDrawer(200, 220, (0, 0), (0, 210))

    def draw_digits(self):
        for digit in self.digits:
            digit.draw()

    def draw_hands(self, hours, minutes, seconds):
        self.hour_hand.angle = (hours % 12) * 30 + (minutes / 60) * 30 - 3
        self.minute_hand.angle = minutes * 6 + (seconds / 60) * 6 - 3
        self.second_hand.angle = seconds * 6 - 3
        self.hour_hand.draw()
        self.minute_hand.draw()
        self.second_hand.draw()

    def draw_circles_around_dial(self):
        self.circle_drawer.draw_circles()

    def update_clock(self):
        now = datetime.now()
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second
        turtle.clear()
        self.draw_circles_around_dial()
        self.draw_digits()
        self.draw_hands(hours, minutes, seconds)
        turtle.ontimer(self.update_clock, 1000)

    def draw_analog_clock(self):
        turtle.speed(100)
        turtle.hideturtle()
        turtle.tracer(0, 0)
        self.draw_circles_around_dial()
        self.draw_digits()
        self.update_clock()
        turtle.mainloop()


analog_clock = AnalogClock()
analog_clock.draw_analog_clock()