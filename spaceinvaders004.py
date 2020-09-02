# Space invaders

import pygame

pygame.init()
size = w, h = 500, 400
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Space invaders")
clock = pygame.time.Clock()


# =================================== CLASS SHIP
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


direz = 1

# ================================== CLASS ALIEN
class Alien(pygame.sprite.Sprite):
    def __init__(self, file, x, y):

        super(Alien, self).__init__()
        self.x = x
        self.y = y
        self.image = load("imgs\\" + file)
        self.w, self.h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        #self.rect.center = self.x, self.y
      
        g.add(self)
        aliens.add(self)

    def update(self):
        global direz
        self.rect.left += direz # + int(1 / len(aliens))
        self.collide()

    def godown(self):
        self.rect.top += 20

    def collide(self):
        global direz

        if self.rect.colliderect(ship):
            direz = 0
            self.gameover()

    def gameover(self):
        text = write("GAME OVER")
        text_rect = text.get_rect() 
        text_rect.center = w // 2, h // 2
        # rect = pygame.Rect(w, h, rect)
        screen.blit(write("GAME OVER"), text_rect)

font = pygame.font.SysFont("Arial", 36)


def write(text_to_show, color="Coral"):
    'write("Start")'
    text = font.render(text_to_show, 1, pygame.Color(color))
    return text


g = pygame.sprite.Group()
aliens = pygame.sprite.Group()
moveleft = 0
moveright = 0
# SPRITES ==========================
ship = Ship("ship", w // 2, 360)

squad = [
    [1,1,1,1,1,1,1,1], # line 1... [item, item]
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
    ]
    
#################################### ALIENS =====================
for y, line in enumerate(squad):
    for x, item in enumerate(line):
        if item == 1:
            # HERE you can change the enemy image!
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
            if event.key == pygame.K_ESCAPE:
                loop = 0
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
    aliens.update()
    for alien in aliens:
        if alien.rect.right > 500:
            direz = -1
            [alien.godown() for alien in aliens]
        if alien.rect.left < 0:
            direz = 1
            [alien.godown() for alien in aliens]
            
         
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()


