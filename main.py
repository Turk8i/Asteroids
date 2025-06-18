import pygame
from constants import *
from player import *




def main():
    pygame.init() # Starts the Pygame Module
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # this pops up a window and stores the window's Object aka *Surafce*

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  # Storing clock object to use its methods like tick()
    deltaTime = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2)  # Initiating a Player object with the coordinates of the screen's center


    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        screen.fill("black")  # fill method for surface that fills the surface color to *black*
        player.draw(screen)  # Draws the sprite into the screen *surface*
        
        tick = clock.tick(60) # Limiting the game to 40 FPS max, if the fps is higher it pauses the game to slow it down to 40fps. It also returns the miliseconds from past tick.
        deltaTime = tick / 1000 # converting from milisecond to seconds

        player.update(deltaTime)



        pygame.display.flip() # display.flip() which refreshes the screen. LAST METHOD TO DO IN GAME LOOP



if __name__ == "__main__":
    main()