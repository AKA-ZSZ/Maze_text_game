from views.game_over_view import GameOverView
from .keyboard_controller import KeyboardController
import pygame

class GameOverController:
    '''Call display_message() function from GameOverView to display game over messages'''
    def __init__(self, window, maze):
        """Constructor for GameOverController. 

        Args:
            window (pygame.Surface): display the pygame window
            maze (Maze): an instance of the Maze class
        """
        self._maze=maze
        self._keyboard_controller=KeyboardController()

        # player must have 5 items in backpack to win
        self._maze_result=(len(self._maze.player.backpack)==5)
        self._view=GameOverView(window, self._maze_result, maze)

    def run(self):
        """Method to call functions from view to display messages"""
        # call functions from WelcomeView to display messages
        
        self._view.display_message()
        # if self.get_user_input()=="q":
        #     pygame.quit()
        # running=True
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.locals.QUIT:
        #             pygame.quit()

        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.locals.QUIT:
        #             running = False

    def get_user_input(self):
        """Method to get user input from keyboard_controller and return it

        Returns:
            str: key pressed by user
        """
        user_input = self._keyboard_controller.get_action()
        return user_input

    