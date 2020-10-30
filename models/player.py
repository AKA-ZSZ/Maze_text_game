class Player:
    def __init__(self, backpack=None):
        """The Player class is to create a player in maze text game

        Args:
            backpack (list): The initial backpack of the player. Defaults to [].

        Attrs:
            _backpack (list): The backpack of the player

        Raises:
            TypeError: when the backpack argument is not a list or or the length of arguments is not 1
        """
        if backpack is None:
            backpack = []

        if type(backpack) != list:
            raise TypeError

        # [item1,item2...]
        self._backpack = backpack

    @property
    def backpack(self):
        return self._backpack

    def pickup(self, item):
        """Player can pick up items and put into backpack

        Args:
            item (str): The items in the backpack

        Raises:
            TypeError: When the item argument is not str or the length of arguments is not 1
        """
        if type(item) != str:
            raise TypeError
        if item not in self.backpack:
            self.backpack.append(item)
