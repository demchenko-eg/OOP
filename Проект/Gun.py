import math
from PIL import Image, ImageTk


class Gun:
    def __init__(self, game):
        self.game = game
        self.id = self.game.canvas.create_line(427, 570, 427, 520, fill='black', width=2)
        x0, y0 = 427 - 7, 570 - 7
        x1, y1 = 427 + 7, 570 + 7
        self.gun_image = Image.open("gun.png")
        self.gun_image = self.gun_image.resize((15, 65), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.gun_image)
        self.image_id = self.game.canvas.create_image(427, 545, image=self.tk_image)
        self.circle = self.game.canvas.create_oval(x0, y0, x1, y1, fill='#87997a')
        self.angle = 0

    def move(self, event):
        if self.game.paused:
            return
        key = event.keysym
        if key == 'Left':
            self.rotate(-4)
        elif key == 'Right':
            self.rotate(4)

    def rotate(self, angle):
        cx, cy = 427, 570
        gx0, gy0, gx1, gy1 = self.game.canvas.coords(self.id)
        angle_rad = math.radians(angle)
        gx0, gy0 = self.rotate_point(gx0, gy0, cx, cy, angle_rad)
        gx1, gy1 = self.rotate_point(gx1, gy1, cx, cy, angle_rad)
        self.game.canvas.coords(self.id, gx0, gy0, gx1, gy1)
        self.angle += angle
        rotated_image = self.gun_image.rotate(-self.angle, expand=True)
        self.tk_image = ImageTk.PhotoImage(rotated_image)
        self.game.canvas.itemconfig(self.image_id, image=self.tk_image)
        self.update_image_position()

    def update_image_position(self):
        cx, cy = 427, 570
        gx0, gy0, gx1, gy1 = self.game.canvas.coords(self.id)
        mid_x = (gx0 + gx1) / 2
        mid_y = (gy0 + gy1) / 2
        self.game.canvas.coords(self.image_id, mid_x, mid_y)

    def rotate_point(self, x, y, cx, cy, angle):
        x -= cx
        y -= cy
        x_new = x * math.cos(angle) - y * math.sin(angle) + cx
        y_new = x * math.sin(angle) + y * math.cos(angle) + cy
        return x_new, y_new
