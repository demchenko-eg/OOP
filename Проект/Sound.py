import pygame


class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.shot_sound = pygame.mixer.Sound("Shot.mp3")
        self.crash_sound = pygame.mixer.Sound("Crash.mp3")
        self.aircraft_sound = pygame.mixer.Sound("Aircraft sound.mp3")
        self.crashed_aircraft_sound = pygame.mixer.Sound("Crashed aircraft.mp3")
        self.smash_sound = pygame.mixer.Sound("Smash.mp3")