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

        self.engine_images = self.game.graphics.engine_gif
        self.engine_id = None
        self.animate_engine(0)
    
    def get_engine_position(self):
        coords = self.game.canvas.coords(self.id)
        if not coords:
            return None
        a_x1, a_y1 = self.game.canvas.coords(self.id)
        engine_x = a_x1 + 122
        engine_y = a_y1 + self.image.height() // 2 + 5
        return engine_x, engine_y
    
    def animate_engine(self, frame):
        position = self.get_engine_position()
        if position:
            engine_x, engine_y = position
            if not self.engine_id:
                self.engine_id = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.engine_images[frame])
            else:
                self.game.canvas.coords(self.engine_id, engine_x, engine_y)
                self.game.canvas.itemconfig(self.engine_id, image=self.engine_images[frame])
            frame = (frame + 1) % len(self.engine_images)
            self.game.root.after(100, self.animate_engine, frame)
        else:
            if self.engine_id:
                self.game.canvas.delete(self.engine_id)
                self.engine_id = None

    def move(self):
        if self.game.paused:
            return
        if self.game.canvas.coords(self.id):
            self.game.canvas.move(self.id, -self.speed, 0)
            position = self.get_engine_position()
            if position:
                engine_x, engine_y = position
                self.game.canvas.coords(self.engine_id, engine_x, engine_y)
            if self.check_off_screen():
                self.game.missed += 1
                self.game.update_missed()
                self.sound.stop()
                self.game.canvas.delete(self.id)
                if self.engine_id:
                    self.game.canvas.delete(self.engine_id)
                self.game.aircrafts.remove(self)

    def check_off_screen(self):
        coords = self.game.canvas.coords(self.id)
        if not coords:
            return False
        a_x1, _ = coords
        return a_x1 < -133