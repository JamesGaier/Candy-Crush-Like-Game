from enum import Enum
import pygame
import random



class Board:
    def __init__(self, rows, cols, sprite_sheet):
        self.rows = rows 
        self.cols = cols 
        self.board = []
        self.sprite_sheet = sprite_sheet
        self.selected_candy = []
        self.sprites = self.sprite_sheet.get_sprites()
        self.fill_board()
        

    def fill_board(self):
        for r in range(self.rows):
            self.board.append([])
            for c in range(self.cols):
                self.board[r].append([])
                
        for r in range(self.rows):
            for c in range(self.cols):
                rand_candy = random.randint(0,2)
                sprite = self.sprites[rand_candy]
                self.board[r][c] = [rand_candy, pygame.Rect(c * sprite.width, r * sprite.height, sprite.width, sprite.height)]


    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != None: 
                    sprite = self.sprites[self.board[r][c][0]]
                    screen.blit(self.sprite_sheet.get_sprite(sprite), self.board[r][c][1])


    def update(self, screen):
        pass


    def swap_cell(self, r1, c1, r2, c2):
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
        tmp = self.board[r1][c1][1].topleft  
        self.board[r1][c1][1].topleft = self.board[r2][c2][1].topleft
        self.board[r2][c2][1].topleft = tmp


    # sliding window check if there is a match
    def drop_candy_col(self, col):
        lo = 0
        for hi in range(len(self.board)):
            if len(self.board[hi][col]) != 0 and len(self.board[lo][col]) != 0 and self.board[hi][col][0] != self.board[lo][col][0]:
                if (hi - lo) > 2:
                    for r in range(lo, hi):
                        self.board[r][col][0] = random.randint(0,2) 
                lo = hi 


    def drop_candy_row(self, row):
        lo = 0
        for hi in range(len(self.board)):
            if len(self.board[row][hi]) != 0 and len(self.board[row][lo]) != 0 and self.board[row][hi][0] != self.board[row][lo][0]:
                if (hi - lo) > 2:
                    for c in range(lo, hi):
                        self.board[row][c][0] = random.randint(0,2)
                lo = hi 
        
    
    def check_matches(self, r1, c1, r2, c2):
        self.drop_candy_col(c1)
        self.drop_candy_col(c2)
        self.drop_candy_row(r1)
        self.drop_candy_row(r2)
        

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
                self.swap_cell(r1, c1, r2, c2)
                self.check_matches(r1, c1, r2, c2)


    def find_tile(self, pos):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != None and self.board[r][c][1].collidepoint(pos):
                    return r,c

    
    def register_click(self, pos, screen):
        tile = self.find_tile(pos)
        self.selected_candy.append(tile)

        if len(self.selected_candy) == 2:
            self.swap_tiles(screen)
            self.selected_candy = []
