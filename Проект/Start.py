import tkinter as tk
from PIL import Image, ImageTk

from Game import Game


class Start:
    def __init__(self, root):
        self.root = root
        self.root.title("Zenitka Game")
        self.root.geometry("1000x600")
        background_image = Image.open("background2.jpg")
        background_image = background_image.resize((1000, 600), Image.ANTIALIAS)
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.root, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        start_button = tk.Button(self.root, text="Старт", command=self.start_game, width=20, height=1, font=("Helvetica", 16))
        exit_button = tk.Button(self.root, text="Вихід", command=self.root.destroy, width=20, height=1, font=("Helvetica", 16))
        start_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        exit_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def start_game(self):
        game = Game(self.root)