import pygame

from models.grid_size import GridSize


class Item(pygame.sprite.Sprite):
    """The Item class is to create the item in the window. Inherits from sprite class.
        It loads the item image from a file and transforms it to the required scale
    """

    def __init__(self, file):
        """Constructor for Item class.
        """
        super().__init__()
        image = pygame.image.load(file)

        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
