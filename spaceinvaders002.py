# Space invaders

import pygame

pygame.init()
size = w, h = 500, 400
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Space invaders")
clock = pygame.time.Clock()

class Ship(pygame.sprite.Sprite):
    def __init__(self, file, x, y):

        super(Ship, self).__init__()
        self.x = x
        self.y = y
        self.image = load("imgs\\" + file)
        self.w, self.h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        g.add(self)
        self.rect.center = self.x, self.y


def load(file):
    return pygame.image.load(file + ".png")


class Alien(pygame.sprite.Sprite):
    def __init__(self, file, x, y):

        super(Alien, self).__init__()
        self.x = x
        self.y = y
        self.image = load("imgs\\" + file)
        self.w, self.h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.rect.center = self.x, self.y
        g.add(self)




g = pygame.sprite.Group()
moveleft = 0
moveright = 0

ship = Ship("ship", w // 2, 360)

squad = [
    [1,1,1,1,1,1,1,1], # line 1... [item, item]
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
    ]
    

for y, line in enumerate(squad):
    for x, item in enumerate(line):
        if item == 1:
            alien = Alien("alien1", 70 + 50 * x, 30 + 50 * y)


loop = 1
while loop:

    if moveleft:
        if ship.rect.left > 0:
            ship.rect.left -= 1
    if moveright:
        if ship.rect.right < 500:
            ship.rect.left += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveleft = 1
                moveright = 0
            if event.key == pygame.K_RIGHT:
                moveleft = 0
                moveright = 1
        if event.type == pygame.KEYUP:
            moveleft = 0
            moveright = 0
    screen.fill((0, 0, 0))
    g.draw(screen)
    g.update()
    pygame.display.update()
    clock.tick(180)

pygame.quit()


