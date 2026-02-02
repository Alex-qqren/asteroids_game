import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()    
    # Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Classes
    Player.containers = (updatable, drawable)
    # Class instances
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    # Game loop
    while True:
        log_state()

        # Quit button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # color the screen black
        screen.fill("black")
        
            # moving (left, right, forward, backward)
        for instance in updatable:
            instance.update(dt)

            # add the player to the screen
        for instance in drawable:
            instance.draw(screen) 


        # update the screen
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
