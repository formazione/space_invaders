# devlog 5

# I changed the window size

pygame.init()
size = w, h = 500, 700
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Space invaders")
clock = pygame.time.Clock()

# Also the ship position

ship = Ship("ship", w // 2, 660)


# In the class Alien I put 20 as num. of pixels...

    def godown(self):
        "How much the aliens go down"
        self.rect.top += 20