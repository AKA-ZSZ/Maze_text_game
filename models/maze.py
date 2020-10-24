from random import randrange
from models.player import Player


class Maze:
    def __init__(self, filename):

        self._filename = filename
        self._items = ["P", "M", "T", "E"]
        self._locations = {
            "P": None,  # Player's location
            "M": None,
            "T": None,
            "E": None,  # Exit's location
        }

        # read a file
        with open(filename, "r") as f:
            maze_lines = f.readlines()

            self._maze_lines = maze_lines

        self._maze_width = len(self._maze_lines[0].rstrip("\n"))
        self._maze_height = len(self.maze_lines)

        # add a player
        self._player = Player()

        # initialize the maze
        self.initialize_game()

    # properties
    @property
    def filename(self):
        return self._filename

    @property
    def maze_lines(self):
        # maze data getter

        return self._maze_lines

    @maze_lines.setter
    def maze_lines(self, maze_lines):
        self._maze_lines = maze_lines

    @property
    def maze_width(self):
        return self._maze_width

    @property
    def maze_height(self):
        return self._maze_height

    @property
    def items(self):
        return self._items

    @property
    def locations(self):
        return self._locations

    @property
    def player(self):
        return self._player

    # methods

    def can_move_to(self, row, col):
        """True if the position is NOT an wall; otherwise False

        Args:
            row ([type]): [description]
            col ([type]): [description]
        """

        # list_lines[row][col]==" " - True
        if self.maze_lines[row][col] == "X":
            return False
        return True

    def display(self):
        # traversing
        for line in self.maze_lines:
            print(line.rstrip('\n'))

    def find_random_spot(self):
        # generate 2 random numbers
        # 1. if it's not, run again until it's an empty space - while loop
        # use check() to check if it's an empty space
        # the two numbers have min and max
        selected = False

        while not selected:
            # use randint

            spot_row = randrange(0, self.maze_height)
            spot_col = randrange(0, self.maze_width)
            if self.can_move_to(spot_row, spot_col):
                selected=True
                return (spot_row, spot_col)

    def is_item(self, row, col):
        item = self.maze_lines[row][col]
        if item != "X" and item != " ":
            return True
        return False

    def initialize_game(self):

        # random select 4 empty spots

        max_spots_len = len(self.items)
        i = 0
        while i < max_spots_len:

            random_spot = self.find_random_spot()

            if self.can_move_to(random_spot[0], random_spot[1]):
                if not self.is_item(random_spot[0], random_spot[1]):
                    # track location
                    self.locations[self.items[i]] = random_spot

                    # overwrite

                    line_replaced = self.maze_lines[random_spot[0]]
                    line_replaced = line_replaced[0:random_spot[1]] + \
                        self.items[i]+line_replaced[(random_spot[1]+1):]
                    self.maze_lines[random_spot[0]] = line_replaced

                    i += 1

    def is_exit(self, location):
        """Check if the player is at the exit

        Args:
            location (tuple): current position of player in the maze

        Returns:
            boolean: True if the player reaches the exit. otherwise false
        """
        if self.locations["E"] == location:
            return True
        return False

    def get_item(self):
        # T represents Treasure
        
        self.player.pick_up_item("T")
        print("\nGet a Treasure!")
        print(f"You have: ${self.player.backpack}.\n")

        # treasure is opened, avoid repetitive error
        self.locations["T"]=None
            