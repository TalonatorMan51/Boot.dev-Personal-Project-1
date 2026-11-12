import pygame
from clickables import *
from settings import *

def create_buttons():
    pass

def draw_title(screen:pygame.Surface, buttons):
    FONT = pygame.font.Font("assets/COPRGTL.TTF", 100)
    text_surf = FONT.render(f"{TITLE}", True, "white")
    text_rect = text_surf.get_rect(center = (SCREEN_WIDTH // 2, 150))
    screen.blit(text_surf, text_rect)