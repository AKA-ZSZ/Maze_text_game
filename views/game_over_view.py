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
        if maze_result != "win" and maze_result != "lose":
            raise ValueError("Game result must be win or lose")
        self._maze_result = maze_result

    def _display_message(self):
        """ Display whether a user won or lost

        Returns:
            str
        """
        if self._maze_result == "win":
            return "You won the game, Congratulations"
        elif self._maze_result == "lose":
            return "you lost"


