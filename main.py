import pygame
import sys
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import *

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # Class instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_fld = AsteroidField()

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
        updatable.update(dt)

        # player and asteroid collision
        for asteroid in asteroids:
            # if CircleShape.collides_with(asteroid, player):
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # shot and asteroid collision
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()

            # add the player to the screen
        for instance in drawable:
            instance.draw(screen) 


        # update the screen
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
