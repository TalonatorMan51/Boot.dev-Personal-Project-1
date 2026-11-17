import pygame, sys
from settings import *
from clickables import *
from nodes import *
from title_functions import *
from button_effects import *
from initialize import *
from options_menu import *

def main():
    initialize()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = game.screen
    pygame.display.set_caption(f"{TITLE}")
    game.running = True

    title_menu = create_title_buttons()
    options_menu = create_options()
    resolution_select = create_res()
    nodes = create_nodes()


    pure_node = nodes[0]
    PURE_FLASH = False
    flash_dur = 500
    flash_start = 0


    while game.running:
        if game.pending_resolution:
            w, h = game.pending_resolution
            game.set_resolution(w, h)
            game.pending_resolution = None

        # Rebuild menus safely!
            title_menu = create_title_buttons()
            options_menu = create_options()
            resolution_select = create_res()

        while game.state == GameState.TITLE and game.running:
            screen = pygame.display.get_surface()
            mouse_pos = pygame.mouse.get_pos()

            for button in title_menu:
                button.check_hover(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                for button in title_menu:
                    if button.is_clicked(event):
                        button.click()

            screen.fill("#22211F")

            draw_title(screen, title_menu)
        
            dt = clock.tick(60) / 1000
            pygame.display.flip()


        while game.state == GameState.OPTIONS and game.running:
            screen = pygame.display.get_surface()
            mouse_pos = pygame.mouse.get_pos()

            for button in options_menu:
                button.check_hover(mouse_pos)

            if game.opt_res == True:
                for button in resolution_select:
                    button.check_hover(mouse_pos)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                for button in options_menu:
                    if button.is_clicked(event):
                        button.click()
                if game.opt_res:
                    for button in resolution_select:
                        if button.is_clicked(event):
                            button.click()

            screen.fill("#22211F")

            draw_options(screen, options_menu)
            if game.opt_res == True:
                draw_options(screen, resolution_select)

            dt = clock.tick(60) / 1000
            pygame.display.flip()


        while game.state == GameState.GAME and game.running:
            screen = pygame.display.get_surface()
            mouse_pos = pygame.mouse.get_pos()
        
            for node in nodes:
                node.check_hover(mouse_pos)

            active_nodes: list[Node] = []
            pure_nodes: list[Node] = []
            big_tier = 0
            for node in nodes:
                #check if unlocked
                if node.is_unlocked == True:
                    #skip higher tiers that are unlocked but have not been used
                    if node.tier > 1:
                        if node.value <= 1:
                            continue
                    #check highest tier
                    if node.tier > big_tier:
                        big_tier = node.tier
                    #add to active list
                    active_nodes.append(node)
            #if node tier is at least lower 2 than highest active tier, do not include for pure to pull from.
            for active in active_nodes:
                if active.tier >= (big_tier - 1):
                    pure_nodes.append(active)

            #Pure node flashes red if insufficient mana of all needed types
            if PURE_FLASH:
                current_time = pygame.time.get_ticks()
                if current_time - flash_start >= flash_dur:
                    pure_node.hover_color = "#9d37f1"
                    pure_node.color = "#8a00f8"
                    PURE_FLASH = False

            #The actual actions players can take.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                for node in nodes:
                    if node.is_clicked(event):
                        if node.type == ClickType.NODE:
                            reg_increment(node, pure_node)
                        if node.type == ClickType.PURE:
                            flash = pure_increment(node, pure_nodes)
                            if flash == 1:
                                pure_node.hover_color = "#bb293f"
                                pure_node.color = "#df0829"
                                PURE_FLASH = True
                                flash_start = pygame.time.get_ticks()

            for node in nodes:
                node.update()

         
            screen.fill("#22211F")

            draw_nodes(nodes, screen)

            dt = clock.tick(60) / 1000
            pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()
