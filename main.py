import pygame, sys
from settings import *
from clickables import *
from nodes import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    nodes = create_nodes()

    while running:
        mouse_pos = pygame.mouse.get_pos()
        for node in nodes:
            node.check_hover(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for node in nodes:
                if node.is_clicked(event):
                    node.value += 1

        screen.fill("#22211F")

        draw_nodes(nodes, screen)

        dt = clock.tick(60) / 1000
        pygame.display.flip()


    pass
pygame.quit()

if __name__ == "__main__":
    main()
