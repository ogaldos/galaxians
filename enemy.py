import pygame
import random
from bullet import Bullet
from utils import make_transparent

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        try:
            # Load image
            raw_image = pygame.image.load("assets/enemy.png")
            # Make transparent
            self.image = make_transparent(raw_image)
            # Scale
            self.image = pygame.transform.scale(self.image, (30, 30))
            
            # Tinting logic
            # Create a mask to ensure we only tint the sprite, not the transparent background
            # Note: make_transparent already set alpha to 0 for background
            
            # Create a solid color surface
            color_surface = pygame.Surface(self.image.get_size()).convert_alpha()
            color_surface.fill(color)
            
            # Blit the color surface onto the image using MULT blend mode
            self.image.blit(color_surface, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            
        except FileNotFoundError:
            self.image = pygame.Surface((30, 30))
            self.image.fill(color)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.origin_x = x
        self.origin_y = y
        
        self.is_diving = False
        self.dive_speed_x = 0
        self.dive_speed_y = 0

    def update(self):
        if self.is_diving:
            self.rect.x += self.dive_speed_x
            self.rect.y += self.dive_speed_y
            
            # Return to formation if off screen (simplified logic for now)
            if self.rect.top > 800: 
                self.reset_formation()
        else:
            # Formation movement handled by Game class, but we can add small idle animation here
            pass

    def move_formation(self, dx):
        if not self.is_diving:
            self.origin_x += dx
            self.rect.x = self.origin_x

    def dive(self, target_x, target_y):
        self.is_diving = True
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            self.dive_speed_x = (dx / dist) * 4
            self.dive_speed_y = (dy / dist) * 4 + 2 # Add some downward bias
            
    def shoot(self):
        # Simple shooting logic
        return Bullet(self.rect.centerx, self.rect.bottom, 1)

    def reset_formation(self):
        self.is_diving = False
        self.rect.x = self.origin_x
        self.rect.y = self.origin_y
