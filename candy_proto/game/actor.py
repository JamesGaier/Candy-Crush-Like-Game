import pygame
from ..engine.sheet import SpriteSheet

class Actor(pygame.sprite.Sprite):
    def __init__(self, image_path, sheet_positions, position, dim):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(image_path, dim, sheet_positions)
        self.image = sprite_sheet.get_sprite(sheet_positions[0])
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def update(self, pos, off=(0,0)):
        self.x = pos[0] + off[0]
        self.y = pos[1] + off[1]

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
