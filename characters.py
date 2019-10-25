import pygame
import param as p


class Frame(pygame.sprite.Sprite):
    def __init__(self):
        pass


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        # Load everything
        pygame.sprite.Sprite.__init__(self)
        # Definition
        self.x = p.pos[0]
        self.y = p.pos[1]
        self.vel = 0
        self.max_vel = p.max_vel
        self.size = p.bird_size
        self.color = (255, 0, 0)

    def flap(self):
        self.vel += p.boost
        if self.vel > self.max_vel:
            self.vel = self.max_vel

    def move(self):
        self.y -= self.vel
        self.vel -= p.gravity
        if self.vel < -self.max_vel:
            self.vel = -self.max_vel

    def show(self, screen):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(screen, self.color, pos, self.size, 0)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, open_pos):
        # Load everything
        pygame.sprite.Sprite.__init__(self)
        # Definition
        self.x = p.size[0]
        self.open_pos = open_pos
        self.vel = p.speed
        self.width = p.obs_width
        self.open_rad = p.open_rad
        self.color = (0, 0, 255)

    def move(self):
        self.x -= self.vel

    def show(self, screen):
        rect1 = ((self.x, 0), (self.width, self.open_pos - self.open_rad))
        rect2 = ((self.x, self.open_pos + self.open_rad), (self.width, p.size[1] - self.open_pos - self.open_rad))
        pygame.draw.rect(screen, self.color, rect1, 0)
        pygame.draw.rect(screen, self.color, rect2, 0)
