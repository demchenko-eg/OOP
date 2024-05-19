import tkinter as tk
import pygame
import random
from PIL import Image, ImageTk


class Pause:
    def __init__(self, game):
        self.game = game
        self.window = None

    def pause_game(self):
        pygame.mixer.pause()
        self.game.root.after_cancel(self.game.update_game_timer)
        self.game.root.after_cancel(self.game.create_aircraft_timer)
        if not self.window:
            self.game.paused = True
            self.window = tk.Toplevel(self.game.root)
            self.window.title("Pause")
            self.window.geometry("500x300")
            background_image = Image.open("background3.jpg")
            background_image = background_image.resize((500, 300), Image.ANTIALIAS)
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(self.window, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_photo
            pause_label = tk.Label(self.window, text="Гра на паузі", font=("Helvetica", 20), bg='white')
            pause_label.pack(pady=20)
            resume_button = tk.Button(self.window, text="Повернутись до гри", command=self.resume_game, width=20, height=2, font=("Helvetica", 9))
            resume_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
            exit_button = tk.Button(self.window, text="Вийти", command=self.game.root.destroy, width=20, height=2, font=("Helvetica", 9))
            exit_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
            self.window.transient(self.game.root)
            self.window.grab_set()
            self.game.root.wait_window(self.window)
            self.window = None

    def resume_game(self):
        self.game.paused = False
        if self.window:
            self.window.destroy()
            self.window = None
            self.game.update_game()
            pygame.mixer.unpause()
            self.game.create_aircraft_timer = self.game.root.after(random.randint(100, 10000), self.game.create_aircraft)
            for bullet in self.game.bullets[:]:
                if self.game.canvas.coords(bullet.id):
                    bullet.move()