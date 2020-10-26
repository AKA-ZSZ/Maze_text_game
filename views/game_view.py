
class GameView:
    """ Displays the maze, move options and the player items
    """

    def __init__(self, maze):
        """ initialize private attribute maze

        Args:
            maze (object): instance of the Maze class

        Raises:
            TypeError: maze must be object
        """
        if not isinstance(maze, object):
            raise TypeError("Maze must be object")

        self._maze = maze

    def display_move_options(self):
        """ Public: prints move options
        """
        print(self._display_move_options())

    def display_maze(self):
        """ Public: prints maze text
        """
        print(self._display_maze())

    def get_items(self, items):
        """ Public: prints item in backpack
        """
        print(self._get_items(items))

    def _get_items(self, items):
        """ Display items in player backpack

            Returns
                str: items in backpack text 
        """

        return f"""Get an item!\nYou have: {items}.\n"""

    def _display_move_options(self):
        """ Displays move options for users

        Returns:
            str: move options text
        """
        return "type w,a,s,d to move the player: "

    def _display_maze(self):
        """ Display the maze

        Returns:
            str: maze text
        """
        text = ""
        for line in self._maze.structure:
            text += ("").join(line)
            text += "\n"
        return text
