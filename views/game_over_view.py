from .abstract_view import AbstractView
import pygame

class GameOverView(AbstractView):
    """ Display the Game over view. Inherits from "AbstractView"
    """

    def __init__(self, window, maze_result):
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

        self._window = window
        self._window.fill((255, 255, 255))

        pygame.font.init()
        self._arial = pygame.font.SysFont('arial', 18)

        # initialization
        self._display_message()
        pygame.display.update()


    def _display_message(self):
        """ Template method: display the message according to True or False
            True: win, False: lose

        Returns:
            str: display the text according to win or lose
        """

        if self._maze_result:
            msg = "You won the game, Congratulations, press 'q' to quit"
        else:
            msg = "you lost, press 'q' to quit"

        msg_surface=self._arial.render(msg,True,(0,0,0))
        msg_text=msg_surface.convert_alpha()

        self._window.blit(msg_text,(155,180))

    def _display_instructions(self):
        """ Template method: to be implemented in pygame for repeating games
        """
        pass
