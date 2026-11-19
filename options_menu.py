from settings import *
from clickables import *
from button_effects import *



def create_options():
    resolution = Button(f"Resolution: {game.SCREEN_WIDTH}x{game.SCREEN_HEIGHT}", (game.SCREEN_WIDTH / 2), (game.SCREEN_HEIGHT // 3.48),
                         "#674ae9", "#5d4da3", 
                        effect = res_button, height = game.opt_height, width = game.opt_width, font_size = game.opt_font_size)
    back = Button("Back", (game.SCREEN_WIDTH / 2), resolution.y + (game.SCREEN_HEIGHT / 7.2), "#674ae9", "#5d4da3", effect = back_button, 
                  height = game.opt_height, width = game.opt_width, font_size = game.opt_font_size)

    buttons = [back, resolution]
    return buttons

def draw_options(screen: pygame.Surface, buttons: list[Button]):
    FONT = pygame.font.Font("assets/COPRGTL.TTF", 80)
    text_surf = FONT.render("The Options Menu.", True, "white")
    text_rect = text_surf.get_rect(center = (game.SCREEN_WIDTH / 2, game.SCREEN_HEIGHT / 7.2))
    screen.blit(text_surf, text_rect)
    for button in buttons:
        button.draw(screen)

def create_res():
    hd = Button("1280x720", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), (game.SCREEN_HEIGHT // 3.48), "#1442d8", "#3f58ac", effect = res_hd,
                 height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _4x3 = Button("1280x960", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), hd.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                      effect = res_4x3, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    full_hd = Button("1920x1080", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), _4x3.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_full_hd, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    tall16x10 = Button("1920x1200", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), full_hd.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_16x10, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _2k_ultrawide = Button("2560x1080", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), tall16x10.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_2k_uw, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _2k = Button("2560x1440", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), _2k_ultrawide.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_2k, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _2k_16x10 = Button("2560x1600", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), _2k.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_2k_16x10, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _4k_uw = Button("3840x1440", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), _2k_16x10.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_4k_uw, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)
    _4k = Button("3840x2160", (game.SCREEN_WIDTH / 2) + (game.SCREEN_WIDTH / 3), _4k_uw.y + (game.SCREEN_HEIGHT / 14.4), "#1442d8", "#3f58ac", 
                     effect = res_4k, height = game.sub_opt_height, width = game.tit_width, font_size = game.opt_font_size)

    buttons = [_4x3, hd, full_hd, tall16x10, _2k_ultrawide, _2k, _2k_16x10, _4k_uw, _4k]
    return buttons