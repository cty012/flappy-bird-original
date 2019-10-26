from random import Random
import param as p
from characters import *
import pygame


def sqrDist(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2


def init(bird, obs_list, scoreboard):
    bird.vel = p.init_vel
    bird.y = p.pos[1]
    obs_list *= 0
    scoreboard.refresh()


def showText(screen, text, pos, font_name, font_size, color):
    font = pygame.font.Font(font_name, font_size)
    textMsg = font.render(text, True, color)
    rect = textMsg.get_rect()
    rect.center = pos
    screen.blit(textMsg, rect)


class CollisionDetector:
    @staticmethod
    def detect(obj1, obj2):
        if isinstance(obj1, Bird) and isinstance(obj2, Obstacle):
            xcenter = (obj2.x + 0.5 * obj2.width)
            # if center within boundary created by obstacle
            if abs(obj1.x - xcenter) <= 0.5 * obj2.width:
                return abs(obj1.y - obj2.open_pos) >= obj2.open_rad - obj1.size
            # if center not within boundary created by obstacle
            elif abs(obj1.x - xcenter) <= obj1.size + 0.5 * obj2.width:
                # if aligned with opening
                if abs(obj1.y - obj2.open_pos) < obj2.open_rad:
                    y1 = obj2.open_rad - abs(obj1.y - obj2.open_pos)
                    x1 = abs(obj1.x - xcenter) - 0.5 * obj2.width
                    r1 = obj1.size
                    return x1 ** 2 + y1 ** 2 <= r1 ** 2
                # if not aligned with opening
                else:
                    return True
        elif isinstance(obj1, Bird) and isinstance(obj2, Frame):
            return obj1.y - obj1.size <= 0 or obj1.y + obj1.size >= p.size[1]
        return False


class ObsGenerator:
    @staticmethod
    def needNewObs(obs_list):
        return len(obs_list) == 0 or obs_list[-1].x + p.obs_interval <= p.size[0]

    @staticmethod
    def getNewObs(obs_list):
        open_pos = Random().randrange(int(0.1 * (p.size[1] - 2 * p.open_rad) + p.open_rad),
                                      int(0.9 * (p.size[1] - 2 * p.open_rad) + p.open_rad))
        if len(obs_list) == 0 or obs_list[0].x + obs_list[0].width > 0:
            obs = Obstacle(open_pos)
        else:
            obs = obs_list.pop(0)
            obs.x = p.size[0]
            obs.open_pos = open_pos
            obs.scores = False
        obs_list.append(obs)
