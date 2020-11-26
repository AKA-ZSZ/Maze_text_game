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
        # # a list of command that the game would recognize
        # input_list = ("w", "a", "s", "d")
        # user_input=""

        # while user_input not in input_list:
        #     user_input=input()

        #     # if the input is not recognized by the game, user need to enter another command
        #     if user_input in input_list:
        #         return user_input

        # while True:
        #     for event in pygame.event.get():
        #         if event.type==pygame.locals.KEYDOWN:
        #             # print(pygame.key.name(event.key))
        #             return pygame.key.name(event.key)
        #         elif event.type == pygame.locals.QUIT:
        #             pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                # print(pygame.key.name(event.key))
                return pygame.key.name(event.key)
            elif event.type == pygame.locals.QUIT:
                pygame.quit()
