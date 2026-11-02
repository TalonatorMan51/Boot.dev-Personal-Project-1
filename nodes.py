import pygame
from clickables import *

def create_nodes() -> list[Node]:
    fire = Node("Fire", 250, 500, "orange", "gray")
    water = Node("Water", 375, 500, "blue", "gray")
    earth = Node("Earth", 500, 500, "brown", "gray")
    air = Node("Air", 625, 500, "white", "gray")
    nodes = [fire, water, earth, air]
    return nodes


def draw_nodes(nodes:list[Node], screen: pygame.Surface):
    for node in nodes:
        node.draw(screen)