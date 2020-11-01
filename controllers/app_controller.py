from models.maze import Maze

from controllers.welcome_controller import WelcomeController
from controllers.game_controller import GameController
from controllers.game_over_controller import GameOverController

import pygame
import random
import pygame.locals


class App:
    '''Main class for the application. It interacts with Maze model and three controllers:
       WelcomeController
       GameController
       GameOverController'''

    def __init__(self, filename=None):
        """ Call the classmethod to load all students from the CSV """
        self._maze = Maze()
        self._maze._load_all_from_file(filename)

        # pygame
        pygame.init()
        # pygame.font.init()
        # arial = pygame.font.SysFont('arial', 18)

        # window
        window = pygame.display.set_mode((500, 500))
        window.set_colorkey((255, 255, 255))
        clock = pygame.time.Clock()

        self._window=window

        

    def run(self):
        """ This is the main method for our application.

        It runs an infinite loop, unless the user decides to quit.
        The `SystemExit` exception is raised by the child controllers.

        """

        

        welcome_controller = WelcomeController(self._window)
        

        running = True

        welcome_controller.run()
        pygame.display.update()
        
        welcome_controller.get_input()

        while running:
            # Paint the screen white
            self._window.fill((255, 255, 255))

            game_controller = GameController(self._maze)

            result = game_controller.run()

            if result:
                running = False

        # result can be win or loss

        game_over_controller = GameOverController(self._maze)
        game_over_controller.run()
