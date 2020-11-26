import pygame
import os

from models.grid_size import GridSize

FILE_PATH_H = os.path.join(os.path.dirname(__file__), "images/item.png")
FILE_PATH_G = os.path.join(os.path.dirname(__file__), "images/gun.png")
FILE_PATH_S = os.path.join(os.path.dirname(__file__), "images/sword.png")
FILE_PATH_K = os.path.join(os.path.dirname(__file__), "images/key.png")
FILE_PATH_B = os.path.join(os.path.dirname(__file__), "images/bomb.png")


class Item(pygame.sprite.Sprite):

    def __init__(self, file):
        super().__init__()
        image = pygame.image.load(file)

        self.image = pygame.transform.scale(
            image, (GridSize.SIZE, GridSize.SIZE))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()


class Items:

    def __init__(self):
        self.image_sprites = {
            "B": Item(FILE_PATH_B),
            "K": Item(FILE_PATH_K),
            "H": Item(FILE_PATH_H),
            "S": Item(FILE_PATH_S),
            "G": Item(FILE_PATH_G),
        }
