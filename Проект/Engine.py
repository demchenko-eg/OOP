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
        self.smoke_id2 = None
        self.engine_animation = None
        self.crashed_animation = None
        self.smoke_animation = None
        self.smoke_animation2 = None
        self.current_engine_frame = 0
        self.current_crashed_frame = 0
        self.current_smoke_frame = 0
        self.animate_engine(0)

    def animate(self, engine_x, engine_y):
        if not self.engine_id:
            self.engine_id = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.engine_images[0])
        else:
            self.game.canvas.coords(self.engine_id, engine_x, engine_y)
            self.game.canvas.itemconfig(self.engine_id, image=self.engine_images[self.current_engine_frame])
        self.animate_engine(self.current_engine_frame)

    def animate_engine(self, frame):
        if self.game.paused:
            self.current_engine_frame = frame
            return
        position = self.aircraft.get_engine_position()
        if position and not self.aircraft.crashed:
            engine_x, engine_y = position
            self.game.canvas.itemconfig(self.engine_id, image=self.engine_images[frame])
            frame = (frame + 1) % len(self.engine_images)
            self.engine_animation = self.game.root.after(100, self.animate_engine, frame)
        elif self.engine_id:
            self.game.canvas.delete(self.engine_id)
            self.engine_id = None

    def animate_crashed(self, engine_x, engine_y):
        if not self.engine_id:
            self.engine_id = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.crashed_engine_images[0])
        else:
            self.game.canvas.coords(self.engine_id, engine_x, engine_y)
            self.game.canvas.itemconfig(self.engine_id, image=self.crashed_engine_images[self.current_crashed_frame])
        self.animate_crashed_engine(self.current_crashed_frame)

    def animate_crashed_engine(self, frame):
        if self.game.paused:
            self.current_crashed_frame = frame
            return
        position = self.aircraft.get_engine_position()
        if position:
            engine_x, engine_y = position
            self.game.canvas.itemconfig(self.engine_id, image=self.crashed_engine_images[frame])
            frame = (frame + 1) % len(self.crashed_engine_images)
            self.crashed_animation = self.game.root.after(100, self.animate_crashed_engine, frame)
        elif self.engine_id:
            self.game.canvas.delete(self.engine_id)
            self.engine_id = None

    def animate_smoke(self, frame):
        if self.game.paused:
            self.current_smoke_frame = frame
            return
        position = self.aircraft.get_engine_position()
        if position:
            engine_x, engine_y = position
            if not self.smoke_id:
                self.smoke_id = self.game.canvas.create_image(engine_x-30, engine_y, anchor=tk.CENTER, image=self.smoke_images[frame])
                self.smoke_id2 = self.game.canvas.create_image(engine_x, engine_y, anchor=tk.CENTER, image=self.smoke_images[frame])  # Створення другого диму
            else:
                self.game.canvas.coords(self.smoke_id, engine_x - 30 + random.uniform(0, 50), engine_y)
                self.game.canvas.coords(self.smoke_id2, engine_x + random.uniform(0, 50), engine_y)  # Координати для другого диму
                self.game.canvas.itemconfig(self.smoke_id, image=self.smoke_images[frame])
                self.game.canvas.itemconfig(self.smoke_id2, image=self.smoke_images[frame])  # Зміна кадру другого диму
            frame = (frame + 1) % len(self.smoke_images)
            self.smoke_animation = self.game.root.after(100, self.animate_smoke, frame)
        else:
            if self.smoke_id:
                self.game.canvas.delete(self.smoke_id)
                self.smoke_id = None
            if self.smoke_id2:
                self.game.canvas.delete(self.smoke_id2)
                self.smoke_id2 = None

    def remove(self):
        if self.engine_id:
            self.game.canvas.delete(self.engine_id)
        if self.smoke_id:
            self.game.canvas.delete(self.smoke_id)
        if self.smoke_id2:
            self.game.canvas.delete(self.smoke_id2)
        if self.engine_animation:
            self.game.root.after_cancel(self.engine_animation)
        if self.crashed_animation:
            self.game.root.after_cancel(self.crashed_animation)
        if self.smoke_animation:
            self.game.root.after_cancel(self.smoke_animation)
        if self.smoke_animation2:
            self.game.root.after_cancel(self.smoke_animation2)
