import pygame
from enum import Enum


class ClickType(Enum):
    NODE = "node"
    MENU = "menu"


class Clickable:
    def __init__(self, x: float, y: float, type: ClickType):
        self.position = pygame.Vector2 = pygame.Vector2(x, y)
        self.type = type

    def draw(self, screen:pygame.Surface):
        pass

    def on_click(self):
        pass


class Node(Clickable):
    def __init__(self, name: str, x: float, y: float, tier: int = 0):
        super.__init__(x, y, ClickType.NODE)
        self.name = name
        self.tier = tier
        self.children: list[Node] = [] 
        self.parents: list[Node] = []

