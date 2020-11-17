import pygame
import os

from models.grid_size import GridSize

FILE_PATH = os.path.join(os.path.dirname(__file__), "item.png")


class Items(pygame.sprite.Sprite):
    """The Items class is to create the item in the window. Inherits from sprite class.
        It loads the item image from a file and transforms it to the required scale
    """
    def __init__(self):
        """Constructor for Items class.
        """
        super().__init__()
        image = pygame.image.load(FILE_PATH)
        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.rect = self.image.get_rect()
