import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7 * direction # -1 for up (player), 1 for down (enemy)

    def update(self):
        self.rect.y += self.speed
        # Remove if off screen
        if self.rect.bottom < 0 or self.rect.top > 800: # Assuming 800 height for now
            self.kill()
