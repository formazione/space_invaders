'''


                                    SPACE
                                    INVADERS
                                    15.7.2020
                                    12:00




'''
import pygame
import sys


class Game:
    aliens = []

    def __init__(self, w, h):
        pygame.init()
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()

        loop = 1

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = 0
            pygame.display.update()
            self.clock.tick(60)


Game(400, 400)
pygame.quit()
sys.exit()
