
'''
            PART 3 - move 1
we use direz to move all the sprites
in the same direction

'''
# All in the same direction

direz = 1
class Alien(pygame.sprite.Sprite):
    def __init__(self, file, x, y):

# [...]
# in the update method we update the dir every frame
    def update(self):
        global direz
        self.rect.left += direz


# In the while loop we update the pos
# Here we call the update for the aliens
    aliens.update()
    g.draw(screen)

# we check every alien, if one goes to 500 or 0 changedir
    for alien in aliens:
        if alien.rect.right > 500:
            direz = -1
        if alien.rect.left < 0:
            direz = 1

