import pygame
from clickables import *
from settings import *
from button_effects import *

def create_title_buttons():
    play = Button("Play", 960, 460, "#8a00f8", "#9d37f1", effect = play_button)

    buttons = [play]
    return buttons

def draw_title(screen:pygame.Surface, buttons: list[Button]):
    FONT = pygame.font.Font("assets/COPRGTL.TTF", 100)
    text_surf = FONT.render(f"{TITLE}", True, "white")
    text_rect = text_surf.get_rect(center = (SCREEN_WIDTH // 2, 150))
    screen.blit(text_surf, text_rect)

    for button in buttons:
        button.draw(screen)
