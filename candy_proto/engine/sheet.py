"""
Creates a class for handling cutting out sprites from a sprite sheet
"""
import pygame


class SpriteSheet:
    """
    Responsiblity is to handle access to the spritesheet image i.e.
    1. Getting subimages from that image
    2. scaling the image to any resolution
    """
    def __init__(self, path, scale, positions):
        self.sprite_sheet = pygame.image.load(path).convert()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, scale)
        self.sheet_rect = self.sprite_sheet.get_rect()
        self.sheet_rect.topleft = (0,0)
        self.sprite_positions = positions

    def get_sprites(self):
        """
        Gets the positions of each of the sub images in the sprite sheet
        """
        return self.sprite_positions

    def get_sprite(self, rect):
        """
        Returns a pointer to the sprite image
        """
        return self.sprite_sheet.subsurface(rect)
