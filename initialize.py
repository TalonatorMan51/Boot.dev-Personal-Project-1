import pygame
from settings import *

def initialize():
    pygame.init()
    pygame.mixer.init()
    game.screen = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
    game.sounds["witch_laugh"] = pygame.Sound("assets/witches-laugh.wav")
