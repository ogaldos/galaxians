import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        
        self.player = Player(screen_width, screen_height)
        self.all_sprites.add(self.player)
        
        self.create_enemies()
        
        self.score = 0
        self.game_over = False

    def create_enemies(self):
        rows = 4
        cols = 8
        start_x = 50
        start_y = 50
        x_spacing = 50
        y_spacing = 50
        
        enemy_assets = [
            "assets/enemy_01.png",
            "assets/enemy_02.png",
            "assets/enemy_03.png",
            "assets/enemy_04.png",
        ]
        fallback_colors = [(255, 0, 0), (255, 165, 0), (0, 0, 255), (255, 0, 255)]
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * x_spacing
                y = start_y + row * y_spacing
                asset_index = row % len(enemy_assets)
                enemy = Enemy(
                    x,
                    y,
                    enemy_assets[asset_index],
                    fallback_color=fallback_colors[asset_index],
                )
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)

    def update(self):
        if self.game_over:
            return

        # Move formation
        self.formation_direction = getattr(self, 'formation_direction', 1)
        move_amount = 1 * self.formation_direction
        
        # Check bounds for formation
        left_most = min([e.rect.left for e in self.enemies if not e.is_diving], default=0)
        right_most = max([e.rect.right for e in self.enemies if not e.is_diving], default=self.screen_width)
        
        if left_most <= 0 or right_most >= self.screen_width:
            self.formation_direction *= -1
            move_amount = 1 * self.formation_direction
            
        for enemy in self.enemies:
            enemy.move_formation(move_amount)

        # Randomly make enemies dive
        import random
        if random.random() < 0.02: # 2% chance per frame
            if self.enemies:
                attacking_enemy = random.choice(self.enemies.sprites())
                if not attacking_enemy.is_diving:
                    attacking_enemy.dive(self.player.rect.centerx, self.player.rect.centery)
        
        # Randomly make diving enemies shoot
        for enemy in self.enemies:
            if enemy.is_diving and random.random() < 0.05:
                bullet = enemy.shoot()
                self.enemy_bullets.add(bullet)

        self.all_sprites.update()
        self.player.bullets.update()
        self.enemy_bullets.update()
        
        # Check collisions
        # Player bullets hitting enemies
        hits = pygame.sprite.groupcollide(self.enemies, self.player.bullets, True, True)
        for hit in hits:
            self.score += 10
            
        # Enemies hitting player
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.game_over = True
            
        # Enemy bullets hitting player
        hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        if hits:
            self.game_over = True

    def draw(self, screen):
        screen.fill((0, 0, 0)) # Black background
        self.all_sprites.draw(screen)
        self.player.bullets.draw(screen)
        self.enemy_bullets.draw(screen)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.screen_width/2, self.screen_height/2))
            screen.blit(game_over_text, text_rect)
