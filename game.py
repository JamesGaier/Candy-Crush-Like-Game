#!/usr/bin/env python3
"""
A prototype that gives me an idea of how to build a Candy Crush/Bejeweled like game
"""
import sys
import signal
import pygame
from candy_proto.engine.sheet import SpriteSheet
from candy_proto.engine.sheet_coords import candy_positions, cursor_positions
from candy_proto.game.actor import Actor
from candy_proto.game.board import Board

class Game:
    """
    Glue class that puts everything together
    """
    def __init__(self):
        window = (400, 560)
        cols = 10
        rows = 10
        title = "Candy Crush Prototype"

        # pylint: disable=E1101
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(title, icontitle="")

        self.screen = pygame.display.set_mode(window)
        sprite_sheet = SpriteSheet("res/candy_crush.png", window, candy_positions)
        self.board = Board(rows, cols, sprite_sheet)
        self.cursor = Actor("res/cursor.png", cursor_positions, (150, 75))
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
                # pylint: disable=E1101
                if event.type == pygame.QUIT:
                    self.running = False

                # pylint: disable=E1101
                if event.type == pygame.MOUSEMOTION:
                    self.cursor.update(pygame.mouse.get_pos(), off=(-30, -10))

                # pylint: disable=E1101
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.register_click(pygame.mouse.get_pos())
            self.draw()

    def handler(self, _signum, _frame):
        """
        Handles CTRL+C presses to exit the game
        """
        print("CTRL+C received...")
        self.running = False
        sys.exit(0)
