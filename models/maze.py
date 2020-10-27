from random import randrange
from models.player import Player


class Maze:

    def __init__(self):
        """The Maze class is to create a maze object for the maze text game

        Attrs:
            _structure (list(list)): The maze structure
            _items     (list(str)): The items include player and exit
            _locations (dict): The initial locatios of items
            _movements_player (list(int)): The total movements of the player in row and column before the end of game
            _player (Player): an instance of Player class

        """

        self._structure = [[""]]
        self._items = ["P", "M", "T", "R", "S", "G", "E"]
        self._locations = {
            "P": None,  # Player's location
            "M": None,
            "T": None,
            "R": None,
            "S": None,
            "G": None,
            "E": None,  # Exit's location
        }

        self._movements_player = [0, 0]

        # add a player
        self._player = Player()

    @property
    def structure(self):
        # maze data getter
        return self._structure

    @structure.setter
    def structure(self, structure):
        self._structure = structure

    @property
    def movements_player(self):
        return self._movements_player

    @movements_player.setter
    def movements_player(self, movements_player):
        self._movements_player = movements_player

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

    def _load_all_from_file(self, filename=None):
        """ Loads maze from a txt file

        Args:
            filename (str): filename to load students from

        Raises:
            Exception: if the file is missing, or we don't have access, or the CSV format is wrong
        """

        # Default filename
        if not filename:
            filename = 'maze.txt'

        maze_lines = list()

        with open(filename, "r") as f:

            for line in f.readlines():
                line = line.rstrip('\n')
                new_line = []
                for char in line:
                    new_line.append(char)
                maze_lines.append(new_line)
            self.structure = maze_lines

    def check_position(self, row, col):
        """True if the position is NOT an wall; otherwise False

        Args:
            row (int): the row number of the position
            col (int): the column number of the position
        """

        if self.structure[row][col] == "X":
            return False
        return True

    def find_random_spot(self):
        # generate random numbers
        # 1. if it's not, run again until it's an empty space - while loop
        # use check_position() to check if it's an empty space
        # the two numbers have min and max
        selected = False

        while not selected:
            # use randint
            maze_height = len(self.structure)
            maze_width = len(self.structure[0])
            spot_row = randrange(0, maze_height)
            spot_col = randrange(0, maze_width)
            if self.check_position(spot_row, spot_col):
                selected = True
                return (spot_row, spot_col)

    def is_item(self, row, col):
        item = self.structure[row][col]
        if item != "X" and item != " ":
            return True
        return False

    def move_player(self, x, y):
        maze_height = len(self.structure)
        maze_width = len(self.structure[0])

        new_player_location_x = self.locations["P"][0] + \
            self.movements_player[0]+x
        new_player_location_y = self.locations["P"][1] + \
            self.movements_player[1]+y

        if 0 <= new_player_location_x < maze_height and 0 <= new_player_location_y < maze_width:
            if self.check_position(new_player_location_x, new_player_location_y):
                # change spot of the old location of player to empty spot
                self.structure[self.locations["P"][0] +
                               self.movements_player[0]][self.locations["P"][1]+self.movements_player[1]] = " "

                # update the movements
                self.movements_player[0] = self.movements_player[0]+x
                self.movements_player[1] = self.movements_player[1]+y

                # replace new spot to be P
                self.structure[new_player_location_x
                               ][new_player_location_y] = "P"

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

        player_current_location = (
            self.locations["P"][0]+self.movements_player[0], self.locations["P"][1]+self.movements_player[1])
        items_not_p_e = ["M", "T", "R", "S", "G"]
        for item in items_not_p_e:

            if player_current_location == self.locations[item]:
                self.player.pickup(item)
                self.locations[item] = None
                return True

    def generate_random_spots(self):
        # randomly select 5 spots, player and exit during initialization
        max_spots_len = len(self.items)
        i = 0
        while i < max_spots_len:
            random_spot = self.find_random_spot()
            if self.check_position(random_spot[0], random_spot[1]):
                if not self.is_item(random_spot[0], random_spot[1]):
                    # record initial location
                    self.locations[self.items[i]] = random_spot

                    # write items into maze map
                    self.structure[random_spot[0]
                                   ][random_spot[1]] = self.items[i]

                    i += 1
