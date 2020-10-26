from models.maze import Maze

from controllers.welcome_controller import WelcomeController
from controllers.game_controller import GameController
from controllers.game_over_controller import GameOverController

class App:
    

    # def run(self):
    #     pass

    def __init__(self, filename=None):
        """ Call the classmethod to load all students from the CSV """
        self._maze = Maze()
        self._maze._load_all_from_file(filename)
       

    def run(self):
        """ This is the main method for our application.

        It runs an infinite loop, unless the user decides to quit.
        The `SystemExit` exception is raised by the child controllers.

        """

        welcome_controller = WelcomeController()

        running = True

        welcome_controller.run()

        while running:
            
            game_controller = GameController(self._maze)
            # try:
            #     result = game_controller.run()
            # except SystemExit:
            #     running = False
            result = game_controller.run()

            if result:
                running=False

        # result can be win or loss

        game_over_controller=GameOverController(self._maze)
        game_over_controller.run()
