import math


class Gun:
    def __init__(self, game):
        self.game = game
        self.id = self.game.canvas.create_line(425, 570, 425, 520, fill='black', width=3)
        x0, y0 = 427 - 5, 570 - 5
        x1, y1 = 427 + 5, 570 + 5
        self.circle = self.game.canvas.create_oval(x0, y0, x1, y1, fill='gray')

    def move(self, event):
        if self.game.paused:
            return
        key = event.keysym
        if key == 'Left':
            self.rotate(-5)
        elif key == 'Right':
            self.rotate(5)

    def rotate(self, angle):
        cx, cy = 427, 570
        gx0, gy0, gx1, gy1 = self.game.canvas.coords(self.id)
        angle_rad = math.radians(angle)
        gx0, gy0 = self.rotate_point(gx0, gy0, cx, cy, angle_rad)
        gx1, gy1 = self.rotate_point(gx1, gy1, cx, cy, angle_rad)
        self.game.canvas.coords(self.id, gx0, gy0, gx1, gy1)

    def rotate_point(self, x, y, cx, cy, angle):
        x -= cx
        y -= cy
        x_new = x * math.cos(angle) - y * math.sin(angle) + cx
        y_new = x * math.sin(angle) + y * math.cos(angle) + cy
        return x_new, y_new