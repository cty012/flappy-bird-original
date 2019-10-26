import pygame
import param as p
from characters import *
import scenes
pygame.init()

screen = pygame.display.set_mode(p.size)
clock = pygame.time.Clock()
bird = Bird()
obs_list = []
frame = Frame()
scoreboard = Scoreboard()

flag = 'start'
while flag != 'quit':
    if flag == 'start':
        flag = scenes.start(screen, clock, bird)
    elif flag == 'game':
        flag = scenes.game(screen, clock, bird, obs_list, frame, scoreboard)
    elif flag == 'pause':
        flag = scenes.pause(screen, clock)
    elif flag == 'fail':
        flag = scenes.fail(screen, clock, bird, obs_list, scoreboard)

pygame.quit()
