from enum import Enum

#Background classes to keep track of things
class GameState (Enum):
    TITLE = "title"
    GAME = "game"
    OPTIONS = "options"

class Game:
    def __init__(self):
        self.state = GameState.TITLE

game = Game()

# BACKGROUND CONSTANTS
BASE_UNLOCK = 100 #100 unless testing
LINE_HOVER_COLOR = "white"
TITLE = "Beytar Magic Academy"

#Unused for now
LINE_COLOR = "black"


# USER SETTINGS
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
