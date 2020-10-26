from .abstract_view import AbstractView


class GameOverView(AbstractView):
    """ Display the Game over view. Inherits from "AbstractView"
    """

    def __init__(self, maze_result):
        """ initialize private attribute maze result

        Args:
            maze_result (bool): if player has 5 items in list then maze_result
                                is True. Otherwise maze result is False

        Raises:
            ValueError: maze result must be Boolean
        """
        if type(maze_result) != bool:
            raise ValueError("Game result must be win or lose")
        self._maze_result = maze_result

    def _display_message(self):
        """ Template method: display the message according to True or False
            True: win, False: lose

        Returns:
            str: display the text according to win or lose
        """

        if self._maze_result:
            return "You won the game, Congratulations"
        else:
            return "you lost"

    def _display_instructions(self):
        """ Template method: to be implemented in pygame for repeating games
        """
        pass
