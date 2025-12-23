import pygame
from bullet import Bullet
from utils import make_transparent

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        try:
            # Load image
            raw_image = pygame.image.load("assets/player.png")
            # Make transparent with tolerance
            self.image = make_transparent(raw_image)
            # Scale
            self.image = pygame.transform.scale(self.image, (40, 40))
        except FileNotFoundError:
            # Fallback if image not found
            self.image = pygame.Surface((40, 40))
            self.image.fill((0, 255, 0))
            pygame.draw.polygon(self.image, (0, 200, 0), [(20, 0), (0, 40), (40, 40)])
        
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.screen_width = screen_width
        self.speed = 5
        self.bullets = pygame.sprite.Group()
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 250

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top, -1)
            self.bullets.add(bullet)
