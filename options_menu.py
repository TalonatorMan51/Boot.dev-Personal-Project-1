from settings import *
from clickables import *
from button_effects import *

def create_options():
    resolution = Button(f"Resolution: {game.SCREEN_WIDTH}x{game.SCREEN_HEIGHT}", (game.SCREEN_WIDTH / 2), 310, "#674ae9", "#5d4da3", 
                        effect = res_button, width = (game.SCREEN_WIDTH / 2.4))
    back = Button("Back", (game.SCREEN_WIDTH / 2), 460, "#674ae9", "#5d4da3", effect = back_button, width = 800)

    buttons = [back, resolution]
    return buttons

def draw_options(screen: pygame.Surface, buttons: list[Button]):
    FONT = pygame.font.Font("assets/COPRGTL.TTF", 80)
    text_surf = FONT.render("The Options Menu.", True, "white")
    text_rect = text_surf.get_rect(center = (game.SCREEN_WIDTH / 2, 150))
    screen.blit(text_surf, text_rect)
    for button in buttons:
        button.draw(screen)

def create_res():
    hd = Button("1280x720", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), 310, "#1442d8", "#3f58ac", effect = res_hd)
    full_hd = Button("1920x1080", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), 410, "#1442d8", "#3f58ac", effect = res_full_hd)

    buttons = [hd, full_hd]
    return buttons