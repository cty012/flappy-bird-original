import pygame
import param as p
from characters import *
import scenes
pygame.init()

screen = pygame.display.set_mode(p.size)
bird = Bird()
obs_list = []
frame = Frame()

flag = 'start'
while flag != 'quit':
    if flag == 'start':
        flag = scenes.start(screen, bird)
    elif flag == 'game':
        flag = scenes.game(screen, bird, obs_list, frame)
    elif flag == 'fail':
        flag = scenes.fail(screen, bird, obs_list)

pygame.quit()
