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
        self.vel = p.init_vel
        self.max_vel = p.max_vel
        self.size = p.bird_size
        self.color = (255, 0, 0)

    def flap(self):
        self.vel += p.boost
        if self.vel > self.max_vel:
            self.vel = self.max_vel

    def move(self, dT):
        self.y -= self.vel * dT
        self.vel -= p.gravity * dT
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
        self.scores = False

    def move(self, dT):
        self.x -= self.vel * dT

    def score(self):
        if not self.scores and self.x + 0.5 * self.width + 2 * p.bird_size < p.pos[0]:
            self.scores = True
            return True
        return False

    def show(self, screen):
        rect1 = ((self.x, 0), (self.width, self.open_pos - self.open_rad))
        rect2 = ((self.x, self.open_pos + self.open_rad), (self.width, p.size[1] - self.open_pos - self.open_rad))
        pygame.draw.rect(screen, self.color, rect1, 0)
        pygame.draw.rect(screen, self.color, rect2, 0)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.pos = p.scoreboard_pos
        self.size = p.scoreboard_size

    def gain_point(self):
        self.score += 1

    def save_score(self):
        self.max_score = max(self.score, self.max_score)

    def refresh(self):
        self.score = 0

    def show(self, screen):
        rect = (self.pos, self.size)
        pygame.draw.rect(screen, p.background, rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        pos1 = (self.pos[0] + p.score_dist[0], self.pos[1] + p.score_dist[1])
        pos2 = (self.pos[0] + p.maxscore_dist[0], self.pos[1] + p.maxscore_dist[1])
        text1 = pygame.font.Font(p.font, 25)\
            .render('Score: {}'.format(self.score), True, (0, 0, 0))
        text2 = pygame.font.Font(p.font, 25) \
            .render('Highest score: {}'.format(self.max_score), True, (0, 0, 0))
        screen.blit(text1, pos1)
        screen.blit(text2, pos2)
