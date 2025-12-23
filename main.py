import pygame
import sys
from game import Game

def main():
    pygame.init()
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Galaxians Python")
    
    clock = pygame.time.Clock()
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game.game_over:
                    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT) # Restart
        
        # Update
        game.update()
        
        # Draw
        game.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
