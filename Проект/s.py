import tkinter as tk
import random
import math
import time

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Zenitka Game")
        self.canvas = tk.Canvas(root, width=1000, height=600, bg='white')
        self.canvas.pack()
        self.score = 0
        self.misses = 0
        self.missed = 0
        self.aircrafts = []
        self.bullets = []
        self.last_shot_time = time.time()
        self.create_aircraft()
        self.create_zenitka()
        self.create_gun()
        self.canvas.bind("<KeyPress>", self.move_gun)
        self.canvas.bind("<space>", self.fire_bullet)
        self.canvas.focus_set()
        self.score_label = tk.Label(root, text="Збито: 0", font=("Helvetica", 16))
        self.score_label.place(x=800, y=20)
        self.misses_label = tk.Label(root, text="Промахів: 0", font=("Helvetica", 16))
        self.misses_label.place(x=800, y=50)
        self.missed_label = tk.Label(root, text="Пропущено: 0", font=("Helvetica", 16))
        self.missed_label.place(x=800, y=80)
        self.update_game()

    def create_aircraft(self):
        x = 1000
        y = random.randint(50, 400)
        aircraft = self.canvas.create_rectangle(x, y, x+50, y+20, fill='red')
        self.aircrafts.append(aircraft)
        self.root.after(random.randint(100, 10000), self.create_aircraft)

    def create_zenitka(self):
        self.zenitka = self.canvas.create_rectangle(400, 560, 450, 580, fill='blue')

    def create_gun(self):
        self.gun = self.canvas.create_line(425, 570, 475, 570, fill='black', width=3)

    def move_gun(self, event):
        key = event.keysym
        if key == 'Left':
            self.rotate_gun(-5)
        elif key == 'Right':
            self.rotate_gun(5)

    def rotate_gun(self, angle):
        x0, y0, x1, y1 = self.canvas.coords(self.zenitka)
        gx0, gy0, gx1, gy1 = self.canvas.coords(self.gun)
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        angle_rad = math.radians(angle)
        gx0, gy0 = self.rotate_point(gx0, gy0, cx, cy, angle_rad)
        gx1, gy1 = self.rotate_point(gx1, gy1, cx, cy, angle_rad)
        self.canvas.coords(self.gun, gx0, gy0, gx1, gy1)

    def rotate_point(self, x, y, cx, cy, angle):
        x -= cx
        y -= cy
        x_new = x * math.cos(angle) - y * math.sin(angle) + cx
        y_new = x * math.sin(angle) + y * math.cos(angle) + cy
        return x_new, y_new

    def fire_bullet(self, event):
        if time.time() - self.last_shot_time >= 1.0:
            x0, y0, x1, y1 = self.canvas.coords(self.zenitka)
            gx0, gy0, gx1, gy1 = self.canvas.coords(self.gun)
            cx = (x0 + x1) / 2
            cy = (y0 + y1) / 2
            bx = (gx0 + gx1) / 2
            by = (gy0 + gy1) / 2
            bullet_length = math.hypot(gx1 - gx0, gy1 - gy0) / 3
            bullet_angle = math.atan2(gy1 - gy0, gx1 - gx0)
            bullet_end_x = bx + bullet_length * math.cos(bullet_angle)
            bullet_end_y = by + bullet_length * math.sin(bullet_angle)
            bullet = self.canvas.create_line(bx, by, bullet_end_x, bullet_end_y, fill='yellow', width=3)
            self.bullets.append((bullet, bullet_angle))
            self.last_shot_time = time.time()
            self.move_bullet(bullet, bullet_end_x, bullet_end_y, bullet_angle)

    def move_bullet(self, bullet, target_x, target_y, angle):
        if self.canvas.coords(bullet):
            bx, by, _ ,_ = self.canvas.coords(bullet)
            dx = math.cos(angle) * 10
            dy = math.sin(angle) * 10
            if 0 < bx < 1000 and 0 < by < 600:
                self.canvas.move(bullet, dx, dy)
                self.check_bullet_collision(bullet)
                self.root.after(30, self.move_bullet, bullet, target_x, target_y, angle)
            else:
                self.canvas.delete(bullet)
                self.bullets.remove((bullet, angle))
                self.misses += 1
                self.update_misses() 

    def check_bullet_collision(self, bullet):
        for aircraft in self.aircrafts[:]:
            if self.canvas.coords(aircraft) and self.canvas.coords(bullet):
                bx, by, _ ,_ = self.canvas.coords(bullet)
                if self.check_collision(aircraft, bx, by):
                    self.score += 1
                    self.canvas.delete(bullet)
                    self.canvas.delete(aircraft)
                    self.aircrafts.remove(aircraft)
                    self.update_score()
                    return
            else:
                self.canvas.delete(aircraft)
                self.bullets.remove((aircraft))
                self.misses += 1
                self.update_missed()

    def update_game(self):
        for aircraft in self.aircrafts[:]:
            if self.canvas.coords(aircraft):
                self.canvas.move(aircraft, -5, 0)
                if self.check_collision(aircraft):
                    self.score += 1
                    self.canvas.delete(aircraft)
                    self.aircrafts.remove(aircraft)
                    self.update_score()
                else:
                    a_x1, _, _, _ = self.canvas.coords(aircraft)
                    if a_x1 < -50:
                        self.missed += 1
                        self.update_missed()
                        self.canvas.delete(aircraft)
                        self.aircrafts.remove(aircraft)
        self.root.after(50, self.update_game)

    def check_collision(self, aircraft, bx=None, by=None):
        a_x1, a_y1, a_x2, a_y2 = self.canvas.coords(aircraft)
        if bx is not None and by is not None:
            if a_x1 <= bx <= a_x2 and a_y1 <= by <= a_y2:
                return True
        return False

    def update_score(self):
        self.score_label.config(text=f"Збито: {self.score}")

    def update_misses(self):
        self.misses_label.config(text=f"Промахів: {self.misses}")
    
    def update_missed(self):
        self.missed_label.config(text=f"Пропущено: {self.missed}")



if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
