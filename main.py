import pygame
from pygame.locals import *
import param as p
from characters import *
from utils import *
pygame.init()

screen = pygame.display.set_mode(p.size)
bird = Bird()
obs_list = []
frame = Frame()

run = True
while run:
    # draw
    screen.fill(p.background)
    bird.show(screen)
    for obs in obs_list:
        obs.show(screen)

    # detect collision
    collision = False
    collision = collision or CollisionDetector.detect(bird, frame)
    for obs in obs_list:
        collision = collision or CollisionDetector.detect(bird, obs)
    if collision:
        print("COLLIDE!!!")

    # detect operation
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird.flap()
            print("FLAP!!!")

    # move
    if ObsGenerator.needNewObs(obs_list):
        ObsGenerator.getNewObs(obs_list)
    bird.move()
    for obs in obs_list:
        obs.move()

    pygame.display.update()
    pygame.time.delay(1)

pygame.quit()
