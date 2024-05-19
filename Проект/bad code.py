import tkinter as tk
import pygame
import random
import math
import time
from PIL import Image, ImageTk

class Game:
    def __init__(self, root):
        pygame.mixer.init()
        self.root = root
        self.paused = False
        self.canvas = tk.Canvas(root, width=1000, height=600, bg='white')
        self.canvas.pack()
        background_image = Image.open("background.png")
        self.background_photo = ImageTk.PhotoImage(background_image.resize((1010, 610)))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.score = 0
        self.misses = 0
        self.missed = 0
        self.aircrafts = []
        self.aircraft_sounds = {}
        self.bullets = []
        self.aircraft_images = []
        self.explosion_images = []
        self.scaled_explosion_images = []
        self.load_explosion_images()
        self.last_shot_time = time.time()
        self.create_aircraft_timer = None
        self.update_game_timer = None
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
        self.pause_button = tk.Button(root, text="Пауза", command=self.pause_game, width=10, height=1, font=("Helvetica", 8))
        self.pause_button.place(relx=0.05, rely=0.04, anchor=tk.CENTER)
        self.exit_button = tk.Button(root, text="Вихід", command=root.destroy, width=10, height=1, font=("Helvetica", 8))
        self.exit_button.place(relx=0.13, rely=0.04, anchor=tk.CENTER)
        self.shot_sound = pygame.mixer.Sound("shot.mp3")
        self.pause_window = None
        self.running = True
        self.update_game()

    def pause_game(self):
        pygame.mixer.pause()
        self.root.after_cancel(self.update_game_timer)
        self.root.after_cancel(self.create_aircraft_timer)
        if not self.pause_window:
            self.paused = True
            self.pause_window = tk.Toplevel(self.root)
            self.pause_window.title("Pause")
            self.pause_window.geometry("500x300")
            background_image = Image.open("background3.jpg")
            background_image = background_image.resize((500, 300), Image.ANTIALIAS)
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(self.pause_window, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_photo
            pause_label = tk.Label(self.pause_window, text="Гра на паузі", font=("Helvetica", 20), bg='white')
            pause_label.pack(pady=20)
            resume_button = tk.Button(self.pause_window, text="Повернутись до гри", command=self.resume_game, width=20, height=2, font=("Helvetica", 9))
            resume_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
            exit_button = tk.Button(self.pause_window, text="Вийти", command=self.quit_game, width=20, height=2, font=("Helvetica", 9))
            exit_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
            self.pause_window.transient(self.root)
            self.pause_window.grab_set()
            self.root.wait_window(self.pause_window)
            self.pause_window = None            

    def resume_game(self):
        self.paused = False
        if self.pause_window:
            self.pause_window.destroy()
            self.pause_window = None
            self.update_game()
            pygame.mixer.unpause()
            self.create_aircraft_timer = self.root.after(random.randint(100, 10000), self.create_aircraft)

    def quit_game(self):
        self.root.destroy()

    def stop_sounds(self):
        for sound in self.aircraft_sounds.values():
            sound.stop()

    def start_sounds(self):
        for aircraft, sound in self.aircraft_sounds.items():
            if self.canvas.coords(aircraft):
                sound.play()

    def load_explosion_images(self):
        explosion = Image.open("explosion.gif")
        self.explosion_images = []
        self.scaled_explosion_images = []
        scaled_size = (explosion.width // 10, explosion.height // 10)

        for frame in range(explosion.n_frames):
            explosion.seek(frame)
            frame_image = explosion.copy()
            self.explosion_images.append(ImageTk.PhotoImage(frame_image))
            
            scaled_frame_image = frame_image.resize(scaled_size, Image.ANTIALIAS)
            self.scaled_explosion_images.append(ImageTk.PhotoImage(scaled_frame_image))

    def create_aircraft(self):
        if not self.paused:
            y = random.randint(60, 400)
            aircraft_image = tk.PhotoImage(file="aircraft.png").subsample(8, 8)
            aircraft = self.canvas.create_image(1000, y, anchor=tk.NW, image=aircraft_image)
            self.speed = random.uniform(5, 13)
            self.aircrafts.append((aircraft, self.speed))
            self.aircraft_images.append(aircraft_image)
            self.create_aircraft_timer = self.root.after(random.randint(100, 10000), self.create_aircraft)
            self.aircraft_sound = pygame.mixer.Sound("Aircraft sound.mp3").play()
            self.aircraft_sounds[aircraft] = self.aircraft_sound

    def create_zenitka(self):
        self.zenitka_image = tk.PhotoImage(file="zenitka.png").subsample(16, 16)
        self.zenitka = self.canvas.create_image(375, 555, anchor=tk.NW, image=self.zenitka_image)

    def create_gun(self):
        self.gun = self.canvas.create_line(425, 570, 425, 520, fill='black', width=3)
        x0, y0 = 427 - 5, 570 - 5
        x1, y1 = 427 + 5, 570 + 5
        self.circle = self.canvas.create_oval(x0, y0, x1, y1, fill='gray')

    def move_gun(self, event):
        if not self.paused:
            key = event.keysym
            if key == 'Left':
                self.rotate_gun(-5)
            elif key == 'Right':
                self.rotate_gun(5)

    def rotate_gun(self, angle):
        cx, cy = 427, 570
        gx0, gy0, gx1, gy1 = self.canvas.coords(self.gun)
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
        if not self.paused and time.time() - self.last_shot_time >= 1.2:
            gx0, gy0, gx1, gy1 = self.canvas.coords(self.gun)
            bx = (gx0 + gx1) / 2
            by = (gy0 + gy1) / 2
            bullet_length = math.hypot(gx1 - gx0, gy1 - gy0) / 3
            bullet_angle = math.atan2(gy1 - gy0, gx1 - gx0)
            bullet_end_x = bx + bullet_length * math.cos(bullet_angle)
            bullet_end_y = by + bullet_length * math.sin(bullet_angle)
            bullet_width = min(4, bullet_length)
            bullet = self.canvas.create_oval(bx - bullet_width / 2, by - bullet_width / 2, bx + bullet_width / 2, by + bullet_width / 2, fill='yellow')
            self.bullets.append((bullet, bullet_angle))
            self.create_and_remove_explosion(gx1, gy1)
            self.last_shot_time = time.time()
            self.shot_sound.play()
            self.crash_sound = pygame.mixer.Sound("Crash.mp3")
            self.move_bullet(bullet, bullet_end_x, bullet_end_y, bullet_angle)

    def create_and_remove_explosion(self, x, y):
        explosion_id = self.canvas.create_image(x, y, anchor=tk.CENTER, image=self.scaled_explosion_images[0])
        half_frames = len(self.scaled_explosion_images) // 2
        self.animate_explosion(explosion_id, 0, half_frames, scaled=True)

    def animate_explosion(self, explosion_id, frame, max_frames, scaled=False):
        images = self.scaled_explosion_images if scaled else self.explosion_images
        if frame < max_frames:
            self.canvas.itemconfig(explosion_id, image=images[frame])
            self.root.after(100, self.animate_explosion, explosion_id, frame + 1, max_frames, scaled)
        else:
            self.canvas.delete(explosion_id)

    def move_bullet(self, bullet, target_x, target_y, angle):
        if not self.paused and self.canvas.coords(bullet):
            bx, by, _, _ = self.canvas.coords(bullet)
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
        bx, by, _, _ = self.canvas.coords(bullet)
        bullet_center = (bx, by)
        bullet_radius = 2
        for i, (aircraft, self.speed) in enumerate(self.aircrafts[:]):
            if self.canvas.coords(aircraft):
                ax, ay = self.canvas.coords(aircraft)
                aircraft_image = self.aircraft_images[i]
                aircraft_center = ((ax + ax + aircraft_image.width()) / 2, (ay + ay + aircraft_image.height()) / 2)
                aircraft_radius = max(aircraft_image.width(), aircraft_image.height()) / 2
                distance = math.hypot(bullet_center[0] - aircraft_center[0], bullet_center[1] - aircraft_center[1])
                if distance < bullet_radius + aircraft_radius:
                    self.score += 1
                    self.create_collision_point(bx, by)
                    self.canvas.delete(bullet)
                    self.canvas.delete(aircraft)
                    self.aircrafts.remove((aircraft, self.speed))
                    self.aircraft_images.remove(aircraft_image)
                    self.update_score()
                    self.crash_sound.play()
                    self.aircraft_sounds[aircraft].stop()
                    return
            else:
                self.canvas.delete(aircraft)
                self.bullets.remove((aircraft, self.speed))
                self.misses += 1
                self.update_missed()

    def create_collision_point(self, x, y):
        explosion_id = self.canvas.create_image(x, y, anchor=tk.CENTER, image=self.explosion_images[0])
        half_frames = len(self.explosion_images) // 2
        self.animate_explosion(explosion_id, 0, half_frames, scaled=False)

    def update_game(self):
        if not self.paused:
            for aircraft, self.speed in self.aircrafts[:]:
                if self.canvas.coords(aircraft):
                    self.canvas.move(aircraft, -self.speed, 0)
                    if self.check_collision(aircraft):
                        self.score += 1
                        self.canvas.delete(aircraft)
                        self.aircrafts.remove((aircraft, self.speed))
                        self.update_score()
                    else:
                        a_x1, _ = self.canvas.coords(aircraft)
                        if a_x1 < -80:
                            self.missed += 1
                            self.update_missed()
                            self.aircraft_sounds[aircraft].stop()
                            self.canvas.delete(aircraft)
                            self.aircrafts.remove((aircraft, self.speed))
            self.update_game_timer = self.root.after(50, self.update_game)

    def check_collision(self, aircraft, bx=None, by=None):
        a_x1, a_y1 = self.canvas.coords(aircraft)
        a_x2 = a_x1 + self.aircraft_images[self.aircrafts.index((aircraft, self.speed))].width() // 11
        a_y2 = a_y1 + self.aircraft_images[self.aircrafts.index((aircraft, self.speed))].height() // 11
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
    def start_game(root):
        game = Game(root)
    root = tk.Tk()
    root.title("Zenitka Game")
    root.geometry("1000x600")
    background_image = Image.open("background2.jpg")
    background_image = background_image.resize((1000, 600), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_button = tk.Button(root, text="Старт", command=lambda: start_game(root), width=20, height=1, font=("Helvetica", 16))
    exit_button = tk.Button(root, text="Вихід", command=root.destroy, width=20, height=1, font=("Helvetica", 16))
    start_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    exit_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    root.mainloop()