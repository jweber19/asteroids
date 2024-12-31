# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        pygame.display.flip()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player = Player(x, y)
    player.draw(screen)

if __name__ == "__main__":
    main()
