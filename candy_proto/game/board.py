import pygame
import random

class Board:
    def __init__(self, rows, cols, sprite_sheet):
        self.rows = rows 
        self.cols = cols 
        self.board = []
        self.sprite_sheet = sprite_sheet
        self.fill_board()

    def fill_board(self):
        sprites = self.sprite_sheet.get_sprites()
        for r in range(self.rows):
            self.board.append([])
            for c in range(self.cols):
                rand_candy = random.randint(0,2)
                self.board[r].append(sprites[rand_candy])


    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                can = self.board[r][c]
                screen.blit(self.sprite_sheet.get_sprite(can), (can.width * r,can.height * c))


    def update(self, screen):
        pass
    
