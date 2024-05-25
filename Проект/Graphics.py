import tkinter as tk
from PIL import Image, ImageTk


class Graphics:
    def __init__(self, game):
        self.game = game
        self.background_image = Image.open("background.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((1010, 610)))
        self.game.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.score_label = tk.Label(game.root, text="Збито: 0", font=("Helvetica", 16))
        self.score_label.place(x=800, y=20)
        self.misses_label = tk.Label(game.root, text="Промахів: 0", font=("Helvetica", 16))
        self.misses_label.place(x=800, y=50)
        self.missed_label = tk.Label(game.root, text="Пропущено: 0", font=("Helvetica", 16))
        self.missed_label.place(x=800, y=80)
        self.pause_button = tk.Button(game.root, text="Пауза", command=game.pause.pause_game, width=10, height=1, font=("Helvetica", 8))
        self.pause_button.place(relx=0.05, rely=0.04, anchor=tk.CENTER)
        self.exit_button = tk.Button(game.root, text="Вихід", command=game.root.destroy, width=10, height=1, font=("Helvetica", 8))
        self.exit_button.place(relx=0.13, rely=0.04, anchor=tk.CENTER)
        self.explosion_images = []
        self.scaled_explosion_images = []
        self.load_explosion_images()
        self.engine_gif = self.load_engine_gif()
        self.crashed_engine_gif = self.load_crashed_engine_gif()
        self.smoke_gif = self.load_smoke_gif()
    
    def load_smoke_gif(self):
        smoke_gif = Image.open("Smoke.gif")
        smoke_frames = []
        try:
            while True:
                frame = smoke_gif.copy()
                scaled_size = (165, 45)
                frame = frame.resize(scaled_size, Image.Resampling.LANCZOS)
                smoke_frames.append(ImageTk.PhotoImage(frame))
                smoke_gif.seek(len(smoke_frames))
        except EOFError:
            pass
        return smoke_frames

    def load_engine_gif(self):
        engine_gif = Image.open("Engine.gif")
        engine_frames = []
        try:
            while True:
                frame = engine_gif.copy()
                scaled_size = (50, 15)
                frame = frame.resize(scaled_size, Image.Resampling.LANCZOS)
                engine_frames.append(ImageTk.PhotoImage(frame))
                engine_gif.seek(len(engine_frames))
        except EOFError:
            pass
        return engine_frames

    def load_crashed_engine_gif(self):
        crashed_engine_gif = Image.open("Crashed engine.gif")
        crashed_engine_frames = []
        try:
            while True:
                frame = crashed_engine_gif.copy()
                scaled_size = (50, 15)
                frame = frame.resize(scaled_size, Image.Resampling.LANCZOS)
                crashed_engine_frames.append(ImageTk.PhotoImage(frame))
                crashed_engine_gif.seek(len(crashed_engine_frames))
        except EOFError:
            pass
        return crashed_engine_frames

    def load_explosion_images(self):
        explosion = Image.open("explosion.gif")
        self.explosion_images = []
        self.scaled_explosion_images = []
        scaled_size = (explosion.width // 10, explosion.height // 10)
        for frame in range(explosion.n_frames):
            explosion.seek(frame)
            frame_image = explosion.copy()
            self.explosion_images.append(ImageTk.PhotoImage(frame_image))
            scaled_frame_image = frame_image.resize(scaled_size, Image.Resampling.LANCZOS)
            self.scaled_explosion_images.append(ImageTk.PhotoImage(scaled_frame_image))

    def create_and_remove_explosion(self, x, y):
        explosion_id = self.game.canvas.create_image(x, y, anchor=tk.CENTER, image=self.scaled_explosion_images[0])
        half_frames = len(self.scaled_explosion_images) // 2
        self.animate_explosion(explosion_id, 0, half_frames, scaled=True)

    def animate_explosion(self, explosion_id, frame, max_frames, scaled=False):
        if self.game.paused:
            self.game.explosions.append((explosion_id, frame, max_frames, scaled))
            return
        images = self.scaled_explosion_images if scaled else self.explosion_images
        if frame < max_frames:
            self.game.canvas.itemconfig(explosion_id, image=images[frame])
            self.game.root.after(100, self.animate_explosion, explosion_id, frame + 1, max_frames, scaled)
        else:
            self.game.canvas.delete(explosion_id)

    def create_collision_point(self, x, y):
        explosion_id = self.game.canvas.create_image(x, y, anchor=tk.CENTER, image=self.explosion_images[0])
        half_frames = len(self.explosion_images) // 2
        self.animate_explosion(explosion_id, 0, half_frames, scaled=False)