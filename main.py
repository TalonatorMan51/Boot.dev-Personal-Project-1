import pygame, sys
from settings import *
from clickables import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    fire = Node("Fire", 250, 250, "orange", "gray")

    while running:
        mouse_pos = pygame.mouse.get_pos()
        fire.check_hover(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if fire.is_clicked(event):
                fire.value += 1

        screen.fill("black")

        fire.draw(screen)

        dt = clock.tick(60) / 1000
        pygame.display.flip()


    pass
pygame.quit()

if __name__ == "__main__":
    main()
