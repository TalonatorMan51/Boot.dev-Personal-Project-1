import pygame, sys
from settings import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        dt = clock.tick(60) / 1000
        pygame.display.flip()


    pass
pygame.quit()

if __name__ == "__main__":
    main()
