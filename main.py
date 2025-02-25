# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
black = (255, 255, 255)
white = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Fill screen with black and refresh the display
        screen.fill(white)
        pygame.display.flip()
        
        #limit display refresh to 60 FPS
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()