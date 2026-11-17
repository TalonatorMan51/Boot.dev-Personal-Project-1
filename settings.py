import pygame
from enum import Enum

#Background classes to keep track of things
class GameState (Enum):
    TITLE = "title"
    GAME = "game"
    OPTIONS = "options"

class Game:
    def __init__(self):
        #background things to for game running stuff.
        self.state = GameState.TITLE
        self.prev_state = None
        self.running = False
        self.sounds = {}
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pending_resolution = None
        #Options Screen
        self.opt_res = False

    def set_resolution(self, width: int, height: int):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))



game = Game()


# BACKGROUND CONSTANTS
TITLE = "Beytar Magic Academy"
BASE_UNLOCK = 100 #100 unless testing
LINE_HOVER_COLOR = "white"


#Unused for now
LINE_COLOR = "black"
