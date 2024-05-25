import tkinter as tk
import pygame
import random

from Engine import Engine

class Aircraft:
    def __init__(self, game, speed, sound):
        self.game = game
        self.speed = speed
        self.sound = sound
        y = random.randint(60, 400)
        self.image = tk.PhotoImage(file="aircraft.png").subsample(8, 8)
        self.id = self.game.canvas.create_image(1000, y, anchor=tk.NW, image=self.image)
        self.sound = pygame.mixer.Sound("Aircraft sound.mp3")
        self.sound.play()
        self.game.aircrafts.append(self)
        self.game.aircraft_sounds[self.id] = self.sound
        self.crashed = False
        self.engine = Engine(self)
        self.iteration_count = 0

    def get_engine_position(self):
        coords = self.game.canvas.coords(self.id)
        if not coords:
            return None
        a_x1, a_y1 = coords
        engine_x = a_x1 + 122
        engine_y = a_y1 + self.image.height() // 2 + 5
        return engine_x, engine_y

    def move(self):
        if self.game.paused:
            return
        if self.game.canvas.coords(self.id):
            self.iteration_count += 1
            dx = -self.speed
            dy = 0
            if self.crashed:
                dy = random.uniform(1, 2)
            self.game.canvas.move(self.id, dx, dy)
            position = self.get_engine_position()
            if position:
                engine_x, engine_y = position
                if self.crashed:
                    self.engine.animate_crashed(engine_x, engine_y)
                    self.engine.animate_smoke(0)
                else:
                    self.engine.animate(engine_x, engine_y)
            if self.check_off_screen():
                if not self.crashed:
                    self.game.missed += 1
                    self.game.update_missed()
                self.remove_aircraft()

    def check_off_screen(self):
        coords = self.game.canvas.coords(self.id)
        if not coords:
            return False
        a_x1, _ = coords
        return a_x1 < -250

    def remove_aircraft(self):
        self.sound.stop()
        self.game.canvas.delete(self.id)
        self.engine.remove()
        self.game.aircrafts.remove(self)