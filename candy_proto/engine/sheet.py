"""
Creates a class for handling cutting out sprites from a sprite sheet
"""
import pygame


class SpriteSheet:
    def __init__(self, path, scale):
        self.sprite_sheet = pygame.image.load(path)
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, scale)
        self.sheet_rect = self.sprite_sheet.get_rect()
        self.sheet_rect.topleft = (0,0)
        # x, y, l, w
        self.sprite_positions = [
            pygame.Rect(0,0,63,75), # red fish
            pygame.Rect(64,0,60,75), # green fish
            pygame.Rect(0,78,63,75), # orange fish
            pygame.Rect(0,237,40,58), # green jelly bean
            pygame.Rect(0,405,40,58), # red jelly bean
            pygame.Rect(170,190,40,58) # blue jelly bean
        ]

    def get_sprites(self):
        return self.sprite_positions

    def get_sprite(self, rect):
        return self.sprite_sheet.subsurface(rect)
        
