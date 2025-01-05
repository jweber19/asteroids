import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    # Game loop
    while True:
        dt = clock.tick(60) / 1000.0  # add dt calculation
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update and draw INSIDE the game loop
        player.update(dt)  # pass dt to update
        
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()