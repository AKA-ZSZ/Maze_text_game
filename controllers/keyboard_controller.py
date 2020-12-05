import pygame
import pygame.locals


class KeyboardController:
    def __init__(self):
        pass

    def get_action(self):
        """Method to get user input

        Returns:
            str: key presssed by the user
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                return pygame.key.name(event.key)
            elif event.type == pygame.locals.QUIT:
                pygame.quit()
