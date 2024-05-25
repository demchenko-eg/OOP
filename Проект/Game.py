import tkinter as tk
import random
import time

from Pause import Pause
from Aircraft import Aircraft
from Zenitka import Zenitka
from Gun import Gun
from Bullet import Bullet
from Sound import Sound
from Graphics import Graphics


class Game:
    def __init__(self, root):
        Sound.__init__(self, Game)
        self.root = root
        self.paused = False
        self.canvas = tk.Canvas(root, width=1000, height=600, bg='white')
        self.canvas.pack()
        self.score = 0
        self.misses = 0
        self.missed = 0
        self.aircrafts = []
        self.aircraft_sounds = {}
        self.bullets = []
        self.aircraft_images = []
        self.last_shot_time = time.time()
        self.create_aircraft_timer = None
        self.update_game_timer = None
        self.pause = Pause(self)
        self.graphics = Graphics(self)
        self.create_aircraft()
        self.zenitka = Zenitka(self)
        self.gun = Gun(self)
        self.canvas.bind("<KeyPress>", self.gun.move)
        self.canvas.bind("<space>", self.fire_bullet)
        self.canvas.focus_set()
        self.update_game()

    def create_aircraft(self):
        if not self.paused:
            speed = random.uniform(8, 13)
            aircraft = Aircraft(self, speed, self.aircraft_sound)
            self.create_aircraft_timer = self.root.after(random.randint(100, 11000), self.create_aircraft)

    def fire_bullet(self, event):
        if not self.paused and time.time() - self.last_shot_time >= 1.2:
            _, _, gx1, gy1 = self.canvas.coords(self.gun.id)
            Bullet(self, gx1, gy1)
            self.last_shot_time = time.time()

    def update_game(self):
        if not self.paused:
            for aircraft in self.aircrafts[:]:
                aircraft.move()
            self.update_game_timer = self.root.after(50, self.update_game)

    def update_score(self):
        self.graphics.score_label.config(text=f"Збито: {self.score}")

    def update_misses(self):
        self.graphics.misses_label.config(text=f"Промахів: {self.misses}")

    def update_missed(self):
        self.graphics.missed_label.config(text=f"Пропущено: {self.missed}")