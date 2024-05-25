import tkinter as tk
import random

class Engine:
    def __init__(self, aircraft):
        self.aircraft = aircraft
        self.game = aircraft.game
        self.engine_images = self.game.graphics.engine_gif
        self.crashed_engine_images = self.game.graphics.crashed_engine_gif
        self.smoke_images = self.game.graphics.smoke_gif
        self.engine_id = None
        self.smoke_id = None
        self.animate_engine(0)

    def animate(self, engine_x, engine_y):
        if not self.engine_id:
            self.engine_id = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.engine_images[0])
        else:
            self.game.canvas.coords(self.engine_id, engine_x, engine_y)
            self.game.canvas.itemconfig(self.engine_id, image=self.engine_images[0])
        self.animate_engine(0)

    def animate_engine(self, frame):
        position = self.aircraft.get_engine_position()
        if position and not self.aircraft.crashed:
            engine_x, engine_y = position
            self.game.canvas.itemconfig(self.engine_id, image=self.engine_images[frame])
            frame = (frame + 1) % len(self.engine_images)
            self.game.root.after(100, self.animate_engine, frame)
        elif self.engine_id:
            self.game.canvas.delete(self.engine_id)
            self.engine_id = None

    def animate_crashed(self, engine_x, engine_y):
        if not self.engine_id:
            self.engine_id = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.crashed_engine_images[0])
        else:
            self.game.canvas.coords(self.engine_id, engine_x, engine_y)
            self.game.canvas.itemconfig(self.engine_id, image=self.crashed_engine_images[0])
        self.animate_crashed_engine(0)

    def animate_crashed_engine(self, frame):
        position = self.aircraft.get_engine_position()
        if position:
            engine_x, engine_y = position
            self.game.canvas.itemconfig(self.engine_id, image=self.crashed_engine_images[frame])
            frame = (frame + 1) % len(self.crashed_engine_images)
            self.game.root.after(100, self.animate_crashed_engine, frame)
        elif self.engine_id:
            self.game.canvas.delete(self.engine_id)
            self.engine_id = None
    
    def animate_smoke(self, frame):
        position = self.aircraft.get_engine_position()
        if position:
            engine_x, engine_y = position
            if not self.smoke_id:
                self.smoke_id = self.game.canvas.create_image(engine_x + 30, engine_y, anchor=tk.CENTER, image=self.smoke_images[frame])
            else:
                self.game.canvas.coords(self.smoke_id, engine_x + random.uniform(0, 50), engine_y)
                self.game.canvas.itemconfig(self.smoke_id, image=self.smoke_images[frame])
            frame = (frame + 1) % len(self.smoke_images)
            self.game.root.after(100, self.animate_smoke, frame)
        else:
            if self.smoke_id:
                self.game.canvas.delete(self.smoke_id)
                self.smoke_id = None

    def remove(self):
        if self.engine_id:
            self.game.canvas.delete(self.engine_id)
        if self.smoke_id:
            self.game.canvas.delete(self.smoke_id)
