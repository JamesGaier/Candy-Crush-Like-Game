#!/usr/bin/env python3
"""
A prototype that gives me an idea of how to build a Candy Crush/Bejeweled like game
"""
import sys
import signal
import pygame
from candy_proto.engine.sheet import SpriteSheet

pygame.display.init()

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

WIDTH = 400
HEIGHT = 560
window = (WIDTH, HEIGHT)
TITLE = 'Candy Crush'
screen = pygame.display.set_mode(window)

sprite_sheet = SpriteSheet("res/candy_crush.png", window)
background = pygame.Surface(window)

def draw():
    """
    Draws sprites to the screen
    """
    screen.fill((255, 255, 255))
    x_off = 0
    for sprite in sprite_sheet.get_sprites():
        screen.blit(sprite_sheet.get_sprite(sprite), (x_off,0))
        x_off += sprite.width
    pygame.display.flip()

def loop():
    """
    Runs the draw and update calls to handles game elements
    """
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()

pygame.display.flip()
if __name__ == "__main__":
    loop()
