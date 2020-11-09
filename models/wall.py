import pygame
import os

from models.grid_size import GridSize

FILE_PATH = os.path.join(os.path.dirname(__file__), "brick.png")


class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load(FILE_PATH)
        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.rect = self.image.get_rect()
