from .abstract_view import AbstractView


class GameOverView(AbstractView):
    """ Display the Game over view. Inherits from "AbstractView"
    """

    def __init__(self, maze_result):
        """ initialize the game over view with one private attribite maze result

        Args:
            maze_result (str): win or lose

        Raises:
            ValueError: maze result must be "win" or "lose"
        """
        if type(maze_result)!=bool:
            raise ValueError("Game result must be win or lose")
        self._maze_result = maze_result

    def _display_message(self):
        """ Display whether a user won or lost

        Returns:
            str
        """
        if self._maze_result:
            return "You won the game, Congratulations"
        else:
            return "you lost"

    def _display_instructions(self):
        return "type r to restart, q to quit the game"
