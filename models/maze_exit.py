import pygame
import os
from models.grid_size import GridSize

FILE_PATH = os.path.join(os.path.dirname(__file__), "door.png")


class MazeExit(pygame.sprite.Sprite):
    """The MazeExit class is to create the door in the window for the game to end.
         Inherits from sprite class.
        It loads the door image from a file and transforms it to the required scale.
    """
    def __init__(self):
        """Constructor for MazeExit class
        """
        super().__init__()
        image = pygame.image.load(FILE_PATH)
        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.rect = self.image.get_rect()
