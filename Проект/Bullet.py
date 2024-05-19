import math


class Bullet:
    def __init__(self, game, gx1, gy1):
        self.game = game
        self.bx = (gx1 + 425) / 2
        self.by = (gy1 + 570) / 2
        self.angle = math.atan2(gy1 - 570, gx1 - 425)
        bullet_length = math.hypot(gx1 - 425, gy1 - 570) / 3
        bullet_width = min(4, bullet_length)
        self.id = self.game.canvas.create_oval(self.bx - bullet_width / 2, self.by - bullet_width / 2, self.bx + bullet_width / 2, self.by + bullet_width / 2, fill='yellow')
        self.game.bullets.append(self)
        self.game.graphics.create_and_remove_explosion(gx1, gy1)
        self.game.shot_sound.play()
        self.move()

    def check_collision(self):
        bx, by, _, _ = self.game.canvas.coords(self.id)
        bullet_center = (bx, by)
        bullet_radius = 2
        for aircraft in self.game.aircrafts[:]:
            if self.game.canvas.coords(aircraft.id):
                ax, ay = self.game.canvas.coords(aircraft.id)
                aircraft_center = ((ax + ax + aircraft.image.width()) / 2, (ay + ay + aircraft.image.height()) / 2)
                aircraft_radius = max(aircraft.image.width(), aircraft.image.height()) / 2
                distance = math.hypot(bullet_center[0] - aircraft_center[0], bullet_center[1] - aircraft_center[1])
                if distance < bullet_radius + aircraft_radius:
                    self.game.score += 1
                    self.game.graphics.create_collision_point(bx, by)
                    self.game.canvas.delete(self.id)
                    self.game.canvas.delete(aircraft.id)
                    self.game.aircrafts.remove(aircraft)
                    self.game.update_score()
                    self.game.crash_sound.play()
                    self.game.aircraft_sounds[aircraft.id].stop()
                    return True
            else:
                self.game.canvas.delete(aircraft.id)
                self.game.aircrafts.remove(aircraft)
                self.game.misses += 1
                self.game.update_misses()

    def move(self):
        if self.game.paused:
            return
        bx, by, _, _ = self.game.canvas.coords(self.id)
        dx = math.cos(self.angle) * 10
        dy = math.sin(self.angle) * 10
        if 0 < bx < 1000 and 0 < by < 600:
            self.game.canvas.move(self.id, dx, dy)
            if not self.check_collision():
                self.game.root.after(30, self.move)
        else:
            self.game.canvas.delete(self.id)
            self.game.bullets.remove(self)
            self.game.misses += 1
            self.game.update_misses()