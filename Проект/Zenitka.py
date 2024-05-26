import tkinter as tk


class Zenitka:
    def __init__(self, game):
        self.game = game
        self.image = tk.PhotoImage(file="zenitka.png").subsample(16, 16)
        self.id = self.game.canvas.create_image(375, 552, anchor=tk.NW, image=self.image)
