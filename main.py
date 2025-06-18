import pygame
from constants import *




def main():
    pygame.init() # Starts the Pygame Module
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # this pops up a window and stores the window's Object aka *Surafce*

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))  # fill method for surface that fills the surface color to *black*
        pygame.display.flip() # display.flip() which refreshes the screen



if __name__ == "__main__":
    main()