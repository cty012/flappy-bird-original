import pygame
from pygame.locals import *
import param as p
from characters import *
pygame.init()

screen = pygame.display.set_mode(p.size)
bird = Bird()

run = True
while run:
    screen.fill(p.background)
    # draw
    bird.move()
    bird.show(screen)
    # detect
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird.flap()
            print("FLAP!!!")

    pygame.display.update()
    pygame.time.delay(1)

pygame.quit()
