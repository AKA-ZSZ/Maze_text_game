from .abstract_view import AbstractView
import pygame


class WelcomeView(AbstractView):
    """ Display the Game Welcome view. Inherits from "AbstractView"
    """

    def __init__(self, window):
        self._window = window
        # Paint the screen white
        self._window.fill((255, 255, 255))

        pygame.font.init()
        self._arial = pygame.font.SysFont('arial', 25)

    def _display_message(self):
        """Template method: display the initial welcome message

        Returns:
            str: welcome message
        """

        msg = "Welcome to our maze game!!"
        msg_surface = self._arial.render(msg, True, (0, 0, 0))
        msg_text = msg_surface.convert_alpha()

        self._window.blit(msg_text, (155, 180))

    def _display_instructions(self, width, height, grid_size):
        """ Template method: display the game start instructions

        Args:
            width (int): width of pygame window
            height (int): height of pygame window
            grid_size (int): grid size of pygame window
        """
        
        # return "Press any key to start the game"
        # instruction="Press any key to start the game"
        size_controller = grid_size
        print(size_controller)
        rectangle_surface = pygame.Surface((200, 200))
        pygame.draw.rect(
            rectangle_surface, (128, 128, 128), (0, 0, 100, 30))
        pygame.draw.rect(
            rectangle_surface, (128, 128, 128), (0, 50, 100, 30))
        rectangle_surface.set_colorkey((0, 0, 0))
        self._window.blit(rectangle_surface.convert(),
                          (width/2 - size_controller, height/2))

        start = "Start"
        start_surface = self._arial.render(start, True, (0, 0, 0))
        self._window.blit(
            start_surface, (width/2 - size_controller/2, height/2))

        game_quit = "Quit"
        start_surface = self._arial.render(game_quit, True, (0, 0, 0))
        self._window.blit(
            start_surface, (width/2 - size_controller/2, height/2 + 50))
