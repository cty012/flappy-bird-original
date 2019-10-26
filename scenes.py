import pygame
import param as p
from characters import *
from utils import *


def start(screen, clock, bird):
    # draw
    screen.fill(p.background)
    bird.show(screen)
    text = 'Flappy Round Bird Floating in Vacuum'
    showText(screen, text, p.title_pos, p.font, 50, (0, 0, 0))
    text = 'press "Space" to play'
    showText(screen, text, p.subtitle_pos, p.font, 30, (0, 0, 0))
    pygame.display.update()

    # detect operation
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            return 'quit'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            print('START!!!')
            return 'game'

    # wait
    clock.tick_busy_loop(80)
    return 'start'


def game(screen, clock, bird, obs_list, frame, scoreboard):
    # calculate score
    for obs in obs_list:
        if obs.score():
            scoreboard.gain_point()

    # draw
    screen.fill(p.background)
    bird.show(screen)
    for obs in obs_list:
        obs.show(screen)
    scoreboard.show(screen)
    pygame.display.update()

    # detect collision
    collision = False
    collision = collision or CollisionDetector.detect(bird, frame)
    for obs in obs_list:
        collision = collision or CollisionDetector.detect(bird, obs)
    if collision:
        print('COLLIDE!!!')
        scoreboard.save_score()
        return 'fail'

    # detect operation
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            return 'quit'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird.flap()
            print('FLAP!!!')

    # move
    if ObsGenerator.needNewObs(obs_list):
        ObsGenerator.getNewObs(obs_list)
    bird.move()
    for obs in obs_list:
        obs.move()

    # wait
    clock.tick_busy_loop(80)
    return 'game'


def fail(screen, clock, bird, obs_list, scoreboard):
    # draw
    text = 'You Have Failed With a Score of {}'.format(scoreboard.score)
    showText(screen, text, p.title_pos, p.font, 50, (255, 0, 0))
    text = 'press "Space" to play again'
    showText(screen, text, p.subtitle_pos, p.font, 30, (0, 0, 0))
    pygame.display.update()

    # detect operation
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            return 'quit'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird.vel = p.init_vel
            bird.y = p.pos[1]
            obs_list *= 0
            scoreboard.refresh()
            print('START!!!')
            return 'game'

    # wait
    clock.tick_busy_loop(80)
    return 'fail'
