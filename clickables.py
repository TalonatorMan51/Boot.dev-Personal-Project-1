import pygame, math
from enum import Enum
from settings import *


class ClickType(Enum):
    NODE = "node"
    MENU = "menu"
    PURE = "pure"


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
    def __init__(self, name: str, x: float, y: float, color, hover_color, value = 1, tier: int = 1, radius = 50, 
                 type = ClickType.NODE, parents: list = []):
        super().__init__(x, y, type)
        self.name = name
        self.value: int = value
        self.tier = tier
        self.children: list[Node] = []
        self.parents: list[Node] = parents

        self.radius = radius
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen: pygame.Surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.circle(screen, current_color, self.position, self.radius)

        FONT = pygame.font.SysFont("Copperplate Gothic", 30)
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

    @property
    def is_unlocked(self):
        if self.tier <= 1:
            return True
        if self.value >= 50:
            return True
        for parent in self.parents:
            if parent.value < (BASE_UNLOCK * parent.tier):
                return False
        return True

class PureNode(Node):
    def __init__(self, name: str, x: float, y: float, color, hover_color, value = 1, tier: int = 0, radius = 40, type = ClickType.PURE):
        super().__init__(name, x, y, color, hover_color, value, tier, radius, type)

    def draw(self, screen: pygame.Surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.circle(screen, current_color, self.position, self.radius)

        FONT = pygame.font.SysFont("Copperplate Gothic", 30)
        first, second = self.name.split()
        text_surf1 = FONT.render(f"{first}", True, "black")
        text_surf2 = FONT.render(f"{second}:", True, "black")
        text_surf3 = FONT.render(f"{self.value}", True, "black")
        text_rect = text_surf1.get_rect(center=(self.x, self.y - 20))
        text_rect2 = text_surf2.get_rect(center = (self.x, self.y))
        text_rect3 = text_surf3.get_rect(center = (self.x, self.y + 25))
        screen.blit(text_surf1, text_rect)
        screen.blit(text_surf2, text_rect2)
        screen.blit(text_surf3, text_rect3)

