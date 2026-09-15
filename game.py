#!/usr/bin/env python3
"""
A prototype that gives me an idea of how to build a Candy Crush/Bejeweled like game
"""
import sys
import signal
import pygame
from candy_proto.engine.sheet_coords import candy_positions, cursor_positions
from candy_proto.engine.sheet import SpriteSheet
from candy_proto.game.board import Board
from candy_proto.game.actor import Actor
import random

running = True
def handler(_signum, _frame):
    """
    Handles CTRL+C presses to exit the game
    """
    global running
    print("CTRL+C received...")
    running = False
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Candy Crush Prototype", icontitle="")

WIDTH = 400
HEIGHT = 560
window = (WIDTH, HEIGHT)
COLS = 10
ROWS = 10
TITLE = 'Candy Crush'
screen = pygame.display.set_mode(window)
sprite_sheet = SpriteSheet("res/candy_crush.png", window, candy_positions)
board = Board(COLS, ROWS, sprite_sheet)
cursor_sprite = SpriteSheet("res/cursor.png", (150,75), cursor_positions)
cursor = Actor("res/cursor.png", cursor_positions, (0,0), (150, 75))
background = pygame.image.load("res/background0.jpg")
background = pygame.transform.scale(background, window)

def draw():
    """
    Draws sprites to the screen
    """
    screen.blit(background, (0,0))
    board.draw(screen)
    cursor.draw(screen)
    pygame.display.flip()

def loop():
    """
    Runs the draw and update calls to handles game elements
    """
    draw()
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.update(pygame.mouse.get_pos(), off=(-30, -10))
        draw()


if __name__ == "__main__":
    loop()
