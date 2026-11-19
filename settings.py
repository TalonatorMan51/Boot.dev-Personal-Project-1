import pygame
from enum import Enum

#Background classes to keep track of things
class GameState (Enum):
    TITLE = "title"
    GAME = "game"
    OPTIONS = "options"

class Game:
    def __init__(self):
        #Background things for game running stuff.
        self.state = GameState.TITLE
        self.prev_state = None
        self.running = False
        self.sounds = {}
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pending_resolution = None

        #Title Screen
        self.tit_width = 400 #Width of Title Screen buttons

        #Options Screen
        self.opt_width = 800 #Width of options buttons
        self.opt_height = 100 #Height of options and title buttons (title is added here since I game options the ability to be changed first before realizing it was the same.)
        self.sub_opt_height = 75 #Submenu button height
        self.opt_font_size = int(50) #Font size for options and title buttons (^^^)
        self.opt_res = False #If resolution menu is active


    def set_resolution(self, width: int, height: int):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.tit_width = self.SCREEN_WIDTH / 4.8
        self.opt_width = self.SCREEN_WIDTH / 2.4 
        self.opt_height = self.SCREEN_HEIGHT / 10.8
        self.opt_font_size = int(self.SCREEN_WIDTH // 38.4) 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))



game = Game()


# BACKGROUND CONSTANTS
TITLE = "Beytar Magic Academy"
BASE_UNLOCK = 100 #100 unless testing
LINE_HOVER_COLOR = "white"


#Unused for now
LINE_COLOR = "black"
