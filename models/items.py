import os
from .item import Item

FILE_PATH_H = os.path.join(os.path.dirname(__file__), "images/item.png")
FILE_PATH_G = os.path.join(os.path.dirname(__file__), "images/gun.png")
FILE_PATH_S = os.path.join(os.path.dirname(__file__), "images/sword.png")
FILE_PATH_K = os.path.join(os.path.dirname(__file__), "images/key.png")
FILE_PATH_B = os.path.join(os.path.dirname(__file__), "images/bomb.png")


class Items:
    """ Composition relation with Item Class
    """

    def __init__(self):
        """ instantiate each item that matches with Item in maze
        """
        self.image_sprites = {
            "B": Item(FILE_PATH_B),
            "K": Item(FILE_PATH_K),
            "H": Item(FILE_PATH_H),
            "S": Item(FILE_PATH_S),
            "G": Item(FILE_PATH_G),
        }
