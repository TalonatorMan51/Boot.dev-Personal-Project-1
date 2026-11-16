import pygame
from settings import *




def play_button():
    game.state = GameState.GAME

def quit_button():
    game.running = False

def options_button():
    game.sounds["witch_laugh"].play()

def empty_button():
    pass
