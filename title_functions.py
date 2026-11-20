import pygame
from clickables import *
from settings import *
from button_effects import *

def create_title_buttons():
    play = Button("Play", (game.SCREEN_WIDTH // 2), (game.SCREEN_HEIGHT / 2.34), "#8a00f8", "#9d37f1", effect = play_button, height = game.opt_height, 
                  width = game.tit_width, font_size = game.opt_font_size)
    options = Button("Options", (game.SCREEN_WIDTH // 2), play.y + (game.SCREEN_HEIGHT / 7.2), "#8a00f8", "#9d37f1", effect = options_button, height = game.opt_height, 
                  width = game.tit_width, font_size = game.opt_font_size)
    quit = Button("Quit Game", (game.SCREEN_WIDTH // 2), options.y + (game.SCREEN_HEIGHT / 7.2), "#8a00f8", "#9d37f1", effect = quit_button, height = game.opt_height, 
                  width = game.tit_width, font_size = game.opt_font_size)


    buttons = [play, quit, options]
    return buttons

def draw_title(screen:pygame.Surface, buttons: list[Button]):
    FONT = pygame.font.Font("assets/COPRGTL.TTF", 100)
    text_surf = FONT.render(f"{TITLE}", True, "white")
    text_rect = text_surf.get_rect(center = (game.SCREEN_WIDTH // 2, game.SCREEN_HEIGHT / 7.2))
    screen.blit(text_surf, text_rect)

    for button in buttons:
        button.draw(screen)
