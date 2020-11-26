import pygame
import os

from models.grid_size import GridSize

FILE_PATH = os.path.join(os.path.dirname(__file__), "images/brick.png")


class Wall(pygame.sprite.Sprite):
    """The Wall class is to create the wall in the window where player can't go.
         Inherits from sprite class.
        It loads the wall image from a file and transforms it to the required scale.
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(FILE_PATH)
        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.rect = self.image.get_rect()
