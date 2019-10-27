import pygame
import param as p
from characters import *
from utils import *


def start(screen, clock, bird):
    # draw
    screen.fill(p.background)
    bird.show(screen)
    text = 'Flappy Circular Bird Floating in Vacuum'
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
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            print('PAUSE!!!')
            return 'pause'

    # move
    if ObsGenerator.needNewObs(obs_list):
        ObsGenerator.getNewObs(obs_list)
    bird.move()
    for obs in obs_list:
        obs.move()

    # wait
    clock.tick_busy_loop(80)
    return 'game'


def pause(screen, clock):
    # draw
    # TODO: Draw a circle with play symbol
    pos = (int(0.5 * p.size[0]), int(0.5 * p.size[1]))
    pygame.draw.circle(screen, p.background, pos, p.pause_rad, 0)
    pygame.draw.circle(screen, (0, 0, 0), pos, p.pause_rad, 5)
    pointlist = ((int(pos[0] - p.pause_lwidth), int(pos[1] - 0.5 * p.pause_hight)),
                 (int(pos[0] - p.pause_lwidth), int(pos[1] + 0.5 * p.pause_hight)),
                 (int(pos[0] + p.pause_rwidth), int(pos[1])))
    pygame.draw.polygon(screen, (0, 0, 0), pointlist, 0)
    pygame.display.update()

    # detect operation
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            return 'quit'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            print('CONTINUE!!!')
            return 'game'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            print('CONTINUE!!!')
            return 'game'

    # wait
    clock.tick_busy_loop(80)
    return 'pause'


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
            init(bird, obs_list, scoreboard)
            print('START!!!')
            return 'game'
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            init(bird, obs_list, scoreboard)
            print('MENU!!!')
            return 'start'

    # wait
    clock.tick_busy_loop(80)
    return 'fail'
