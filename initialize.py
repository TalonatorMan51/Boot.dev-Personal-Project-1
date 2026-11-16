import pygame
from settings import *

def initialize():
    pygame.init()
    pygame.mixer.init()
    game.sounds["witch_laugh"] = pygame.Sound("assets/witches-laugh.wav")
