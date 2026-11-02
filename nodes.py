import pygame
from clickables import *

def create_nodes() -> list[Node]:
    fire = Node("Fire", 250, 500, "#ff9900", "#da9124")
    air = Node("Air", 375, 500, "#f3f3f3", "#cacaca")
    earth = Node("Earth", 500, 500, "#7f6000", "#644e0b")
    water = Node("Water", 625, 500, "#0000ff", "#3030e4")
    nodes = [fire, water, earth, air]
    return nodes


def draw_nodes(nodes:list[Node], screen: pygame.Surface):
    for node in nodes:
        node.draw(screen)