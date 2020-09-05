# I put collisions() and gameover() out of the class Alien:

def collisions():
    global direz, godown

    for alien in aliens:
        if alien.rect.colliderect(ship):
            direz = 0
            godown = 0
            gameover()

# some changes in the game over function

def gameover():
    text = write("GAME OVER")
    text_rect = text.get_rect() 
    text_rect.center = w // 2, h // 2
    # rect = pygame.Rect(w, h, rect)

    # I "deleted the groups g and aliens"
    g = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    # cleared the screen
    screen.fill((0, 0, 0))

    # wrote GAME OVER
    screen.blit(write("GAME OVER"), text_rect)

# In the while loop I added collitions:

    screen.fill((0, 0, 0))
    g.draw(screen)
    aliens.update()
    collisions()

# before aliens.update() called self.collide() that now is collisions()