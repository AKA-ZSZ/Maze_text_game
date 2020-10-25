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
        self._maze_map=self._maze.structure

    def run(self):
        """ This is the main method for our application.

        It runs an infinite loop, unless the user decides to quit.
        The `SystemExit` exception is raised by the child controllers.

        """

        welcome_controller = WelcomeController()

        running = True

        output_welcome = welcome_controller.run()
        # Display the list of students, and get user input
        while running:
            # try:
            #     output_welcome = welcome_controller.run()
            # except SystemExit:
            #     running = False
            #     continue

            # Display details about a student, and get user input
            game_controller = GameController(self._maze_map)
            try:
                action = game_controller.run()
            except SystemExit:
                running = False
