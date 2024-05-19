import tkinter as tk
import pygame
import random


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

    def move(self):
        if self.game.paused:
            return
        if self.game.canvas.coords(self.id):
            self.game.canvas.move(self.id, -self.speed, 0)
            if self.check_off_screen():
                self.game.missed += 1
                self.game.update_missed()
                self.sound.stop()
                self.game.canvas.delete(self.id)
                self.game.aircrafts.remove(self)

    def check_off_screen(self):
        a_x1, _ = self.game.canvas.coords(self.id)
        return a_x1 < -80