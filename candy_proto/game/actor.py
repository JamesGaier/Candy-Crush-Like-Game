"""
Handles the cursor movement of the character
"""
import pygame
from candy_proto.engine.sheet import SpriteSheet

class Actor(pygame.sprite.Sprite):
    """
    Handles movement for the cursor
    """
    def __init__(self, image_path, sheet_positions, dim):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(image_path, dim, sheet_positions)
        self.image = sprite_sheet.get_sprite(sheet_positions[0])
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def update(self, pos, off=(0,0)):
        """
        Updates the cursor x and y position
        """
        self.x = pos[0] + off[0]
        self.y = pos[1] + off[1]

    def draw(self, screen):
        """
        Draws the cursor x and y position
        """
        screen.blit(self.image, (self.x,self.y))
