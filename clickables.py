import pygame, math
from enum import Enum
from settings import *


class ClickType(Enum):
    NODE = "node"
    MENU = "menu"


class Clickable(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, type: ClickType):
        super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.type = type

    def draw(self, screen: pygame.Surface):
        pass

    def is_clicked(self):
        pass


class Node(Clickable):
    def __init__(self, name: str, x: float, y: float, color, hover_color, value = 1, tier: int = 0, radius = 50):
        super().__init__(x, y, ClickType.NODE)
        self.name = name
        self.value = value
        self.tier = tier
        self.children: list[Node] = [] 
        self.parents: list[Node] = []

        self.radius = radius
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen: pygame.Surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.circle(screen, current_color, self.position, self.radius)

        FONT = pygame.font.SysFont("Arial", 24)
        text_surf = FONT.render(f"{self.name}:{self.value}", True, "black")
        text_rect = text_surf.get_rect(center=self.position)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        mx, my = mouse_pos

        distance = math.hypot(mx - self.x, my - self.y)
        self.is_hovered = distance <= self.radius
        return self.is_hovered

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False
