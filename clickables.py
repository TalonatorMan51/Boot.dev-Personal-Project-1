import pygame, math
from enum import Enum
from settings import *
from collections.abc import Callable
from button_effects import empty_button


class ClickType(Enum):
    NODE = "node"
    MENU = "menu"
    PURE = "pure"


class Clickable(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, type: ClickType):
        super().__init__()
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.type = type

        #Use these for a reset camera button or something
        self.origin_x = x
        self.origin_y = y

    def draw(self, screen: pygame.Surface):
        pass

    def is_clicked(self):
        pass

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x += 2.5
            self.position = pygame.Vector2(self.x, self.y)
        if keys[pygame.K_d]:
            self.x -= 2.5
            self.position = pygame.Vector2(self.x, self.y)
        if keys[pygame.K_w]:
            self.y += 2.5
            self.position = pygame.Vector2(self.x, self.y)
        if keys[pygame.K_s]:
            self.y -= 2.5
            self.position = pygame.Vector2(self.x, self.y)

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

        FONT = pygame.font.Font("assets/COPRGTB.TTF", 18)
        text_surf = FONT.render(f"{self.name}:{self.value}", True, "black")
        text_rect = text_surf.get_rect(center=self.position)
        screen.blit(text_surf, text_rect)

    def draw_lines(self, screen: pygame.Surface):
        #variable for having always visible lines, if final version does not have it, it will be removed.
        line_current = LINE_HOVER_COLOR if self.is_hovered else LINE_COLOR
        if self.is_hovered:
            for parent in self.parents:
                pygame.draw.line(screen, LINE_HOVER_COLOR, (self.x, (self.y + self.radius - 3)), (parent.x, (parent.y - parent.radius + 3)), width = 3)


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
        if self.value >= (BASE_UNLOCK / 2):
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

        FONT = pygame.font.Font("assets/COPRGTB.TTF", 20)
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

class Button(Clickable):
    def __init__(self, name: str, x: float, y: float, color, hover_color, effect: Callable = empty_button, height: float = 100, width: float = 400, 
                 type = ClickType.MENU, font_size = 50, font_file = "assets/COPRGTB.TTF"):
        super().__init__(x, y, type)
        self.name = name
        self.height = height
        self.width = width
        
        self.rect = pygame.Rect(self.x - (self.width/2), self.y - (self.height/2), self.width, self.height)
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font_file = font_file

        self.effect = effect


    def draw(self, screen: pygame.Surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        FONT = pygame.font.Font(self.font_file, self.font_size)
        text_surf = FONT.render(f"{self.name}", True, "black")
        text_rect = text_surf.get_rect(center=self.position)
        screen.blit(text_surf, text_rect)


    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False
        return self.is_hovered


    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False

    def click(self):
        if self.effect:
            self.effect()