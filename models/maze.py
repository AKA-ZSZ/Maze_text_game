from random import randrange
from models.player import Player
from models.wall import Wall
from models.items import Items
from models.maze_exit import MazeExit
import pygame

import requests


from models.grid_size import GridSize


class Maze:

    def __init__(self):
        """The Maze class is to create a maze object for the maze text game

        Attrs:
            _structure (list(list)): The maze structure
            _items     (list(str)): The items include player and exit
            _locations (dict): The initial locatios of items
            _movements_player (list(int)): The total movements of the player in row and column before the end of game
            _player (Player): an instance of Player class
            _time_left (float): The remaining time of the maze game
            _score (int): The number of picked items
            _API_URL (str): The Flask API url (const)
            _scores (list(int)): a list containing all winners' high scores
        """

        self._structure = [[""]]
        self._items = ["P", "B", "K", "H", "S", "G", "E"]
        self._locations = {
            "P": None,  # Player's location
            "B": None,
            "K": None,
            "H": None,
            "S": None,
            "G": None,
            "E": None,  # Exit's location
        }

        self._movements_player = [0, 0]

        # add a player
        self._player = Player()
        # add maze exit
        self._maze_exit = MazeExit()

        self._wall = pygame.sprite.Group()
        self._maze_items = pygame.sprite.Group()

        self._time_left = 30.00  # in seconds
        self._score = 0

        # flask
        self._API_URL = "http://localhost:5000/api"
        self._scores = list()

    @property
    def row(self):
        """ Get length of maze_text row

        Returns:
            int : len(self._structure[0])
        """
        return len(self._structure[0])

    @property
    def col(self):
        """ Get length of maze_text column

        Returns:
            int: len(self._structure)
        """
        return len(self._structure)

    @property
    def maze_exit(self):
        """ Get maze exit object

        Returns:
            object: self._maze_exit
        """
        return self._maze_exit

    @property
    def player(self):
        """ Get player object

        Returns:
            object: self._player
        """
        return self._player

    @property
    def structure(self):
        """ Get structure nested list

        Returns:
            list: self._structure
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        """ Set structure nested list

        Returns:
            None
        """
        self._structure = structure

    @property
    def movements_player(self):
        """ Get player movements, i.e. how many times
            player moved since the game started

        Returns:
            list: self._movements_player
        """
        return self._movements_player

    @movements_player.setter
    def movements_player(self, movements_player):
        """ Set player movements
        """
        self._movements_player = movements_player

    @property
    def items(self):
        """ Get list of items in maze

        Returns:
            list: self._items
        """
        return self._items

    @property
    def locations(self):
        """ Get location of each item in maze

        Returns:
            dictionary: self._locations
        """
        return self._locations

    @property
    def scores(self):
        """ Get player scores

        Returns:
            list: new_scores
        """

        new_scores = []
        for score in sorted(self._scores, reverse=True):
            new_dict = dict()
            new_dict["name"] = score[0]
            new_dict["score"] = score[1]
            new_scores.append(new_dict)
        return new_scores

    def add_score(self, score):
        """ Add score to score list

        Args:
            score (dict): player score
        """

        self._scores.append(score)

    def create_wall(self):
        """Method to place the wall object at a postion that is not "X".
            Uses the check_position() function to verify the position to place the wall.
        """

        for height in range(self.col):
            for width in range(self.row):

                if not self.check_position(height, width):
                    brick = Wall()
                    brick.rect.x = width * GridSize.SIZE
                    brick.rect.y = height * GridSize.SIZE

                    self._wall.add(brick)

    # methods

    def create_player(self):
        """Method to create player

        Returns:
            (Player): an instance of Player class
        """
        self._player.rect.x = self.locations.get("P")[1] * GridSize.SIZE
        self._player.rect.y = self.locations.get("P")[0] * GridSize.SIZE
        return self._player

    def create_maze_exit(self):
        """Method to create exit

        Returns:
            (MazeExit): an instance of MazeExit class
        """
        self._maze_exit.rect.x = self.locations.get("E")[1] * GridSize.SIZE
        self._maze_exit.rect.y = self.locations.get("E")[0] * GridSize.SIZE
        return self._maze_exit

    def create_items(self):
        items = Items()
        for player_item in ["B", "K", "H", "S", "G"]:
            items.image_sprites.get(player_item).rect.x = self.locations.get(
                player_item)[1] * GridSize.SIZE
            items.image_sprites.get(player_item).rect.y = self.locations.get(
                player_item)[0] * GridSize.SIZE

            self._maze_items.add(items.image_sprites.get(player_item))

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
        """Function to generate a random spot until an empty spot on the grid is found.
            Uses check_position() to check the position generated.

        Returns:
            (tuple): random empty position generated
        """
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
        """Returns True if the item in the given position is neither a wall nor an empty space,
            False, otherwise 

        Args:
            row (int): x-position of the item 
            col (int): y-position of the item
        """
        item = self.structure[row][col]
        if item != "X" and item != " ":
            return True
        return False

    def move_player(self, x, y):
        """Method to move the player by x and y spots, change old location of the player to an empty spot,
            update the movements list and replace the new spot with "P"

        Args:
            x (int): number of spots on x axis
            y (int): number of spots on y axis
        """
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
        """Method to pickup items in the maze.

        Returns:
            (boolean): True if player is at the same location as an item
        """
        player_current_location = (
            self.locations["P"][0]+self.movements_player[0], self.locations["P"][1]+self.movements_player[1])
        items_not_p_e = ["B", "K", "H", "S", "G"]
        for item in items_not_p_e:

            if player_current_location == self.locations[item]:
                self.player.pickup(item)
                self.locations[item] = None
                return True

    def generate_random_spots(self):
        """Generates 7 random spots to place the items, player and exit."""
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

    # calculate the final score when user wins
    def cal_final_score(self):
        return float("{:.2f}".format(self._time_left*self._score))

    # ask winner for name in console and send a request
    def add_name_score(self):
        winner_name = input('Please enter your name:')
        req = requests.put(
            f"{self._API_URL}/new", json={"name": winner_name, "score": self.cal_final_score()})

        if req.status_code == 204:
            return True

        return False

    # print all scores on {self._API_URL}/list
    def print_scores(self):
        data = requests.get(f"{self._API_URL}/list").json()
        output = "\n".join(
            [f"{score['name']}: {score['score']}" for score in data["scores"]]
        )
        print(output)
        return data
