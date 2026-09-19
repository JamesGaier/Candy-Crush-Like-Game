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

class Game:
    def __init__(self):
        WIDTH = 400
        HEIGHT = 560
        window = (WIDTH, HEIGHT)
        COLS = 10
        ROWS = 10
        TITLE = 'Candy Crush Prototype'

        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(TITLE, icontitle="")

        self.screen = pygame.display.set_mode(window)
        sprite_sheet = SpriteSheet("res/candy_crush.png", window, candy_positions)
        self.board = Board(COLS, ROWS, sprite_sheet)
        self.cursor = Actor("res/cursor.png", cursor_positions, (0,0), (150, 75))
        self.background = pygame.image.load("res/background0.jpg")
        self.background = pygame.transform.scale(self.background, window)
        self.running = True
        signal.signal(signal.SIGINT, self.handler)
        

    def draw(self):
        """
        Draws sprites to the screen
        """
        self.screen.blit(self.background, (0,0))
        self.board.draw(self.screen)
        self.cursor.draw(self.screen)
        pygame.display.flip()

    
    def loop(self):
        """
        Runs the draw and update calls to handles game elements
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEMOTION:
                    self.cursor.update(pygame.mouse.get_pos(), off=(-30, -10))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.register_click(pygame.mouse.get_pos(), self.screen)
            self.draw()


    def handler(self, _signum, _frame):
        """
        Handles CTRL+C presses to exit the game
        """
        print("CTRL+C received...")
        self.running = False
        sys.exit(0)
