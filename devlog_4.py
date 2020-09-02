''' part 4 - move 2 '''
# Move down if > 500 or <0

# In the Alien class:
    def update(self):
        global direz
        self.rect.left += direz + int(1 / len(aliens))
        self.collide()

    def godown(self):
        self.rect.top += 5

    def collide(self):
        global direz

        if self.rect.colliderect(ship):
            direz = 0

# In the while loop:

# When an alien hit the border, all change direction
    g.draw(screen)
    for alien in aliens:
        if alien.rect.right > 500:
            direz = -1
            [alien.godown() for alien in aliens]
        if alien.rect.left < 0:
            direz = 1
            [alien.godown() for alien in aliens]


# WRITE GAME OVER

font = pygame.font.SysFont("Arial", 16)


def write(text_to_show, color="Coral"):
    'write("Start")'
    text = font.render(text_to_show, 1, pygame.Color(color))
    return text

# In the collide method of Alien... we call gameover method to write...

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
