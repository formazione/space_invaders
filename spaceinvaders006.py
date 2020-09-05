# Space invaders

import pygame

pygame.init()
size = w, h = 500, 700
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



# makes all aliens go in the same direction
direz = 1
# to make the aliens go down fluently
godown = 0
# ================================== CLASS ALIEN
class Alien(pygame.sprite.Sprite):
    def __init__(self, file, x, y):

        super(Alien, self).__init__()
        self.x = x
        self.y = y
        # Animation frames
        self.frames = [load(f) for f in (
            "imgs\\alien1b",
            "imgs\\alien1bb",
            "imgs\\alien1c",
            "imgs\\alien1bb")
            ]
        # starting frame
        self.image = self.frames[0]
        self.w, self.h = self.image.get_size()
        # rectangle around alien to detect collitions and move it
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        #self.rect.center = self.x, self.y
        # counter to update frames
        self.frame_cnt = 0
        # this adds the sprite to g and aliens groups to be updated in the while loop
        g.add(self)
        aliens.add(self)

    def update(self):
        global direz
        # The frame is changed every 3 frames at 0.33
        self.frame_cnt += .03
        if self.frame_cnt > len(self.frames):
            self.frame_cnt = 0
        # They all go right or left together
        self.rect.left += direz # + int(1 / len(aliens))
        # updates the image of the sprite every  3 frames (0.3 * 3)
        self.image = self.frames[int(self.frame_cnt)]


def collisions():
    global direz, godown

    for alien in aliens:
        if alien.rect.colliderect(ship):
            direz = 0
            godown = 0
            gameover()


def gameover():
    text = write("GAME OVER")
    text_rect = text.get_rect() 
    text_rect.center = w // 2, h // 2
    # rect = pygame.Rect(w, h, rect)
    g = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    screen.fill((0, 0, 0))
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
ship = Ship("ship", w // 2, 660)

squad = [
        [1,1,1,1,1,1,1,1],
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
cnt = 0
loop = 1
mem_direz = 0
going = 1
while loop:

    if godown:
        # mem_direz = direz
        # direz = 0
        cnt += 1
        for alien in aliens:
            alien.rect.top += 3

        direz = 0
        if cnt == 30:
            godown = 0
            cnt = 0
            direz = going


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
    collisions()

    for alien in aliens:
        if alien.rect.right > 500:
            going = -1
            godown = 1
        if alien.rect.left < 0:
            going = 1
            godown = 1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
