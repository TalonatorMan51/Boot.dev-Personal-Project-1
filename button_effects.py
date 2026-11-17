import pygame
from settings import *



#TITLE
def play_button():
    game.prev_state = game.state
    game.state = GameState.GAME

def quit_button():
    game.running = False

def options_button():
    game.prev_state = game.state
    if game.state == GameState.TITLE:
        game.sounds["witch_laugh"].play()
    game.state = GameState.OPTIONS



#OPTIONS
def back_button():
    game.state = game.prev_state
    game.prev_state = None

def res_button():
    game.opt_res = True

#ANY OTHER USELESS BUTTON
def empty_button():
    pass

#RESOLUTION FUNCTIONS
def res_hd():
    game.pending_resolution = (1280, 720)
    game.opt_res = False

def res_full_hd():
    game.pending_resolution = (1920, 1080)
    game.opt_res = False

#Helper functions
