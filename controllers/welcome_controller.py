from views.welcome_view import WelcomeView
from .keyboard_controller import KeyboardController
import pygame


class WelcomeController:
    '''Call functions from WelcomeView to display welcome messages'''

    def __init__(self, window, width, height, grid_size):
        self._keyboard_controller = KeyboardController()
        self._view = WelcomeView(window)
        self._width = width
        self._height = height
        self.grid_size = grid_size

    def run(self):
        """This is the main function that calls function from WelcomeView to display messages"""
        # call functions from WelcomeView to display messages
        
        self._view.display_message()
        self._view.display_instructions(
            self._width, self._height, self.grid_size)


    def get_input(self):
        """Method to get user input

        Returns:
            str: key pressed by the user
        """
        # get user input from KeyboardController

        text_field_width = self._width / 2 - self.grid_size
        text_field_height = self._height/2 + 50
        start_game = False
        while not start_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (text_field_width) < pygame.mouse.get_pos()[0] < (text_field_width + 100) and (text_field_height) < pygame.mouse.get_pos()[1] < (text_field_height + 30):
                        print("Quit the game")
                        pygame.quit()
                    elif (text_field_width) < pygame.mouse.get_pos()[0] < (text_field_width + 100) and (text_field_height - 50) < pygame.mouse.get_pos()[1] < (text_field_height - 20):
                        start_game = True
