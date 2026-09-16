import pygame
import random

class Board:
    def __init__(self, rows, cols, sprite_sheet):
        self.rows = rows 
        self.cols = cols 
        self.board = []
        self.sprite_sheet = sprite_sheet
        self.fill_board()
        self.selected_candy = []

    def fill_board(self):
        for r in range(self.rows):
            self.board.append([])
            for c in range(self.cols):
                self.board[r].append(None)
                
        sprites = self.sprite_sheet.get_sprites()
        for r in range(self.rows):
            for c in range(self.cols):
                rand_candy = random.randint(0,2)
                sprite = sprites[rand_candy]
                self.board[r][c] = sprite, pygame.Rect(c * sprite.width, r * sprite.height, sprite.width, sprite.height)


    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                screen.blit(self.sprite_sheet.get_sprite(self.board[r][c][0]), self.board[r][c][1])


    def update(self, screen):
        pass
    
    def swap_tiles(self, screen):
        r1, c1 = self.selected_candy[0] 
        r2, c2 = self.selected_candy[1] 
        
        if r1 < 0 or r1 >= len(self.board) or c1 < 0 or c1 >= len(self.board[r1]):
            return

        if r2 < 0 or r2 >= len(self.board) or c2 < 0 or c2 >= len(self.board[r2]):
            return
         
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dr, dc in dirs:
            r = r1 + dr
            c = c1 + dc  
            
            if r == r2 and c == c2:
                self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
                

    def find_tile(self, pos):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c][1].collidepoint(pos):
                    return r,c
    
    def register_click(self, pos, screen):
        tile = self.find_tile(pos)
        self.selected_candy.append(tile)

        if len(self.selected_candy) == 2:
            self.swap_tiles(screen)
            self.selected_candy = []
